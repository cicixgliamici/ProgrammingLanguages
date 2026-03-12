/-
Lists.lean

Goal:
- understand Lean lists
- define recursive functions on lists
- prove simple properties
-/

-- A list of natural numbers
def numbers : List Nat := [1, 2, 3, 4]

#eval numbers.length
#eval numbers.reverse

-- Compute the sum of a list of natural numbers
def sumList : List Nat → Nat
  | [] => 0
  | x :: xs => x + sumList xs

#eval sumList []
#eval sumList [1, 2, 3, 4]

-- Compute the length of a list manually
def myLength : List α → Nat
  | [] => 0
  | _ :: xs => 1 + myLength xs

#eval myLength [10, 20, 30]
#eval myLength ["a", "b"]

-- Append an element at the end of a list
def snoc : List α → α → List α
  | [], y => [y]
  | x :: xs, y => x :: snoc xs y

#eval snoc [1, 2, 3] 4

-- Map a function over a list
def myMap (f : α → β) : List α → List β
  | [] => []
  | x :: xs => f x :: myMap f xs

#eval myMap (fun x => x + 1) [1, 2, 3]
#eval myMap String.length ["lean", "is", "fun"]

-- Prove that the length of the empty list is 0
example : myLength ([] : List Nat) = 0 := rfl

-- Prove that sumList [x] = x
example (x : Nat) : sumList [x] = x := by
  rfl

-- Prove that myLength agrees with one-step expansion
example (x : α) (xs : List α) : myLength (x :: xs) = 1 + myLength xs := by
  rfl

/-
Exercises:
1. Define myAppend : List α → List α → List α
2. Define containsZero : List Nat → Bool
3. Prove: sumList [] = 0
4. Prove: myLength (snoc xs x) = myLength xs + 1
-/
