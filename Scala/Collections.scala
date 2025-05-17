/*
 * This file demonstrates Scala collections and their operations.
 * 
 * Key Concepts:
 * - Lists, Sets, Maps
 * - Immutable vs Mutable collections
 * - Common collection operations
 * - For comprehensions
 * - Collection methods (map, filter, fold, etc.)
 */

@main def collections(): Unit =
  // 1. Lists (immutable by default)
  val numbers = List(1, 2, 3, 4, 5)
  println(s"Original list: $numbers")
  
  // Common list operations
  println(s"Head: ${numbers.head}")
  println(s"Tail: ${numbers.tail}")
  println(s"Last: ${numbers.last}")
  println(s"Init: ${numbers.init}")
  println(s"Length: ${numbers.length}")
  
  // List concatenation
  val moreNumbers = List(6, 7, 8)
  val combined = numbers ::: moreNumbers
  println(s"Combined lists: $combined")
  
  // 2. Sets (unique elements)
  val fruits = Set("apple", "banana", "orange", "apple")  // apple appears only once
  println(s"Fruits set: $fruits")
  
  // Set operations
  val moreFruits = Set("orange", "grape", "kiwi")
  println(s"Union: ${fruits union moreFruits}")
  println(s"Intersection: ${fruits intersect moreFruits}")
  println(s"Difference: ${fruits diff moreFruits}")
  
  // 3. Maps (key-value pairs)
  val ages = Map(
    "Alice" -> 30,
    "Bob" -> 25,
    "Charlie" -> 35
  )
  
  println(s"Ages: $ages")
  println(s"Alice's age: ${ages("Alice")}")
  println(s"Safe access: ${ages.get("David")}")  // Returns Option
  
  // Map operations
  val updatedAges = ages + ("David" -> 40)
  println(s"Updated ages: $updatedAges")
  
  // 4. Collection methods
  val numbers2 = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  
  // map: transform each element
  val doubled = numbers2.map(_ * 2)
  println(s"Doubled: $doubled")
  
  // filter: keep only elements that match a condition
  val evenNumbers = numbers2.filter(_ % 2 == 0)
  println(s"Even numbers: $evenNumbers")
  
  // fold: combine all elements into a single result
  val sum = numbers2.foldLeft(0)(_ + _)
  println(s"Sum: $sum")
  
  // 5. For comprehensions
  val result = for
    n <- numbers2
    if n % 2 == 0
    if n > 5
  yield n * n
  
  println(s"Squares of even numbers > 5: $result")
  
  // 6. Mutable collections
  import scala.collection.mutable
  
  val mutableList = mutable.ListBuffer(1, 2, 3)
  mutableList += 4  // Add element
  mutableList -= 1  // Remove element
  println(s"Mutable list: $mutableList")
  
  val mutableSet = mutable.Set("a", "b", "c")
  mutableSet += "d"  // Add element
  mutableSet -= "a"  // Remove element
  println(s"Mutable set: $mutableSet")
  
  val mutableMap = mutable.Map("x" -> 1, "y" -> 2)
  mutableMap += "z" -> 3  // Add element
  mutableMap -= "x"       // Remove element
  println(s"Mutable map: $mutableMap")
  
  // 7. Collection views (lazy evaluation)
  val view = numbers2.view
    .map(_ * 2)
    .filter(_ > 10)
    .take(3)
  
  println(s"View result: ${view.toList}")  // Computation happens here
  
  // 8. Grouping and partitioning
  val grouped = numbers2.groupBy(_ % 2 == 0)
  println(s"Grouped by even/odd: $grouped")
  
  val (evens, odds) = numbers2.partition(_ % 2 == 0)
  println(s"Evens: $evens")
  println(s"Odds: $odds") 