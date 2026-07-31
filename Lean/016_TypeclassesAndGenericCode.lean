/-
016_TypeclassesAndGenericCode.lean

Goals:
- understand typeclasses as interfaces selected by type;
- define and use instances;
- write generic functions that request capabilities instead of concrete types.
-/

/- A class declares an operation that a type may support. The output is a
   `String`, so examples can be evaluated without using `IO`. -/
class Describe (α : Type) where
  describe : α → String

-- Square brackets request an instance that Lean should find automatically.
def describeTwice {α : Type} [Describe α] (value : α) : String :=
  Describe.describe value ++ " | " ++ Describe.describe value

instance : Describe Nat where
  describe number := s!"natural number: {number}"

instance : Describe Bool where
  describe value :=
    if value then "boolean: true" else "boolean: false"

#eval Describe.describe 12
#eval describeTwice true

/- Instances can depend on other instances. A pair is describable whenever
   both component types are describable. -/
instance {α β : Type} [Describe α] [Describe β] : Describe (α × β) where
  describe pair :=
    "(" ++ Describe.describe pair.1 ++ ", " ++ Describe.describe pair.2 ++ ")"

#eval Describe.describe (3, false)

/- Standard typeclasses work in the same way. `[BEq α]` supplies the `==`
   operation, allowing this function to work for many element types. -/
def countOccurrences {α : Type} [BEq α] (wanted : α) : List α → Nat
  | [] => 0
  | value :: rest =>
      if value == wanted then 1 + countOccurrences wanted rest
      else countOccurrences wanted rest

#eval countOccurrences 2 [1, 2, 3, 2, 2]
#eval countOccurrences "Lean" ["C", "Lean", "Lean"]

/- A structure stores data. A class usually describes behavior. The distinction
   is conventional rather than absolute, but it keeps APIs easy to understand. -/
structure User where
  name : String
  active : Bool
deriving Repr, BEq, Inhabited

instance : Describe User where
  describe user :=
    let status := if user.active then "active" else "inactive"
    s!"user {user.name} ({status})"

def users : List User :=
  [{ name := "Ada", active := true }, { name := "Linus", active := false }]

-- `head!` requests `Inhabited User` as a fallback for an empty list.
#eval Describe.describe users.head!

/- Solved exercises -/

-- A default value is useful when a computation has no result.
class DefaultValue (α : Type) where
  defaultValue : α

instance : DefaultValue Nat where
  defaultValue := 0

instance : DefaultValue String where
  defaultValue := ""

def headOrDefault {α : Type} [DefaultValue α] : List α → α
  | [] => DefaultValue.defaultValue
  | value :: _ => value

example : headOrDefault ([] : List Nat) = 0 := by
  rfl

example : headOrDefault ["Lean", "Lake"] = "Lean" := by
  rfl

/- Instance synthesis can be inspected directly. Lean fills the expected
   dictionary using the instances currently in scope. -/
#synth Describe Nat
#synth Describe (Nat × Bool)
#synth BEq User

/- Study notes:
- `[Capability α]` is an implicit parameter resolved by instance synthesis.
- Use a typeclass when several types share an operation with type-specific code.
- Instances may themselves require instances, creating reusable generic layers.
- Ambiguous or overlapping instances should be avoided in beginner-facing APIs.
-/
