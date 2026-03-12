/-
007_LogicExercises.lean

Goal:
- practice basic propositional logic in Lean
- use intro, exact, apply, constructor, left, right
-/

variable (p q r : Prop)

-- Identity
example : p → p := by
  intro hp
  exact hp

-- Keep the first hypothesis
example : p → q → p := by
  intro hp
  intro hq
  exact hp

-- Compose implications
example : (p → q) → (q → r) → p → r := by
  intro hpq
  intro hqr
  intro hp
  exact hqr (hpq hp)

-- Build a conjunction
example : p → q → p ∧ q := by
  intro hp
  intro hq
  constructor
  · exact hp
  · exact hq

-- Extract the left part of a conjunction
example : p ∧ q → p := by
  intro hpq
  exact hpq.left

-- Extract the right part of a conjunction
example : p ∧ q → q := by
  intro hpq
  exact hpq.right

-- Build a disjunction: left case
example : p → p ∨ q := by
  intro hp
  left
  exact hp

-- Build a disjunction: right case
example : q → p ∨ q := by
  intro hq
  right
  exact hq

-- Use a disjunction by case analysis
example : (p → r) → (q → r) → p ∨ q → r := by
  intro hpr
  intro hqr
  intro hpq
  cases hpq with
  | inl hp =>
      exact hpr hp
  | inr hq =>
      exact hqr hq

-- Negation is a function to False
example : (p → False) → p → False := by
  intro hnp
  intro hp
  exact hnp hp

/-
Exercises:
1. Prove: (p ∧ q) → (q ∧ p)
2. Prove: (p ∨ q) → (q ∨ p)
3. Prove: (p → q) → (¬ q → ¬ p)
4. Prove: p ∧ (q ∧ r) → (p ∧ q) ∧ r
-/
