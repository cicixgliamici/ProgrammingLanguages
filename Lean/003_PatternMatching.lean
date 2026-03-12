/-
003_PatternMatching.lean

Goal:
- understand match
- see pattern matching on Nat and Bool
- introduce custom inductive types
-/

-- Returns true if n is zero
def isZero (n : Nat) : Bool :=
  match n with
  | 0 => true
  | _ => false

#eval isZero 0
#eval isZero 5

-- Safe predecessor: pred 0 = 0
def safePred (n : Nat) : Nat :=
  match n with
  | 0 => 0
  | m + 1 => m

#eval safePred 0
#eval safePred 9

-- A custom inductive type
inductive Color where
  | red
  | green
  | blue
deriving Repr, DecidableEq

-- A function on an inductive type
def colorCode (c : Color) : Nat :=
  match c with
  | Color.red => 1
  | Color.green => 2
  | Color.blue => 3

#eval colorCode Color.red
#eval colorCode Color.blue

-- Another example: boolean negation written by hand
def myNot (b : Bool) : Bool :=
  match b with
  | true => false
  | false => true

#eval myNot true
#eval myNot false

/-
Exercises:
1. Define a function isGreen : Color → Bool
2. Define a function natToBool : Nat → Bool that is false only on 0
3. Define a type Day with seven constructors
-/
