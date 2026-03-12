/-
000_BasicDefs.lean

Goal:
- understand def
- understand types, parameters, and return values
- see simple functions on Nat and Bool
-/

-- A very simple definition: a constant
def myNumber : Nat := 7

-- A function that takes a natural number and returns the next one
def addOne (n : Nat) : Nat :=
  n + 1

-- A function with two parameters
def add (a : Nat) (b : Nat) : Nat :=
  a + b

-- A boolean function
def negateBool (b : Bool) : Bool :=
  not b

-- An anonymous function assigned to a name
def double : Nat → Nat :=
  fun n => n * 2

-- Examples to let Lean inspect
#check myNumber
#check addOne
#check add
#check negateBool
#check double

-- Evaluations
#eval myNumber
#eval addOne 5
#eval add 3 4
#eval negateBool true
#eval double 6

/-
Suggested exercises:
1. Define a function triple : Nat → Nat
2. Define a function isFive : Nat → Bool
3. Define a function max2 (a b : Nat) : Nat
-/
