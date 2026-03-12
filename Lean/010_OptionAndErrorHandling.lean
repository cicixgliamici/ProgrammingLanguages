/-
10_OptionAndErrorHandling.lean

Goal:
- understand Option
- handle partial computations safely
- practice pattern matching on some / none
-/

-- Return the first element of a list, if it exists
def safeHead : List α → Option α
  | [] => none
  | x :: _ => some x

#eval safeHead ([] : List Nat)
#eval safeHead [10, 20, 30]

-- Return the tail of a list, if it exists
def safeTail : List α → Option (List α)
  | [] => none
  | _ :: xs => some xs

#eval safeTail ([] : List Nat)
#eval safeTail [1, 2, 3]

-- Safe predecessor: 0 has no predecessor in this version
def safePred : Nat → Option Nat
  | 0 => none
  | n + 1 => some n

#eval safePred 0
#eval safePred 7

-- Extract a value from Option, using a default when needed
def getOrElse : Option α → α → α
  | none, default => default
  | some x, _ => x

#eval getOrElse (some 5) 0
#eval getOrElse (none : Option Nat) 0

-- Safe division by zero
def safeDiv (a b : Nat) : Option Nat :=
  match b with
  | 0 => none
  | _ => some (a / b)

#eval safeDiv 10 2
#eval safeDiv 10 0

-- Map a function over Option
def optionMap (f : α → β) : Option α → Option β
  | none => none
  | some x => some (f x)

#eval optionMap (fun x => x + 1) (some 10)
#eval optionMap (fun x => x + 1) (none : Option Nat)

-- If the input is some x, return some (f x); otherwise none
def optionBind (oa : Option α) (f : α → Option β) : Option β :=
  match oa with
  | none => none
  | some x => f x

#eval optionBind (some 5) (fun x => some (x + 3))
#eval optionBind (none : Option Nat) (fun x => some (x + 3))

-- Simple proofs
example : safeHead ([] : List Nat) = none := rfl

example : safeHead [3] = some 3 := rfl

example : getOrElse (none : Option Nat) 42 = 42 := rfl

example : getOrElse (some 7) 0 = 7 := rfl

/-
Exercises:
1. Define safeLast : List α → Option α
2. Define safeNth : List α → Nat → Option α
3. Prove: optionMap f none = none
4. Prove: getOrElse (some x) d = x
5. Define isSome : Option α → Bool
-/
