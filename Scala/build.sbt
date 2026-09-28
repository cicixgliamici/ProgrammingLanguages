ThisBuild / scalaVersion := "3.3.5"
ThisBuild / organization := "dev.learning"
ThisBuild / version := "1.0.0-SNAPSHOT"

lazy val root = project
  .in(file("."))
  .settings(
    name := "scala-language-examples",
    // Lessons intentionally remain in this flat directory for reading in order.
    Compile / unmanagedSourceDirectories := Seq(baseDirectory.value),
    Compile / scalacOptions ++= Seq("-deprecation", "-feature", "-unchecked")
  )
