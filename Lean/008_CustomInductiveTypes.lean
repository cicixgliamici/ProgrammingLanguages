/-
008_CustomInductiveTypes.lean

Goals:
- define algebraic data types with `inductive`;
- use constructors and exhaustive pattern matching;
- recurse over a custom tree.
-/

inductive Day where
  | monday | tuesday | wednesday | thursday | friday | saturday | sunday
deriving Repr, DecidableEq

def isWeekend : Day → Bool
  | .saturday | .sunday => true
  | _ => false

def nextDay : Day → Day
  | .monday => .tuesday
  | .tuesday => .wednesday
  | .wednesday => .thursday
  | .thursday => .friday
  | .friday => .saturday
  | .saturday => .sunday
  | .sunday => .monday

/- `MyOption α` contains either no value or one value of type `α`.
   The parameter makes one reusable type family instead of many concrete types. -/
inductive MyOption (α : Type) where
  | none
  | some (value : α)
deriving Repr

def getOrElse {α : Type} (default : α) : MyOption α → α
  | .none => default
  | .some value => value

inductive MyTree (α : Type) where
  | leaf (value : α)
  | node (left right : MyTree α)
deriving Repr

def countLeaves {α : Type} : MyTree α → Nat
  | .leaf _ => 1
  | .node left right => countLeaves left + countLeaves right

def exampleTree : MyTree Nat :=
  .node (.leaf 1) (.node (.leaf 2) (.leaf 3))

#eval isWeekend Day.sunday
#eval getOrElse 0 (MyOption.some 10)
#eval countLeaves exampleTree

/-
Solved exercises

Exercise 1: define `previousDay : Day → Day`.
Exercise 2: define `mapTree : (α → β) → MyTree α → MyTree β`.
Exercise 3: define `treeSize : MyTree α → Nat`.
Exercise 4: prove by cases that moving to the next day and then to the
previous day returns the original `Day`.
-/

-- Pattern matching covers every constructor, including the weekly wraparound.
def previousDay : Day → Day
  | .monday => .sunday
  | .tuesday => .monday
  | .wednesday => .tuesday
  | .thursday => .wednesday
  | .friday => .thursday
  | .saturday => .friday
  | .sunday => .saturday

-- Mapping changes leaf values while preserving the exact tree shape.
def mapTree {α β : Type} (f : α → β) : MyTree α → MyTree β
  | .leaf value => .leaf (f value)
  | .node left right => .node (mapTree f left) (mapTree f right)

-- This size counts both leaves and internal nodes.
def treeSize {α : Type} : MyTree α → Nat
  | .leaf _ => 1
  | .node left right => 1 + treeSize left + treeSize right

/- There is no separate proof that a result is a valid `Day`: Lean's return type
   already guarantees it. This theorem demonstrates that the seven cases reduce. -/
theorem previous_next_day (d : Day) : previousDay (nextDay d) = d := by
  cases d <;> rfl

/- Study notes:
- Constructors are the only ways to create values of an inductive type.
- Pattern matching must cover every constructor, making functions exhaustive.
- `deriving Repr` enables printing; `DecidableEq` enables computable equality.
-/
