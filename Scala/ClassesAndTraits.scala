/*
 * This file demonstrates object-oriented programming concepts in Scala.
 * 
 * Key Concepts:
 * - Classes and Objects
 * - Case Classes
 * - Traits (similar to interfaces but more powerful)
 * - Companion Objects
 * - Inheritance
 */

// Basic class definition
class Person(val name: String, var age: Int):
  def greet(): String = s"Hello, my name is $name and I am $age years old"
  
  // Method with default parameter
  def haveBirthday(years: Int = 1): Unit =
    age += years

// Case class (automatically generates useful methods)
case class Point(x: Int, y: Int):
  def distance(other: Point): Double =
    val dx = x - other.x
    val dy = y - other.y
    Math.sqrt(dx * dx + dy * dy)

// Trait (similar to interface but can have concrete methods)
trait Animal:
  def name: String
  def makeSound(): String
  def isMammal: Boolean = true  // Default implementation

// Class implementing a trait
class Dog(val name: String) extends Animal:
  def makeSound(): String = "Woof!"
  override def isMammal: Boolean = true

class Bird(val name: String) extends Animal:
  def makeSound(): String = "Tweet!"
  override def isMammal: Boolean = false

// Companion object (similar to static methods in Java)
object Person:
  def apply(name: String, age: Int): Person = new Person(name, age)
  def unapply(p: Person): Option[(String, Int)] = Some((p.name, p.age))

@main def classesAndTraits(): Unit =
  // Using regular class
  val person = new Person("Alice", 30)
  println(person.greet())
  person.haveBirthday()
  println(s"After birthday: ${person.greet()}")
  
  // Using case class
  val p1 = Point(0, 0)
  val p2 = Point(3, 4)
  println(s"Distance between points: ${p1.distance(p2)}")
  
  // Case class automatically implements equals and toString
  val p3 = Point(0, 0)
  println(s"p1 == p3: ${p1 == p3}")  // true
  println(s"p1: $p1")  // Nice string representation
  
  // Using traits
  val dog = new Dog("Rex")
  val bird = new Bird("Tweety")
  
  println(s"${dog.name} says ${dog.makeSound()}")
  println(s"${bird.name} says ${bird.makeSound()}")
  println(s"Is ${dog.name} a mammal? ${dog.isMammal}")
  println(s"Is ${bird.name} a mammal? ${bird.isMammal}")
  
  // Using companion object
  val person2 = Person("Bob", 25)  // Using apply
  println(person2.greet())
  
  // Pattern matching with case class
  person2 match
    case Person(name, age) => println(s"Matched: $name, $age")
  
  // Pattern matching with trait
  def describeAnimal(animal: Animal): String = animal match
    case d: Dog => s"${d.name} is a dog that says ${d.makeSound()}"
    case b: Bird => s"${b.name} is a bird that says ${b.makeSound()}"
    case _ => "Unknown animal"
  
  println(describeAnimal(dog))
  println(describeAnimal(bird)) 