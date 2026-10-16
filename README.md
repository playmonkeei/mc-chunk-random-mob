<div align="center">

# ⚔️ Chunk Mob Challenge

### Jeder neue Chunk bringt einen neuen Gegner. Wie weit kommt ihr?

Ein zufälliger Mob, eine 16×16-Arena und ein Ziel: **Besiegt den echten Enderdrachen.**<br>
Spielt allein oder mit Freunden – an einem Abend oder über mehrere Streams hinweg.

<p>
  <a href="#kompatibilitaet"><img alt="Minecraft Java 26.1.x, 26.2 und 26.3" src="https://img.shields.io/badge/Minecraft_Java-26.1.x%20%7C%2026.2%20%7C%2026.3-62B47A?style=for-the-badge"></a>
  <a href="https://papermc.io/downloads/paper/"><img alt="Für Paper-Server" src="https://img.shields.io/badge/Server-Paper-2C2E35?style=for-the-badge"></a>
  <img alt="Java 25 erforderlich" src="https://img.shields.io/badge/Java-25-E76F00?style=for-the-badge">
  <img alt="Solo und Koop" src="https://img.shields.io/badge/Spielmodus-Solo%20%26%20Koop-7C6AE6?style=for-the-badge">
</p>

**[⬇️ Plugin herunterladen](https://github.com/playmonkeei/mc-chunk-random-mob/releases/latest)**
&nbsp;·&nbsp; **[🚀 Schnellstart](#schnellstart)**
&nbsp;·&nbsp; **[⌨️ Befehle](#befehle)**
&nbsp;·&nbsp; **[🐛 Fehler melden](https://github.com/playmonkeei/mc-chunk-random-mob/issues/new/choose)**

</div>

---

## 🎮 Was euch erwartet

Betretet einen neuen Chunk und stellt euch seinem zufälligen Gegner. Eine
persönliche Worldborder hält euch in der Arena, bis der Challenge-Mob besiegt
ist. Danach entscheidet ihr selbst, wohin es weitergeht.

| | Euer Run |
| --- | --- |
| 🎲 **Jeder Chunk überrascht** | Alle Mobs im aktiven Pool haben dieselbe Chance – von der Kuh bis zum Wither. |
| 🛠️ **Eure Mob-Auswahl** | Entscheidet selbst, welche Mobs in eurem Run vorkommen dürfen. [So passt ihr die Auswahl an ↓](#mob-auswahl) |
| 🤝 **Gemeinsam oder aufteilen** | Kämpft im selben Chunk zusammen oder eröffnet nach einem Sieg getrennte Runden. |
| 🧭 **Euer Tempo** | Bleibt im sicheren Chunk zurück oder wagt euch direkt in den nächsten Kampf. |
| 💾 **Über mehrere Sessions** | Positionen, Gegner, Fortschritt und Statistiken bleiben nach einem Serverneustart erhalten. |
| ⏱️ **Nur aktive Spielzeit** | Wenn niemand aus dem Run online ist, pausiert die Challenge-Zeit. |
| 🐉 **Ein klares Ziel** | Gewonnen ist der Run, sobald ihr den echten Enderdrachen im End besiegt. |

Bereits mehrfach von verschiedenen Streamern auf **Minecraft 26.2** problemlos
gespielt.

<a id="schnellstart"></a>

## 🚀 In wenigen Minuten losspielen

### Das braucht ihr

| Voraussetzung | Für euren Server |
| --- | --- |
| **Minecraft Java Edition** | 26.1.1, 26.1.2, 26.2 oder 26.3 |
| **Serversoftware** | [Paper herunterladen](https://papermc.io/downloads/paper/) |
| **Java** | Version 25 auf dem Server |
| **Plugin** | JAR aus dem [aktuellen GitHub Release](https://github.com/playmonkeei/mc-chunk-random-mob/releases/latest) |

Auf euren Clients ist **keine zusätzliche Mod erforderlich**. Verbindet euch mit
der passenden Minecraft-Version mit eurem Paper-Server.

### Installieren und starten

1. Richtet euren Paper-Server ein, startet ihn einmal und akzeptiert die
   Minecraft-EULA in `eula.txt`.
2. Stoppt den Server und legt die heruntergeladene Plugin-JAR in seinen Ordner
   `plugins`.
3. Startet den Server wieder. In der Konsole erscheint
   `ChunkMobChallenge ist bereit.`.
4. Verbindet euch alle mit dem Server. Der Spielleiter benötigt Operatorrechte
   oder die passenden [Berechtigungen](#berechtigungen).
5. Stellt euch an euren gewünschten Startpunkt. Der Spielleiter startet **im
   Spiel** mit:

   ```text
   /cc start
   ```

Alle bereits verbundenen Spieler werden zum Spielleiter teleportiert und
beginnen gemeinsam in seinem Chunk.

> [!TIP]
> Verwendet eine Welt, in der der ursprüngliche Enderdrache noch lebt. Ist er
> bereits besiegt, lässt sich dort kein neuer Run starten.

<a id="spielregeln"></a>

## 🧭 So läuft euer Run

**Chunk betreten → Gegner besiegen → Border öffnet sich → weiterziehen.**

Im selben umkämpften Chunk teilt ihr euch einen Gegner und seine
Lebenspunkteanzeige. Nach dem Sieg könnt ihr zusammenbleiben oder in
unterschiedlichen Chunks weiterspielen. Wer später einen bereits umkämpften
Chunk betritt, steigt in dessen laufende Runde ein.

| Situation | Das passiert |
| --- | --- |
| 🧱 Ihr wollt während des Kampfes aus dem Chunk | Die Worldborder hält euch zurück. Auch Enderperlen, Chorusfrüchte, Portale und fremde Teleports umgehen den Lock nicht. |
| 🔥 Der Gegner stirbt durch die Umgebung | Die Runde zählt als gewonnen – auch bei Feuer, Ertrinken, Ersticken oder einer Creeper-Selbstexplosion. |
| 🐄 Ihr begegnet normalen Mobs | Sie gehören nicht zur Challenge-Runde und bleiben uneingeschränkt. |
| 💀 Ein Spieler stirbt im normalen Modus | Er beginnt nach dem Respawn eine neue Runde im Respawn-Chunk. Die anderen können weiterspielen. |
| ☠️ Ein Spieler stirbt in Hardcore | Der gesamte Run endet für alle Teilnehmer. |
| 🐉 Ein zufälliger Challenge-Enderdrache erscheint | Er zählt als normale Chunk-Runde. Für den Gesamtsieg müsst ihr weiterhin den echten Enderdrachen im End besiegen. |

Nach eurem Sieg seht ihr die **aktive Spielzeit, besiegten Challenge-Mobs,
gestarteten Runden und Todesfälle**.

<a id="befehle"></a>

## ⌨️ Eure Befehle

Verwendet `/cc` oder den vollständigen Namen `/chunkchallenge`.
Die Befehle sind standardmäßig für Operatoren freigegeben.

| Befehl | Damit könnt ihr … |
| --- | --- |
| `/cc start` | einen gemeinsamen Run starten; muss im Spiel ausgeführt werden. |
| `/cc status` | Spielzeit, Statistiken, Anzeigeoptionen und die eigene Runde ansehen. |
| `/cc tags enable` · `/cc tags disable` | sichtbare Namen der Challenge-Mobs ein- oder ausschalten. |
| `/cc glowing enable` · `/cc glowing disable` | die Leuchtkontur der Challenge-Mobs ein- oder ausschalten. |
| `/cc bossbar enable` · `/cc bossbar disable` | die Lebenspunkteanzeigen der Challenge-Mobs ein- oder ausschalten. |
| `/cc reload` | eure geänderte Mobliste für zukünftige Runden laden. |
| `/cc stop` | den aktuellen Run **beenden und löschen**. |

Bei einem neuen Run sind **Nametags und Leuchtkonturen aus**, die **Bossbars
an**. Eure Auswahl gilt für den Run und wird gespeichert. Der Bossbar-Schalter
gilt auch für die Anzeigen eines Challenge-Withers oder Challenge-Enderdrachens.

<a id="berechtigungen"></a>

<details>
<summary>🔑 Berechtigungen für euren Spielleiter einrichten</summary>

Wenn ihr keine Operatorrechte vergeben möchtet, könnt ihr die Rechte über euer
Berechtigungsplugin einzeln freigeben.

| Permission | Erlaubt |
| --- | --- |
| `chunkchallenge.admin` | alle folgenden Befehle |
| `chunkchallenge.start` | Run starten |
| `chunkchallenge.stop` | Run beenden und löschen |
| `chunkchallenge.status` | Status ansehen |
| `chunkchallenge.reload` | Mobliste neu laden |
| `chunkchallenge.tags` | Nametags umschalten |
| `chunkchallenge.glowing` | Leuchtkonturen umschalten |
| `chunkchallenge.bossbar` | Bossbars umschalten |

</details>

## ⏸️ Heute aufhören, morgen weiterspielen

Beendet euren Server nach der Session mit **`stop` in der Serverkonsole**.
Beim nächsten Start und Login setzt ihr euren Run fort. Positionen, Gegner,
Lebenspunkte, Statistiken und Anzeigeoptionen bleiben erhalten; die Zeit
zwischen den Sessions zählt nicht mit.

> [!WARNING]
> **`stop` pausiert euren Run durch einen sauberen Serverstopp.**
> **`/cc stop` beendet und löscht euren Run.** Nutzt diesen Plugin-Befehl nur,
> wenn ihr die Challenge wirklich abbrechen möchtet.

## 🛠️ Euren Server vorbereiten und anpassen

<a id="mob-auswahl"></a>

<details>
<summary>🎲 Selbst festlegen, welche Mobs vorkommen</summary>

Beim ersten Pluginstart entsteht die Datei
`plugins/ChunkMobChallenge/mobs.yml`. Sie enthält die auf eurer Serverversion
verfügbaren, spawnbaren Mobs. Jeder Eintrag hat dieselbe Wahrscheinlichkeit –
auch Wither, Warden, Giant, Illusioner und Enderdrache.

Entfernt die Einträge der Mobs, die ihr nicht spielen möchtet, und führt danach
`/cc reload` aus. Bereits aktive oder pausierte Runden behalten ihren Gegner.

- Entfernte Einträge werden nicht automatisch wieder ergänzt.
- Auch nach einem Minecraft-Update werden neue Mobs nicht automatisch in eine
  bestehende Liste eingetragen.
- Ungültige und doppelte Einträge werden mit einer Konsolenwarnung ignoriert.
  Ist kein gültiger Mob übrig, bleibt der bisherige Pool aktiv.

**Die vollständige Liste wiederherstellen:** Stoppt den Server, löscht nur
`plugins/ChunkMobChallenge/mobs.yml` und startet ihn erneut. Die Datei wird
passend zu eurer installierten Minecraft-Version neu erzeugt.

</details>

<details>
<summary>☠️ Einen Hardcore-Run vorbereiten</summary>

Legt für Hardcore eine frische Welt an. Bereits **vor der ersten Erzeugung der
Welt** müssen in `server.properties` diese Werte stehen:

```properties
hardcore=true
difficulty=hard
```

Das nachträgliche Umschalten einer vorhandenen normalen Welt aktiviert Hardcore
nicht zuverlässig. Im Hardcore-Run beendet der Tod eines Teilnehmers die
Challenge für alle.

</details>

<details>
<summary>💾 Euren Run sichern oder ein Backup wiederherstellen</summary>

Sichert immer **Welt und Plugin-Daten gemeinsam**. Der Challenge-Zustand liegt
in `plugins/ChunkMobChallenge/state.yml`; die Gegner selbst werden zusätzlich
in den Weltdateien gespeichert.

| Backup erstellen | Backup wiederherstellen |
| --- | --- |
| 1. Server mit `stop` herunterfahren. | 1. Server vollständig stoppen. |
| 2. Alle zugehörigen Weltordner sichern. | 2. Weltordner aus dem Backup wiederherstellen. |
| 3. Den gesamten Ordner `plugins/ChunkMobChallenge` sichern. | 3. Den Pluginordner aus **demselben Backup** wiederherstellen. |
| | 4. Server starten, verbinden und `/cc status` prüfen. |

Eine Welt und eine `state.yml` aus unterschiedlichen Zeitpunkten können zu
fehlenden oder doppelt rekonstruierten Gegnern führen.

</details>

<details>
<summary>🖥️ Paper auf eurem eigenen Rechner starten</summary>

Prüft mit `java -version`, ob Java 25 verwendet wird. Startet den Server im
Ordner seiner Paper-JAR unter macOS, Linux oder Windows beispielsweise so:

```text
java -Xms2G -Xmx2G -jar paper.jar --nogui
```

Ersetzt `paper.jar` durch den Dateinamen eurer heruntergeladenen Paper-JAR.
Der erste Pluginstart erzeugt `plugins/ChunkMobChallenge/mobs.yml`. Sobald ihr
einen Run startet, kommt dessen gespeicherter Zustand in `state.yml` hinzu.

</details>

## ❓ Gut zu wissen

<details>
<summary>🤝 Können Freunde während eines laufenden Runs dazukommen?</summary>

Ja. Neue Spieler, die während eines laufenden Runs beitreten, werden in die
Challenge aufgenommen und nach Möglichkeit zu einem aktiven Teilnehmer
teleportiert. Bereits bekannte Teilnehmer setzen ihren gespeicherten Zustand
fort.

</details>

<details>
<summary>🦑 Was passiert mit Wasser-Mobs, Flugmobs und großen Gegnern?</summary>

- Wasser-Mobs können an Land erscheinen und dort natürlich sterben. Auch das
  zählt als Rundensieg.
- Challenge-Mobs despawnen nicht natürlich und bleiben in ihrem Chunk.
- Flugmobs werden an der Chunkgrenze umgelenkt.
- Große Gegner werden aus Blöcken und unzugänglichen Bereichen gerettet.
- Nether-Mobs werden bei Bedarf vom Bedrockdach zurück in den Spielbereich
  geholt, wenn die Runde darunter stattfindet.
- Verwandelt sich ein Gegner, etwa ein Zombie Villager in einen Villager,
  übernimmt die neue Form die laufende Runde.
- Slime- und Magma-Cube-Nachkommen verlieren nach dem Rundensieg ihre
  Challenge-Markierungen.
- Challenge-Enderdrachen sind auf halbe Größe verkleinert, bleiben über der
  Arena und können dort mit Drachenfeuerbällen und Atemwolken angreifen.
- Wither und Enderdrache verwenden nach Möglichkeit ihre normale Bossbar.
  Bei Bedarf erhält ein Challenge-Enderdrache eine Ersatzanzeige.

</details>

<a id="kompatibilitaet"></a>

<details>
<summary>🧩 Welche Minecraft-Versionen und Server werden unterstützt?</summary>

Ein einziges Plugin-JAR unterstützt **Paper 26.1.x, 26.2 und 26.3 mit Java 25**.
Neue Mobtypen erscheinen nur auf Versionen, die sie anbieten.

| Minecraft / Paper-Build | Automatische Prüfungen | Gameplay-Erfahrung |
| --- | --- | --- |
| **26.1.1** · Build 29, Paper-Alpha | ✅ bestanden | vollständiger Spieltest noch offen |
| **26.1.2** · Build 74 | ✅ bestanden | Solo, Persistenz, Hardcore und Koop getestet |
| **26.2** · Build 134 | ✅ bestanden | mehrfach in Streams gespielt; eigener kompletter Solo-Run auf Build 121 |
| **26.3** · Build 194 | ✅ bestanden | vollständiger Spieltest noch offen |

Die automatischen Prüfungen umfassen API-Build, Unit-Tests, Pluginstart,
Statusabfrage, Mobpool-Reload und sauberes Herunterfahren mit derselben
Plugin-JAR. Die genauen Ergebnisse stehen in [`TESTING.md`](TESTING.md).

Für 26.1/26.1.0 gibt es keinen separaten Paper-Download; die verfügbare
26.1-Reihe beginnt bei 26.1.1. Dessen letzter Paper-Build ist als Alpha
gekennzeichnet.

Folia, Spigot, Vanilla, Fabric, Forge und NeoForge werden als Serverplattform
nicht unterstützt. Client-Mods sind grundsätzlich möglich, solange sie das
normale Multiplayer-Verhalten nicht verändern.

</details>

## 🐛 Etwas funktioniert nicht?

Nutzt das [Formular für Fehlermeldungen](https://github.com/playmonkeei/mc-chunk-random-mob/issues/new/choose)
und beschreibt kurz, was passiert ist und wie es sich wiederholen lässt.
Hilfreich sind:

- eure Minecraft-, Paper-, Plugin- und Java-Version,
- die Ausgabe von `/cc status` und relevante Konsolenmeldungen,
- der betroffene Mob und Chunk,
- ein Screenshot bei Problemen mit Border, Nametags, Glowing oder Bossbar.

Prüft vor dem Teilen von Logs oder `state.yml`, ob darin Spieler-UUIDs oder
andere Informationen stehen, die ihr nicht veröffentlichen möchtet.

## 🧰 Für Entwickler

<details>
<summary>🔧 Plugin selbst bauen und lokale Testserver starten</summary>

Voraussetzung ist Java 25. Das Projekt verwendet Gradle mit Kotlin DSL und
baut die gemeinsame JAR gegen die älteste unterstützte Paper-API, 26.1.1.

```bash
./gradlew build
```

Die fertige JAR liegt unter `build/libs/chunk-mob-challenge-1.1.0.jar`.

**Lokale Testserver vorbereiten:**

```bash
./scripts/setup-test-servers.sh
```

Das Skript lädt alle vier gepinnten Paper-Versionen, prüft ihre SHA-256-Summen,
baut das Plugin und kopiert es in die Testserver. Startet anschließend jeweils
**eine** Version:

```bash
./scripts/start-test-server.sh 26.1.1
./scripts/start-test-server.sh 26.1.2
./scripts/start-test-server.sh 26.2
./scripts/start-test-server.sh 26.3
```

Alle manuellen Testserver verwenden `localhost:25565`. Die lokale
`server.properties` wird bei Bedarf aus `server.properties.example` angelegt.
Generierte Konfigurationen und Zugangsdaten bleiben lokal.

**Automatischer Servercheck ohne Minecraft-Client:**

```bash
./gradlew clean build
python3 scripts/smoke-test-server.py 26.3 build/libs/chunk-mob-challenge-1.1.0.jar
```

Zusätzlich benötigt ihr Python 3, `curl` und Zustimmung zu
[Mojangs EULA](https://aka.ms/MinecraftEULA). Der Check akzeptiert die EULA für
den Testserver und verwendet ausschließlich wegwerfbare Welten unter
`build/smoke-servers/`.

GitHub Actions prüft jede Ziel-API und startet pro Version einen frischen
Server mit der gegen 26.1.1 gebauten Release-JAR. Dieselben Prüfungen laufen
vor Releases. Sie ersetzen keinen vollständigen Gameplay-Test.

| Weiterführend | Inhalt |
| --- | --- |
| [`TESTING.md`](TESTING.md) | manuelle Prüfschritte und bisherige Ergebnisse |
| [`paper-versions.tsv`](test-servers/paper-versions.tsv) | gepinnte Builds und SHA-256-Prüfsummen |
| [Paper Downloads-API](https://fill.papermc.io/v3/projects/paper) | offizielle Versionsdaten |
| [Release Notes](docs/release-notes/) | Änderungen pro Pluginversion |

</details>

---

<div align="center">

**Viel Erfolg – und hoffentlich wartet im nächsten Chunk keine Wither-Runde.** ⚔️

</div>
