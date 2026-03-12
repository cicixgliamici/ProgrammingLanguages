/-
Propositions.lean

Goal:
- understand that propositions are types
- use example
- write first proof terms
- use intro / exact
-/

-- A trivial proof: everything is equal to itself
example : 2 = 2 := rfl

example : true = true := rfl

-- Work with generic propositions
variable (p q r : Prop)

-- p → p
example : p → p := by
  intro hp
  exact hp

-- p → q → p
example : p → q → p := by
  intro hp
  intro hq
  exact hp

-- p → q → q
example : p → q → q := by
  intro hp
  intro hq
  exact hq

-- (p → q) → p → q
example : (p → q) → p → q := by
  intro hpq
  intro hp
  exact hpq hp

-- ∀ n : Nat, n = n
example : ∀ n : Nat, n = n := by
  intro n
  rfl

/-
Things to notice:
- intro introduces hypotheses or variables
- exact closes the goal using an available proof
- rfl closes reflexive equalities

Exercises:
1. Prove q → p → q
2. Prove (p → q) → (q → r) → p → r
-/
