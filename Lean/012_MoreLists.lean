/-
012_MoreLists.lean

Goals:
- implement common list combinators by structural recursion;
- recognize how parameters evolve in recursive calls;
- prepare reusable definitions for later proofs.
-/

def myAppend {α : Type} : List α → List α → List α
  | [], ys => ys
  | x :: xs, ys => x :: myAppend xs ys

-- This direct definition is clear but repeatedly traverses intermediate lists.
def myReverse {α : Type} : List α → List α
  | [] => []
  | x :: xs => myAppend (myReverse xs) [x]

def myFilter {α : Type} (predicate : α → Bool) : List α → List α
  | [] => []
  | x :: xs =>
      if predicate x then x :: myFilter predicate xs
      else myFilter predicate xs

def myTake {α : Type} : Nat → List α → List α
  | 0, _ => []
  | _ + 1, [] => []
  | n + 1, x :: xs => x :: myTake n xs

def myDrop {α : Type} : Nat → List α → List α
  | 0, xs => xs
  | _ + 1, [] => []
  | n + 1, _ :: xs => myDrop n xs

-- Zipping stops as soon as either input is exhausted.
def myZip {α β : Type} : List α → List β → List (α × β)
  | [], _ => []
  | _, [] => []
  | x :: xs, y :: ys => (x, y) :: myZip xs ys

/- A left fold carries `accumulator` through the traversal. Tail recursion makes
   it suitable for iterative computations such as sums. -/
def myFoldl {α β : Type} (combine : β → α → β) : β → List α → β
  | accumulator, [] => accumulator
  | accumulator, x :: xs => myFoldl combine (combine accumulator x) xs

/- Solved exercises -/

def myLength {α : Type} : List α → Nat
  | [] => 0
  | _ :: xs => 1 + myLength xs

def myMap {α β : Type} (f : α → β) : List α → List β
  | [] => []
  | x :: xs => f x :: myMap f xs

def myAny {α : Type} (predicate : α → Bool) : List α → Bool
  | [] => false
  | x :: xs => predicate x || myAny predicate xs

def myAll {α : Type} (predicate : α → Bool) : List α → Bool
  | [] => true
  | x :: xs => predicate x && myAll predicate xs

example (xs : List α) : myAppend [] xs = xs := by
  rfl

example (xs : List α) : myTake 0 xs = [] := by
  rfl

#eval myReverse [1, 2, 3, 4]
#eval myFilter (fun n => n % 2 == 0) [1, 2, 3, 4, 5, 6]
#eval myFoldl (fun total n => total + n) 0 [1, 2, 3, 4]
#eval myAny (fun n => n == 3) [1, 2, 3]

/- Study notes:
- `myTake` recurses on both the number and the list.
- The neutral result of `any` is false; the neutral result of `all` is true.
- A fold separates traversal from the operation performed at every element.
-/
