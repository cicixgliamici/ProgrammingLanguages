/-
013_ListProofs.lean

Goal:
- prove basic properties of recursive list functions
- practice induction on lists
-/

-- Reintroduce the functions locally for a self-contained file

def myAppend : List α → List α → List α
  | [], ys => ys
  | x :: xs, ys => x :: myAppend xs ys

def myLength : List α → Nat
  | [] => 0
  | _ :: xs => 1 + myLength xs

def myReverse : List α → List α
  | [] => []
  | x :: xs => myAppend (myReverse xs) [x]

-- Appending [] on the right changes nothing
theorem myAppend_nil (xs : List α) : myAppend xs [] = xs := by
  induction xs with
  | nil =>
      rfl
  | cons x xs ih =>
      simp [myAppend, ih]

-- Length of append
theorem myLength_append (xs ys : List α) :
    myLength (myAppend xs ys) = myLength xs + myLength ys := by
  induction xs with
  | nil =>
      simp [myAppend, myLength]
  | cons x xs ih =>
      simp [myAppend, myLength, ih]

-- A helper lemma for reverse
theorem myReverse_append_singleton (xs : List α) (x : α) :
    myReverse (myAppend xs [x]) = x :: myReverse xs := by
  induction xs with
  | nil =>
      simp [myAppend, myReverse]
  | cons y ys ih =>
      simp [myAppend, myReverse, ih]

-- Length is preserved by reverse
theorem myLength_reverse (xs : List α) :
    myLength (myReverse xs) = myLength xs := by
  induction xs with
  | nil =>
      rfl
  | cons x xs ih =>
      simp [myReverse, myLength_append, myLength, ih]

-- Double reverse gives back the original list
theorem myReverse_reverse (xs : List α) :
    myReverse (myReverse xs) = xs := by
  induction xs with
  | nil =>
      rfl
  | cons x xs ih =>
      simp [myReverse, myReverse_append_singleton, ih]

/-
Exercises:
1. Prove: myAppend (myAppend xs ys) zs = myAppend xs (myAppend ys zs)
2. Define myMap and prove: myMap id xs = xs
3. Prove: myLength (x :: xs) = 1 + myLength xs
4. Prove: myReverse [] = []
5. Prove: myReverse [x] = [x]
-/
