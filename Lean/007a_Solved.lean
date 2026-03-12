/-
007a_Solved exercises for LogicExercises.lean
-/

variable (p q r : Prop)

-- 1. Prove: (p ∧ q) → (q ∧ p)
example : (p ∧ q) → (q ∧ p) := by
  intro hpq
  constructor
  · exact hpq.right
  · exact hpq.left

-- 2. Prove: (p ∨ q) → (q ∨ p)
example : (p ∨ q) → (q ∨ p) := by
  intro hpq
  cases hpq with
  | inl hp =>
      right
      exact hp
  | inr hq =>
      left
      exact hq

-- 3. Prove: (p → q) → (¬ q → ¬ p)
example : (p → q) → (¬ q → ¬ p) := by
  intro hpq
  intro hnq
  intro hp
  apply hnq
  exact hpq hp

-- 4. Prove: p ∧ (q ∧ r) → (p ∧ q) ∧ r
example : p ∧ (q ∧ r) → (p ∧ q) ∧ r := by
  intro h
  constructor
  · constructor
    · exact h.left
    · exact h.right.left
  · exact h.right.right
