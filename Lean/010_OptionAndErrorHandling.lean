/-
010_OptionAndErrorHandling.lean

Goals:
- represent computations that may fail with `Option`;
- combine optional computations without unsafe placeholder values;
- prove equations by reducing pattern matches.
-/

def safeHead {α : Type} : List α → Option α
  | [] => none
  | x :: _ => some x

def safeTail {α : Type} : List α → Option (List α)
  | [] => none
  | _ :: xs => some xs

-- Zero has no predecessor in `Nat`, so failure is represented explicitly.
def safePred : Nat → Option Nat
  | 0 => none
  | n + 1 => some n

def getOrElse {α : Type} : Option α → α → α
  | none, default => default
  | some value, _ => value

def safeDiv (dividend divisor : Nat) : Option Nat :=
  match divisor with
  | 0 => none
  | _ => some (dividend / divisor)

-- `optionMap` changes a present value and preserves absence.
def optionMap {α β : Type} (f : α → β) : Option α → Option β
  | none => none
  | some value => some (f value)

/- `optionBind` sequences operations that can each fail. If the first operation
   fails, its continuation is not called. This is the essential monadic pattern. -/
def optionBind {α β : Type} (value : Option α)
    (next : α → Option β) : Option β :=
  match value with
  | none => none
  | some present => next present

#eval safeHead [10, 20, 30]
#eval safeDiv 10 0
#eval optionBind (some 5) (fun x => some (x + 3))

/-
Solved exercises

Exercise 1: define `safeLast : List α → Option α`.
Exercise 2: define `safeNth : List α → Nat → Option α`.
Exercise 3: prove that `optionMap f none = none`.
Exercise 4: prove that `getOrElse (some x) d = x`.
Exercise 5: define `isSome : Option α → Bool`.
-/

-- A singleton reveals the answer; longer lists delegate to their shorter tail.
def safeLast {α : Type} : List α → Option α
  | [] => none
  | [x] => some x
  | _ :: xs => safeLast xs

-- Matching the list and index together makes both failure cases explicit.
def safeNth {α : Type} : List α → Nat → Option α
  | [], _ => none
  | x :: _, 0 => some x
  | _ :: xs, n + 1 => safeNth xs n

-- Only the constructor matters, so the contained value can be ignored.
def isSome {α : Type} : Option α → Bool
  | none => false
  | some _ => true

example (f : α → β) : optionMap f none = none := by
  rfl

example (x d : α) : getOrElse (some x) d = x := by
  rfl

theorem optionMap_identity (value : Option α) :
    optionMap (fun x => x) value = value := by
  cases value <;> rfl

#eval safeLast [1, 2, 3]
#eval safeNth [10, 20, 30] 1

/- Study notes:
- `Option α` forces callers to handle both `some value` and `none`.
- Prefer explicit failure to special values such as zero or an empty string.
- `map` is for a total transformation; `bind` is for a transformation that may fail.
-/
