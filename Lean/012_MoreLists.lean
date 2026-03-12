/-
012_MoreLists.lean

Goal:
- practice recursive programming on lists
- define common list-processing functions
- prepare for list proofs
-/

-- Append two lists
def myAppend : List α → List α → List α
  | [], ys => ys
  | x :: xs, ys => x :: myAppend xs ys

#eval myAppend [1, 2] [3, 4]
#eval myAppend ([] : List Nat) [7, 8]

-- Reverse a list
def myReverse : List α → List α
  | [] => []
  | x :: xs => myAppend (myReverse xs) [x]

#eval myReverse [1, 2, 3, 4]
#eval myReverse ["a", "b", "c"]

-- Filter with a predicate
def myFilter (p : α → Bool) : List α → List α
  | [] => []
  | x :: xs =>
      if p x then
        x :: myFilter p xs
      else
        myFilter p xs

#eval myFilter (fun n => n % 2 == 0) [1, 2, 3, 4, 5, 6]

-- Take the first n elements
def myTake : Nat → List α → List α
  | 0, _ => []
  | _ + 1, [] => []
  | n + 1, x :: xs => x :: myTake n xs

#eval myTake 3 [10, 20, 30, 40, 50]
#eval myTake 10 [1, 2]

-- Drop the first n elements
def myDrop : Nat → List α → List α
  | 0, xs => xs
  | _ + 1, [] => []
  | n + 1, _ :: xs => myDrop n xs

#eval myDrop 2 [10, 20, 30, 40]
#eval myDrop 10 [1, 2]

-- Zip two lists together until one runs out
def myZip : List α → List β → List (α × β)
  | [], _ => []
  | _, [] => []
  | x :: xs, y :: ys => (x, y) :: myZip xs ys

#eval myZip [1, 2, 3] ["a", "b", "c"]
#eval myZip [1, 2] ["x"]

-- A left fold
def myFoldl (f : β → α → β) : β → List α → β
  | acc, [] => acc
  | acc, x :: xs => myFoldl f (f acc x) xs

#eval myFoldl (fun acc x => acc + x) 0 [1, 2, 3, 4]
#eval myFoldl (fun acc s => acc ++ s) "" ["Le", "an"]

-- Small basic facts
example : myAppend [1, 2] [3] = [1, 2, 3] := rfl
example : myReverse [1, 2] = [2, 1] := rfl
example : myTake 2 [5, 6, 7] = [5, 6] := rfl
example : myDrop 2 [5, 6, 7] = [7] := rfl

/-
Exercises:
1. Define myLength : List α → Nat
2. Define myMap : (α → β) → List α → List β
3. Define myAny : (α → Bool) → List α → Bool
4. Define myAll : (α → Bool) → List α → Bool
5. Prove: myAppend [] xs = xs
6. Prove: myTake 0 xs = []
-/
