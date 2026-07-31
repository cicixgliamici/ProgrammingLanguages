/-
007a_Solved.lean

Alternative solutions to the exercises in 007. These longer tactic proofs are
kept to make every intermediate step visible to a beginner.
-/

variable (p q r : Prop)

example : (p ∧ q) → (q ∧ p) := by
  intro hpq
  constructor
  · exact hpq.right
  · exact hpq.left

example : (p ∨ q) → (q ∨ p) := by
  intro hpq
  cases hpq with
  | inl hp =>
      right
      exact hp
  | inr hq =>
      left
      exact hq

example : (p → q) → (¬q → ¬p) := by
  intro hpq hnq hp
  apply hnq
  exact hpq hp

example : p ∧ (q ∧ r) → (p ∧ q) ∧ r := by
  intro h
  constructor
  · constructor
    · exact h.left
    · exact h.right.left
  · exact h.right.right
