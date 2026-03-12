/-
TacticsCheatsheet.lean

Goal:
- collect the most common beginner tactics
- provide a quick review file
-/

variable (p q r : Prop)
variable (a b c : Nat)

-- intro: introduce an assumption
example : p → p := by
  intro hp
  exact hp

-- exact: close the goal with a term already available
example (hp : p) : p := by
  exact hp

-- apply: use an implication or theorem to reduce the goal
example (hpq : p → q) (hp : p) : q := by
  apply hpq
  exact hp

-- constructor: build conjunctions and structures with fields
example (hp : p) (hq : q) : p ∧ q := by
  constructor
  · exact hp
  · exact hq

-- left / right: choose one side of a disjunction
example (hp : p) : p ∨ q := by
  left
  exact hp

example (hq : q) : p ∨ q := by
  right
  exact hq

-- cases: split into cases
example (h : p ∨ q) : q ∨ p := by
  cases h with
  | inl hp =>
      right
      exact hp
  | inr hq =>
      left
      exact hq

-- rw: rewrite using an equality
example (h : a = b) : a + 1 = b + 1 := by
  rw [h]

-- simp: simplify expressions automatically
example (n : Nat) : n + 0 = n := by
  simp

-- induction: prove by induction on Nat
example (n : Nat) : n + 0 = n := by
  induction n with
  | zero =>
      rfl
  | succ n ih =>
      simp [ih]

-- have: introduce an intermediate fact
example (hpq : p → q) (hqr : q → r) (hp : p) : r := by
  have hq : q := hpq hp
  exact hqr hq

-- From False, anything follows
example (hFalse : False) : p := by
  cases hFalse

/-
Mini summary:

intro       -- introduce variables / hypotheses
exact       -- solve the goal directly
apply       -- use a theorem or implication
constructor -- build conjunctions
left/right  -- choose a side of a disjunction
cases       -- split into cases
rw          -- rewrite using equalities
simp        -- simplify automatically
induction   -- do induction
have        -- create an intermediate result

Exercises:
1. Re-prove every example in a slightly different way
2. For each tactic, add one extra example of your own
3. Build a personal file called MyTactics.lean
-/
