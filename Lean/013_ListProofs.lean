/-
013_ListProofs.lean

Goals:
- prove algebraic laws for recursive list functions;
- identify and prove helper lemmas;
- follow the same structure in definitions and induction proofs.
-/

def myAppend {α : Type} : List α → List α → List α
  | [], ys => ys
  | x :: xs, ys => x :: myAppend xs ys

def myLength {α : Type} : List α → Nat
  | [] => 0
  | _ :: xs => 1 + myLength xs

def myReverse {α : Type} : List α → List α
  | [] => []
  | x :: xs => myAppend (myReverse xs) [x]

def myMap {α β : Type} (f : α → β) : List α → List β
  | [] => []
  | x :: xs => f x :: myMap f xs

theorem myAppend_nil (xs : List α) : myAppend xs [] = xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simp [myAppend, ih]

theorem myAppend_assoc (xs ys zs : List α) :
    myAppend (myAppend xs ys) zs = myAppend xs (myAppend ys zs) := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simp [myAppend, ih]

theorem myLength_append (xs ys : List α) :
    myLength (myAppend xs ys) = myLength xs + myLength ys := by
  induction xs with
  | nil => simp [myAppend, myLength]
  | cons x xs ih => simp [myAppend, myLength, ih, Nat.add_assoc]

/- Reverse needs a helper lemma because its recursive branch appends a singleton.
   Proving the intermediate shape explicitly keeps the final proof short. -/
theorem myReverse_append_singleton (xs : List α) (x : α) :
    myReverse (myAppend xs [x]) = x :: myReverse xs := by
  induction xs with
  | nil => rfl
  | cons y ys ih => simp [myAppend, myReverse, ih]

theorem myLength_reverse (xs : List α) :
    myLength (myReverse xs) = myLength xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
      simp [myReverse, myLength_append, myLength, ih, Nat.add_comm]

theorem myReverse_reverse (xs : List α) : myReverse (myReverse xs) = xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simp [myReverse, myReverse_append_singleton, ih]

/-
Solved exercises

Exercise 1: prove associativity of `myAppend`.
Exercise 2: define `myMap` and prove that mapping the identity leaves a list unchanged.
Exercise 3: prove `myLength (x :: xs) = 1 + myLength xs`.
Exercise 4: prove `myReverse [] = []`.
Exercise 5: prove `myReverse [x] = [x]`.
-/

-- Induction follows `myMap`: the head is unchanged and `ih` handles the tail.
theorem myMap_identity (xs : List α) : myMap (fun x => x) xs = xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simp [myMap, ih]

example (x : α) (xs : List α) : myLength (x :: xs) = 1 + myLength xs := by
  rfl

example : myReverse ([] : List α) = [] := by
  rfl

example (x : α) : myReverse [x] = [x] := by
  rfl

/- Study notes:
- Induct on the argument inspected by the recursive function.
- A good helper lemma describes the exact intermediate expression blocking `simp`.
- Named theorems can be supplied to `simp` explicitly without making them global rules.
-/
