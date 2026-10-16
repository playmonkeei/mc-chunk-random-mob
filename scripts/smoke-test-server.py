#!/usr/bin/env python3
"""Boot a pinned Paper build with the release JAR in an isolated build directory."""

import argparse
import hashlib
from pathlib import Path
import queue
import shutil
import subprocess
import threading
import time


PROJECT = Path(__file__).resolve().parent.parent


def paper_versions():
    return [
        line.split()
        for line in (PROJECT / "test-servers/paper-versions.tsv").read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]


def smoke_test(version, plugin_jar):
    _, build, _, expected_sha = next(row for row in paper_versions() if row[0] == version)
    # These worlds are disposable; never touch the manually played test servers.
    directory = PROJECT / "build/smoke-servers" / version
    if directory.exists():
        shutil.rmtree(directory)
    (directory / "plugins").mkdir(parents=True)
    shutil.copy2(plugin_jar, directory / "plugins/ChunkMobChallenge.jar")
    (directory / "eula.txt").write_text("eula=true\n")
    (directory / "server.properties").write_text(
        "server-ip=127.0.0.1\nserver-port=0\nonline-mode=true\n"
        "level-type=minecraft:flat\ngenerate-structures=false\n"
        'generator-settings={"layers":[{"block":"minecraft:bedrock","height":1},{"block":"minecraft:dirt","height":2},{"block":"minecraft:grass_block","height":1}],"biome":"minecraft:plains"}\n'
        "view-distance=2\nsimulation-distance=2\nmax-players=1\n"
        "pause-when-empty-seconds=-1\n"
    )
    # Cache downloads outside the disposable server directory.
    cache = PROJECT / "build/paper-downloads"
    cache.mkdir(parents=True, exist_ok=True)
    server_jar = cache / f"paper-{version}-{build}.jar"
    if not server_jar.exists() or hashlib.sha256(server_jar.read_bytes()).hexdigest() != expected_sha:
        subprocess.run([
            "curl", "--fail", "--silent", "--show-error", "--location", "--retry", "3",
            "--connect-timeout", "15", "--max-time", "180",
            "--header", "User-Agent: chunk-mob-challenge-test (https://github.com/playmonkeei/mc-chunk-random-mob)",
            f"https://fill-data.papermc.io/v1/objects/{expected_sha}/{server_jar.name}",
            "--output", str(server_jar),
        ], check=True)
    if hashlib.sha256(server_jar.read_bytes()).hexdigest() != expected_sha:
        raise RuntimeError(f"Paper {version}: SHA-256 mismatch")

    process = subprocess.Popen(
        ["java", "-Dterminal.jline=false", "-Dterminal.ansi=false",
         "-Xms256M", "-Xmx1G", "-jar", str(server_jar), "--nogui"],
        cwd=directory, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, text=True, bufsize=1,
    )
    output = queue.Queue()

    def read_output():
        for line in process.stdout:
            output.put(line)
        output.put(None)

    threading.Thread(target=read_output, daemon=True).start()
    lines = []
    started = False
    checked = False
    stopped = False
    deadline = time.monotonic() + 240
    try:
        while time.monotonic() < deadline:
            try:
                line = output.get(timeout=1)
            except queue.Empty:
                continue
            if line is None:
                break
            print(line, end="", flush=True)
            lines.append(line)
            if "[ChunkMobChallenge] Disabling" in line and not stopped:
                raise RuntimeError(f"Paper {version}: plugin disabled unexpectedly")
            if "Done (" in line and not started:
                started = True
                process.stdin.write("version ChunkMobChallenge\ncc status\ncc reload\n")
                process.stdin.flush()
            if "mobs.yml wurde neu geladen." in line:
                checked = True
            if checked and not stopped:
                process.stdin.write("stop\n")
                process.stdin.flush()
                stopped = True
        else:
            raise RuntimeError(f"Paper {version}: smoke test timed out")
        process.wait(timeout=30)
    finally:
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
        process.stdin.close()
        process.stdout.close()
        (directory / "smoke-test.log").write_text("".join(lines))

    log = "".join(lines)
    required = ["ChunkMobChallenge ist bereit.", "Mob-Pool geladen:",
                "ChunkMobChallenge version", "Keine Challenge vorhanden.",
                "Stopping server", "Disabling ChunkMobChallenge"]
    missing = [marker for marker in required if marker not in log]
    errors = [marker for marker in ("ERROR]:", "Error occurred while", "Could not load",
              "NoSuchMethodError", "NoClassDefFoundError", "Exception") if marker in log]
    if process.returncode != 0 or not started or not checked or missing or errors:
        raise RuntimeError(f"Paper {version}: smoke test failed (missing={missing}, errors={errors})")
    print(f"PASS: Paper {version}, identical release JAR, startup/status/reload/shutdown")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", choices=[row[0] for row in paper_versions()])
    parser.add_argument("plugin_jar", type=Path)
    args = parser.parse_args()
    smoke_test(args.version, args.plugin_jar.resolve(strict=True))
