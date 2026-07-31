/-
011_ProductSumTypes.lean

Goals:
- distinguish product types from sum types;
- construct and consume pairs;
- see the connection between data constructors and logical connectives.
-/

def myPair : Nat × String := (5, "lean")

-- A product contains both components at the same time.
def swapPair {α β : Type} : α × β → β × α
  | (left, right) => (right, left)

def first {α β : Type} : α × β → α
  | (left, _) => left

def second {α β : Type} : α × β → β
  | (_, right) => right

-- A sum contains exactly one of its alternatives, identified by its constructor.
inductive MySum (α β : Type) where
  | inl (value : α)
  | inr (value : β)
deriving Repr

def mapLeft {α β γ : Type} (f : α → γ) : MySum α β → MySum γ β
  | .inl value => .inl (f value)
  | .inr value => .inr value

def mapRight {α β γ : Type} (f : β → γ) : MySum α β → MySum α γ
  | .inl value => .inl value
  | .inr value => .inr (f value)

-- Eliminating a sum requires a handler for each possible alternative.
def sumElim {α β γ : Type} (onLeft : α → γ) (onRight : β → γ) :
    MySum α β → γ
  | .inl value => onLeft value
  | .inr value => onRight value

/- Solved exercises -/

def pairMap {α β γ δ : Type} (f : α → γ) (g : β → δ) :
    α × β → γ × δ
  | (left, right) => (f left, g right)

def isLeft {α β : Type} : MySum α β → Bool
  | .inl _ => true
  | .inr _ => false

def isRight {α β : Type} : MySum α β → Bool
  | .inl _ => false
  | .inr _ => true

theorem swapPair_twice (pair : α × β) : swapPair (swapPair pair) = pair := by
  cases pair
  rfl

def mergeSum {α : Type} : MySum α α → α
  | .inl value => value
  | .inr value => value

#eval pairMap (fun n => n + 1) String.length (4, "Lean")
#eval isLeft (MySum.inl 5 : MySum Nat String)

/- Study notes:
- Products correspond to “and”: a value supplies both components.
- Sums correspond to “or”: a value supplies one tagged alternative.
- Pattern matching on a pair exposes both fields; matching a sum creates branches.
-/
