package dev.learning.scalaexamples

/*
 * This file demonstrates basic functional programming concepts in Scala.
 * 
 * Key Concepts:
 * - Immutability
 * - Higher-Order Functions
 * - Pattern Matching
 * - Collections and their methods
 * - Option type for null safety
 */

@main def functionalBasics(): Unit =
  // 1. Immutability and val vs var
  val immutable = "I cannot be changed"
  // immutable = "This would cause an error"  // Uncomment to see the error
  
  var mutable = "I can be changed"
  mutable = "Now I'm different"
  
  // 2. Functions as first-class citizens
  val numbers = List(1, 2, 3, 4, 5)
  
  // Map: transforms each element
  val doubled = numbers.map(x => x * 2)
  println(s"Doubled numbers: $doubled")
  
  // Filter: keeps only elements that match a condition
  val evenNumbers = numbers.filter(x => x % 2 == 0)
  println(s"Even numbers: $evenNumbers")
  
  // Reduce: combines all elements into a single result
  val sum = numbers.reduce((a, b) => a + b)
  println(s"Sum of numbers: $sum")
  
  // 3. Pattern Matching
  def describeNumber(n: Int): String = n match
    case 0 => "Zero"
    case n if n < 0 => "Negative"
    case n if n % 2 == 0 => "Even"
    case _ => "Odd"
  
  println(s"5 is ${describeNumber(5)}")
  println(s"4 is ${describeNumber(4)}")
  println(s"-1 is ${describeNumber(-1)}")
  
  // 4. Option type for null safety
  val maybeName: Option[String] = Some("Scala")
  val noName: Option[String] = None
  
  // Safe way to handle potentially missing values
  println(maybeName.getOrElse("No name provided"))
  println(noName.getOrElse("No name provided"))
  
  // 5. List operations
  val fruits = List("apple", "banana", "orange")
  
  // For comprehension (similar to for-each but more powerful)
  val upperFruits = for
    fruit <- fruits
    if fruit.length > 5
  yield fruit.toUpperCase()
  
  println(s"Long fruits in uppercase: $upperFruits")
  
  // 6. Function composition
  val addOne = (x: Int) => x + 1
  val multiplyByTwo = (x: Int) => x * 2
  
  // Compose functions
  val addOneThenMultiplyByTwo = addOne.andThen(multiplyByTwo)
  println(s"5 + 1 * 2 = ${addOneThenMultiplyByTwo(5)}")
  
  // 7. Partial functions
  val divide: PartialFunction[Int, Int] =
    case x if x != 0 => 10 / x
  
  println(s"10 / 2 = ${divide(2)}")
  println(s"Can divide by 0? ${divide.isDefinedAt(0)}") 
