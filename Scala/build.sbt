ThisBuild / scalaVersion := "3.3.5"
ThisBuild / organization := "dev.learning"
ThisBuild / version := "1.0.0-SNAPSHOT"

lazy val root = project
  .in(file("."))
  .settings(
    name := "scala-language-examples",
    Compile / scalacOptions ++= Seq("-deprecation", "-feature", "-unchecked"),
    libraryDependencies += "org.scalameta" %% "munit" % "1.0.3" % Test,
    testFrameworks += new TestFramework("munit.Framework")
  )
