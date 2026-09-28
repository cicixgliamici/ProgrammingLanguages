package dev.learning.scalaexamples

class FunctionalProgrammingBasicsSuite extends munit.FunSuite:
  private val basics = new FunctionalProgrammingBasics

  test("factorial handles zero and positive inputs"):
    assertEquals(basics.factorial(0), BigInt(1))
    assertEquals(basics.factorial(1), BigInt(1))
    assertEquals(basics.factorial(5), BigInt(120))

  test("applyTransform preserves order while transforming every value"):
    val result = basics.applyTransform(List(1, 2, 3), _ * 3)
    assertEquals(result, List(3, 6, 9))

  test("valVsVarDemo exposes the value before and after reassignment"):
    val (immutable, before, after) = basics.valVsVarDemo()
    assertEquals(immutable, "I cannot be reassigned")
    assertEquals(before, "I can be reassigned")
    assertEquals(after, "Now I have a new value")
