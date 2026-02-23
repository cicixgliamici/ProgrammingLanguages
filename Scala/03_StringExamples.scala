/*
 * This file demonstrates string manipulation in Scala and highlights key differences from Java.
 * 
 * Key Differences from Java:
 * 1. String Interpolation: Scala provides powerful string interpolation with s"", f"", and raw"" prefixes
 * 2. String Methods: Scala adds many convenient methods to String class
 * 3. Pattern Matching: Scala's pattern matching works great with strings
 * 4. Immutability: Like Java, strings are immutable, but Scala provides more functional ways to work with them
 */

@main def stringExamples(): Unit =
  // Basic string creation and interpolation
  val name = "Scala"
  val version = 3.0
  
  // String interpolation with s""
  println(s"Welcome to $name $version")  // Similar to Java's String.format but more concise
  
  // Multi-line strings with triple quotes
  val multiLine = """
    |This is a multi-line
    |string in Scala.
    |The | at the start of each line
    |is removed by stripMargin
    """.stripMargin
  
  println(multiLine)
  
  // String methods that are more convenient than Java
  val text = "  Hello, Scala!  "
  
  println(s"Original: '$text'")
  println(s"Trimmed: '${text.trim}'")
  println(s"Reversed: '${text.reverse}'")
  println(s"Capitalized: '${text.capitalize}'")
  
  // Pattern matching with strings
  val message = "Hello"
  
  message match
    case "Hello" => println("Greeting found!")
    case "Goodbye" => println("Farewell found!")
    case _ => println("Other message")
  
  // String operations with collections
  val words = "Scala is awesome".split(" ")
  println(s"Words: ${words.mkString(", ")}")
  
  // String formatting with f""
  val pi = 3.14159
  println(f"Pi to 2 decimal places: $pi%.2f")
  
  // String comparison (similar to Java but more idiomatic)
  val str1 = "Scala"
  val str2 = "scala"
  println(s"Case-sensitive comparison: ${str1 == str2}")
  println(s"Case-insensitive comparison: ${str1.equalsIgnoreCase(str2)}")
  
  // String concatenation (multiple ways)
  val part1 = "Hello"
  val part2 = "World"
  println(part1 + " " + part2)  // Java style
  println(s"$part1 $part2")     // Scala style
  println(part1.concat(" ").concat(part2))  // Method chaining 