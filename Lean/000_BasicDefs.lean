/-
000_BasicDefs.lean

Goals:
- understand `def`
- understand types, parameters, and return values
- understand `#check` and `#eval`
- see simple functions on Nat and Bool
- solve a few introductory exercises
-/

/-
`def` introduces a new named definition.

General form:

  def name (parameters) : ReturnType :=
    body

Lean elaborates the body, checks that it has the declared type,
and stores the definition in the current environment.

Executable definitions can later be compiled into code when the
project is built or when an evaluation command needs to run them.
-/

-- A constant is a definition without parameters.
def myNumber : Nat := 7

-- This definition represents a function Nat → Nat.
def addOne (n : Nat) : Nat :=
  n + 1

-- Multiple parameters are written one after another.
-- Lean interprets this as Nat → Nat → Nat.
def add (a : Nat) (b : Nat) : Nat :=
  a + b

-- A function can also return a Boolean value.
def negateBool (b : Bool) : Bool :=
  not b

-- A function can be defined explicitly using an anonymous function.
-- `fun n => n * 2` means: take `n` and return `n * 2`.
def double : Nat → Nat :=
  fun n => n * 2

/-
`#check expression` asks Lean to elaborate and type-check an expression.

It prints the type inferred by Lean, but it does not normally execute
the function.

`#check` is a command for inspecting code: it does not create a new
definition and is not included in the final executable program.
-/

#check myNumber
-- myNumber : Nat

#check addOne
-- addOne : Nat → Nat

#check add
-- add : Nat → Nat → Nat

#check negateBool
-- negateBool : Bool → Bool

#check double
-- double : Nat → Nat

/-
`#eval expression` asks Lean to execute an expression and print its result.

Before evaluation, Lean:
1. elaborates the expression;
2. checks its type;
3. generates executable code for the required definitions;
4. runs that code and displays the result.

`#eval` is useful for testing executable definitions, but it does not
prove a theorem and does not create a new declaration.
-/

#eval myNumber
-- 7

#eval addOne 5
-- 6

#eval add 3 4
-- 7

#eval negateBool true
-- false

#eval double 6
-- 12

/-
Exercises
-/

/-
1. Define a function `triple : Nat → Nat`.

This version uses the same explicit anonymous-function syntax
used by `double`.
-/
def triple : Nat → Nat :=
  fun n => n * 3

/-
2. Define a function `isFive : Nat → Bool`.

`==` performs a decidable equality test and returns a `Bool`.
It is different from `=`, which represents a logical proposition.
-/
def isFive (n : Nat) : Bool :=
  n == 5

/-
3. Define a function `max2 (a b : Nat) : Nat`.

The condition `a ≤ b` is a proposition. Lean can decide it inside
an `if`, returning `b` when it is true and `a` otherwise.
-/
def max2 (a b : Nat) : Nat :=
  if a ≤ b then
    b
  else
    a

-- Inspect the types of the exercise solutions.

#check triple
-- triple : Nat → Nat

#check isFive
-- isFive : Nat → Bool

#check max2
-- max2 : Nat → Nat → Nat

-- Test the exercise solutions.

#eval triple 4
-- 12

#eval isFive 5
-- true

#eval isFive 8
-- false

#eval max2 3 7
-- 7

#eval max2 10 4
-- 10

#eval max2 5 5
-- 5
