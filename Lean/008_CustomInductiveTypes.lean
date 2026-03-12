/-
008_CustomInductiveTypes.lean

Goal:
- define your own inductive types
- write functions by pattern matching
- reason by cases
-/

-- A custom type for weekdays
inductive Day where
  | monday
  | tuesday
  | wednesday
  | thursday
  | friday
  | saturday
  | sunday
deriving Repr, DecidableEq

-- Return true if the day is a weekend day
def isWeekend : Day → Bool
  | Day.saturday => true
  | Day.sunday => true
  | _ => false

#eval isWeekend Day.monday
#eval isWeekend Day.sunday

-- Return the next day
def nextDay : Day → Day
  | Day.monday => Day.tuesday
  | Day.tuesday => Day.wednesday
  | Day.wednesday => Day.thursday
  | Day.thursday => Day.friday
  | Day.friday => Day.saturday
  | Day.saturday => Day.sunday
  | Day.sunday => Day.monday

#eval nextDay Day.friday
#eval nextDay Day.sunday

-- A custom option-like type
inductive MyOption (α : Type) where
  | none : MyOption α
  | some : α → MyOption α
deriving Repr

-- Extract a value with a default
def getOrElse (default : α) : MyOption α → α
  | MyOption.none => default
  | MyOption.some x => x

#eval getOrElse 0 (MyOption.some 10)
#eval getOrElse 0 (MyOption.none)

-- A custom binary tree
inductive MyTree (α : Type) where
  | leaf : α → MyTree α
  | node : MyTree α → MyTree α → MyTree α
deriving Repr

-- Count the number of leaves
def countLeaves : MyTree α → Nat
  | MyTree.leaf _ => 1
  | MyTree.node l r => countLeaves l + countLeaves r

def exampleTree : MyTree Nat :=
  MyTree.node
    (MyTree.leaf 1)
    (MyTree.node (MyTree.leaf 2) (MyTree.leaf 3))

#eval countLeaves exampleTree

-- Simple proof by cases
example (d : Day) : isWeekend d = true ∨ isWeekend d = false := by
  cases d <;> simp [isWeekend]

/-
Exercises:
1. Define a function previousDay : Day → Day
2. Define mapTree : (α → β) → MyTree α → MyTree β
3. Define treeSize : MyTree α → Nat
4. Prove by cases that nextDay d is always a valid Day
-/
