/-
011_ProductSumTypes.lean

Goal:
- understand product types and sum types
- work with pairs
- define and use a custom sum type
-/

-- A pair of values of possibly different types
def myPair : Nat × String := (5, "lean")

#eval myPair.1
#eval myPair.2

-- Swap the components of a pair
def swapPair : α × β → β × α
  | (a, b) => (b, a)

#eval swapPair (10, "hello")
#eval swapPair (true, 7)

-- Return the first component
def first : α × β → α
  | (a, _) => a

-- Return the second component
def second : α × β → β
  | (_, b) => b

#eval first (3, "x")
#eval second (3, "x")

-- A custom sum type, similar to Either
inductive MySum (α β : Type) where
  | inl : α → MySum α β
  | inr : β → MySum α β
deriving Repr

-- Map a function on the left side
def mapLeft (f : α → γ) : MySum α β → MySum γ β
  | MySum.inl a => MySum.inl (f a)
  | MySum.inr b => MySum.inr b

-- Map a function on the right side
def mapRight (g : β → γ) : MySum α β → MySum α γ
  | MySum.inl a => MySum.inl a
  | MySum.inr b => MySum.inr (g b)

#eval mapLeft (fun x => x + 1) (MySum.inl 5 : MySum Nat String)
#eval mapLeft (fun x => x + 1) (MySum.inr "ok" : MySum Nat String)

#eval mapRight String.length (MySum.inr "lean" : MySum Nat String)
#eval mapRight String.length (MySum.inl 99 : MySum Nat String)

-- Consume a sum by handling both cases
def sumElim (f : α → γ) (g : β → γ) : MySum α β → γ
  | MySum.inl a => f a
  | MySum.inr b => g b

#eval sumElim (fun n => n + 1) String.length (MySum.inl 7 : MySum Nat String)
#eval sumElim (fun n => n + 1) String.length (MySum.inr "abc" : MySum Nat String)

-- Small proofs on pairs
example : first (10, 20) = 10 := rfl
example : second (10, 20) = 20 := rfl
example : swapPair ("a", 3) = (3, "a") := rfl

/-
Exercises:
1. Define a function pairMap : (α → γ) → (β → δ) → (α × β) → (γ × δ)
2. Define a function isLeft : MySum α β → Bool
3. Define a function isRight : MySum α β → Bool
4. Prove: swapPair (swapPair p) = p
5. Define a function mergeSum : MySum α α → α
-/
