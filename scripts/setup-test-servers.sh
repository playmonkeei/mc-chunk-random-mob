#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH='' cd -- "$SCRIPT_DIR/.." && pwd)
SERVERS_DIR="$PROJECT_DIR/test-servers"
USER_AGENT="chunk-mob-challenge-test/1.0 (https://github.com/playmonkeei)"

download_paper() {
    version=$1
    url=$2
    expected_sha=$3
    directory="$SERVERS_DIR/$version"
    target="$directory/server.jar"

    mkdir -p "$directory/plugins"
    if [ ! -f "$directory/server.properties" ]; then
        cp "$directory/server.properties.example" "$directory/server.properties"
    fi
    if [ -f "$target" ]; then
        actual_sha=$(shasum -a 256 "$target" | awk '{print $1}')
        if [ "$actual_sha" = "$expected_sha" ]; then
            echo "Paper $version ist bereits vorhanden und verifiziert."
            return
        fi
        echo "Paper $version hat eine falsche Prüfsumme und wird neu geladen."
    fi

    echo "Lade Paper $version herunter ..."
    curl --fail --location --header "User-Agent: $USER_AGENT" "$url" --output "$target.tmp"
    actual_sha=$(shasum -a 256 "$target.tmp" | awk '{print $1}')
    if [ "$actual_sha" != "$expected_sha" ]; then
        echo "FEHLER: SHA-256-Prüfung für Paper $version fehlgeschlagen." >&2
        exit 1
    fi
    mv "$target.tmp" "$target"
}

echo "Baue ChunkMobChallenge ..."
"$PROJECT_DIR/gradlew" -p "$PROJECT_DIR" clean build
PLUGIN_JAR=$("$PROJECT_DIR/gradlew" -p "$PROJECT_DIR" -q printPluginJar)

while read -r version build _channel sha; do
    case "$version" in ''|\#*) continue ;; esac
    download_paper "$version" "https://fill-data.papermc.io/v1/objects/$sha/paper-$version-$build.jar" "$sha"
    cp "$PLUGIN_JAR" "$SERVERS_DIR/$version/plugins/ChunkMobChallenge.jar"
done < "$SERVERS_DIR/paper-versions.tsv"

echo
echo "Alle vier Testserver sind bereit:"
echo "  Paper 26.1.1: ./scripts/start-test-server.sh 26.1.1 (Paper Alpha)"
echo "  Paper 26.1.2: ./scripts/start-test-server.sh 26.1.2"
echo "  Paper 26.2:   ./scripts/start-test-server.sh 26.2"
echo "  Paper 26.3:   ./scripts/start-test-server.sh 26.3"
echo "  Verbindung:   localhost:25565 (immer nur einen Server gleichzeitig starten)"
