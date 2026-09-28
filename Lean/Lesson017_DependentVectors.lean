/-!
Lesson017_DependentVectors.lean

Goals:
- understand a type that depends on a value;
- encode list length in the type of a vector;
- use `Fin n` to represent an index that is provably within bounds.
-/

/- `SizedList α n` is a family of types indexed by a natural number. Its
   constructors guarantee that `nil` has length zero and `cons` adds one. -/
inductive SizedList (α : Type) : Nat → Type where
  | nil : SizedList α 0
  | cons : α → SizedList α n → SizedList α (n + 1)
deriving Repr

namespace SizedList

-- No empty case is required: the input type proves the vector has a head.
def head : SizedList α (n + 1) → α
  | .cons value _ => value

def tail : SizedList α (n + 1) → SizedList α n
  | .cons _ rest => rest

def map (f : α → β) : SizedList α n → SizedList β n
  | .nil => .nil
  | .cons value rest => .cons (f value) (map f rest)

/- The result length is part of the signature. The index is written as `m + n`
   because Lean reduces addition structurally on its second argument. It is
   mathematically equal to `n + m`, while avoiding casts inside this definition. -/
def append : SizedList α n → SizedList α m → SizedList α (m + n)
  | .nil, right => right
  | .cons value rest, right => .cons value (append rest right)

def toList : SizedList α n → List α
  | .nil => []
  | .cons value rest => value :: toList rest

/- `Fin n` contains a natural number together with evidence that it is below
   `n`. Its constructors mirror zero and successor indices. -/
def get : SizedList α n → Fin n → α
  | .cons value _, ⟨0, _⟩ => value
  | .cons _ rest, ⟨index + 1, isValid⟩ =>
      get rest ⟨index, Nat.lt_of_succ_lt_succ isValid⟩

def exampleVector : SizedList String 3 :=
  .cons "Lean" (.cons "Lake" (.cons "Elan" .nil))

#eval head exampleVector
#eval get exampleVector ⟨1, by decide⟩
#eval toList (map String.length exampleVector)

/-
Solved exercises

Exercise 1: define `replicate`, whose result length equals the requested count.
Exercise 2: define a total `last` function for every non-empty `SizedList`.
Exercise 3: prove that converting after `map` agrees with `List.map`.
Exercise 4: prove that converting after `append` agrees with `List.append`.
-/

-- Recursing on `count` lets each branch construct the required length index.
def replicate (count : Nat) (value : α) : SizedList α count :=
  match count with
  | 0 => .nil
  | n + 1 => .cons value (replicate n value)

/- Making the length index an explicit argument lets each branch reveal exactly
   which vector shape is possible at that length. -/
def last : (n : Nat) → SizedList α (n + 1) → α
  | 0, .cons value .nil => value
  | n + 1, .cons _ rest => last n rest

-- Structural induction exposes the same recursion used by both map functions.
theorem toList_map (f : α → β) (values : SizedList α n) :
    toList (map f values) = List.map f (toList values) := by
  induction values with
  | nil => rfl
  | cons value rest ih => simp [map, toList, ih]

theorem toList_append (left : SizedList α n) (right : SizedList α m) :
    toList (append left right) = toList left ++ toList right := by
  induction left with
  | nil => rfl
  | cons value rest ih => simp [append, toList, ih]

#eval toList (replicate 4 true)
#eval last 2 exampleVector

/- Study notes:
- In dependent types, later parts of a type may mention earlier values.
- `SizedList α n` rules out length mismatches before the program can run.
- `Fin n` rules out invalid indices, so `get` needs no `Option` result.
- Stronger guarantees require callers to provide stronger evidence.
-/

end SizedList
