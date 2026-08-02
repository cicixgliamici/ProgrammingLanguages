/-
007_LogicExercises1.lean

Goals:
- read implications as functions between proofs;
- construct and eliminate conjunctions and disjunctions;
- understand negation as `p → False`.
-/

variable (p q r : Prop)

example : p → p := by
  intro hp
  exact hp

-- Applying `hpq` produces a proof of `q`; applying `hqr` then produces `r`.
example : (p → q) → (q → r) → p → r := by
  intro hpq hqr hp
  exact hqr (hpq hp)

example : p → q → p ∧ q := by
  intro hp hq
  constructor
  · exact hp
  · exact hq

example : p ∧ q → p := by
  intro hpq
  exact hpq.left

example : p → p ∨ q := by
  intro hp
  left
  exact hp

/- To consume a disjunction, both possible constructors must be considered.
   Each branch receives the proof stored by that constructor. -/
example : (p → r) → (q → r) → p ∨ q → r := by
  intro hpr hqr hpq
  cases hpq with
  | inl hp => exact hpr hp
  | inr hq => exact hqr hq

/-
Solved exercises

Exercise 1: prove `(p ∧ q) → (q ∧ p)`.
Exercise 2: prove `(p ∨ q) → (q ∨ p)`.
Exercise 3: prove `(p → q) → (¬q → ¬p)`.
Exercise 4: prove `p ∧ (q ∧ r) → (p ∧ q) ∧ r`.
-/

-- Destruct the input pair of proofs, then rebuild it in the opposite order.
theorem and_comm_from_proofs : (p ∧ q) → (q ∧ p) := by
  intro hpq
  exact ⟨hpq.right, hpq.left⟩

-- Each constructor of the input disjunction selects the opposite output side.
theorem or_comm_from_cases : (p ∨ q) → (q ∨ p) := by
  intro hpq
  cases hpq with
  | inl hp => exact Or.inr hp
  | inr hq => exact Or.inl hq

-- This is contraposition: assuming `p` would produce the forbidden proof of `q`.
theorem contrapositive : (p → q) → (¬q → ¬p) := by
  intro hpq hnq hp
  exact hnq (hpq hp)

theorem and_assoc_forward : p ∧ (q ∧ r) → (p ∧ q) ∧ r := by
  intro h
  exact ⟨⟨h.left, h.right.left⟩, h.right.right⟩

/- Study notes:
- `intro` moves the input of an implication into the local context.
- `constructor` splits a conjunction goal; `cases` eliminates a disjunction.
- `⟨a, b⟩` is compact term syntax for constructing a pair or conjunction.
- Lean's core logic is constructive: a proposition is proved by building a value.
-/
