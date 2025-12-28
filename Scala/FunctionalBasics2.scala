/*
 * This file provides a guided, commented introduction to functional programming basics in Scala.
 *
 * Topics covered:
 * - val vs var (immutability)
 * - tail recursion (@tailrec)
 * - higher-order functions (HOF)
 */

import scala.annotation.tailrec

/**
 * A small class that groups functional programming examples.
 *
 * Each method returns values instead of printing directly, keeping the code
 * focused on pure computations and referential transparency when possible.
 */
class FunctionalProgrammingBasics {

  /**
   * Demonstrates the difference between val (immutable) and var (mutable).
   *
   * Returns a tuple describing:
   * - the original val
   * - the original var
   * - the updated var
   */
  def valVsVarDemo(): (String, String, String) = {
    val immutable = "I cannot be reassigned"
    var mutable = "I can be reassigned"
    val before = mutable

    // Reassigning a var is allowed
    mutable = "Now I have a new value"

    (immutable, before, mutable)
  }

  /**
   * Tail-recursive factorial implementation.
   *
   * Tail recursion is a recursive call that is the last action in a function.
   * The Scala compiler can optimize it into a loop to avoid stack overflows.
   *
   * Parameters:
   * - n: non-negative integer to compute factorial of
   *
   * Returns:
   * - n! (factorial of n)
   */
  def factorial(n: Int): BigInt = {
    @tailrec
    def loop(remaining: Int, acc: BigInt): BigInt = {
      if (remaining <= 1) acc
      else loop(remaining - 1, acc * remaining)
    }

    loop(n, BigInt(1))
  }

  /**
   * Applies a higher-order function to a list.
   *
   * A higher-order function (HOF) is a function that takes another function
   * as a parameter or returns a function.
   *
   * Parameters:
   * - numbers: list of integers
   * - transform: function applied to each element
   *
   * Returns:
   * - a new list after applying the transform function
   */
  def applyTransform(numbers: List[Int], transform: Int => Int): List[Int] = {
    numbers.map(transform)
  }
}

/**
 * Small runnable demo that prints the outputs of each example.
 */
@main def functionalProgrammingBasicsDemo(): Unit = {
  val basics = new FunctionalProgrammingBasics

  val (immutable, before, after) = basics.valVsVarDemo()
  println(s"val example: $immutable")
  println(s"var before reassignment: $before")
  println(s"var after reassignment: $after")

  val number = 5
  println(s"factorial($number) = ${basics.factorial(number)}")

  val numbers = List(1, 2, 3, 4, 5)
  val doubled = basics.applyTransform(numbers, n => n * 2)
  println(s"Doubled numbers: $doubled")
}
