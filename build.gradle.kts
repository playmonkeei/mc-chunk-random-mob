plugins {
    java
}

group = "dev.playmonkeei"
version = "1.1.0"

// Compile the shipped JAR against the oldest supported Paper API.
val paperApiVersion = providers.gradleProperty("paperApiVersion")
    .orElse("26.1.1.build.29-alpha")

repositories {
    mavenCentral()
    maven("https://repo.papermc.io/repository/maven-public/")
}

dependencies {
    compileOnly("io.papermc.paper:paper-api:${paperApiVersion.get()}")

    testImplementation(platform("org.junit:junit-bom:6.0.0"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
}

java {
    toolchain.languageVersion.set(JavaLanguageVersion.of(25))
}

tasks.withType<JavaCompile>().configureEach {
    options.encoding = "UTF-8"
    options.release.set(25)
}

tasks.test {
    useJUnitPlatform()
}

tasks.processResources {
    inputs.property("version", project.version)
    filesMatching("plugin.yml") {
        expand("version" to project.version)
    }
}

tasks.register("printPluginJar") {
    doLast {
        println(tasks.jar.get().archiveFile.get().asFile.absolutePath)
    }
}
