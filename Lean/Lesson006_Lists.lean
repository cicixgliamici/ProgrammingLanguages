/-!
Lesson006_Lists.lean

Goals:
- understand `List`, `[]`, and `::`;
- define polymorphic recursive functions;
- prove a property by induction on a list.
-/

def numbers : List Nat := [1, 2, 3, 4]

#eval numbers.length
#eval numbers.reverse

-- A list is either empty or a head followed by a tail.
def sumList : List Nat → Nat
  | [] => 0
  | x :: xs => x + sumList xs

/- The implicit type variable `{α}` makes this function work for lists of any
   element type. The element itself is ignored, hence the `_` pattern. -/
def myLength {α : Type} : List α → Nat
  | [] => 0
  | _ :: xs => 1 + myLength xs

-- `snoc` places an element at the right end, unlike `::`, which adds on the left.
def snoc {α : Type} : List α → α → List α
  | [], y => [y]
  | x :: xs, y => x :: snoc xs y

-- The result list may have a different element type, represented by `β`.
def myMap {α β : Type} (f : α → β) : List α → List β
  | [] => []
  | x :: xs => f x :: myMap f xs

#eval sumList [1, 2, 3, 4]
#eval myLength [10, 20, 30]
#eval snoc [1, 2, 3] 4
#eval myMap (fun x => x + 1) [1, 2, 3]

/-
Solved exercises

Exercise 1: define `myAppend : List α → List α → List α`.
Exercise 2: define `containsZero : List Nat → Bool`.
Exercise 3: prove that `sumList [] = 0`.
Exercise 4: prove that `myLength (snoc xs x) = myLength xs + 1`.
-/

-- Recursing on the first list preserves its order before the second list.
def myAppend {α : Type} : List α → List α → List α
  | [], ys => ys
  | x :: xs, ys => x :: myAppend xs ys

-- The Boolean disjunction stops with `true` as soon as a zero is found.
def containsZero : List Nat → Bool
  | [] => false
  | x :: xs => x == 0 || containsZero xs

example : sumList [] = 0 := by
  rfl

/- The induction hypothesis describes the shorter tail. After unfolding `snoc`
   and `myLength`, `simp` rewrites the tail with that hypothesis. -/
theorem myLength_snoc {α : Type} (xs : List α) (x : α) :
    myLength (snoc xs x) = myLength xs + 1 := by
  induction xs with
  | nil => rfl
  | cons y ys ih => simp [snoc, myLength, ih, Nat.add_assoc]

#eval myAppend [1, 2] [3, 4]
#eval containsZero [3, 0, 5]

/- Study notes:
- Pattern matching guarantees that every list shape is handled.
- Recursive calls must use a structurally smaller list.
- Induction on a list has `nil` and `cons` cases, mirroring its constructors.
-/
