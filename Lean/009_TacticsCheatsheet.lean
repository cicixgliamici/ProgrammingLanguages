/-
009_TacticsCheatsheet.lean

A compact reference for common beginner tactics. Each example explains the
shape of goal for which the tactic is useful.
-/

variable (p q r : Prop)
variable (a b : Nat)

-- `intro` handles `∀ x, ...` and implications by introducing their input.
example : p → p := by
  intro hp
  exact hp

-- `apply` uses a rule whose conclusion matches the current goal.
example (hpq : p → q) (hp : p) : q := by
  apply hpq
  exact hp

-- `constructor` selects a constructor and creates a goal for each argument.
example (hp : p) (hq : q) : p ∧ q := by
  constructor
  · exact hp
  · exact hq

-- `left` and `right` select which constructor of `Or` to build.
example (hp : p) : p ∨ q := by
  left
  exact hp

-- `cases` eliminates a value by considering every constructor.
example (h : p ∨ q) : q ∨ p := by
  cases h with
  | inl hp => exact Or.inr hp
  | inr hq => exact Or.inl hq

-- `rw` substitutes equals for equals in the goal.
example (h : a = b) : a + 1 = b + 1 := by
  rw [h]

-- `simp` repeatedly applies tagged simplification lemmas and definitions supplied.
example (n : Nat) : n + 0 = n := by
  simp

-- `induction` adds an induction hypothesis for the structurally smaller value.
example (n : Nat) : n + 0 = n := by
  induction n with
  | zero => rfl
  | succ n ih =>
      change n + 0 + 1 = n + 1
      rw [ih]

-- `have` records an intermediate result with a readable name and type.
example (hpq : p → q) (hqr : q → r) (hp : p) : r := by
  have hq : q := hpq hp
  exact hqr hq

-- `rfl` proves definitional equality after Lean reduces both sides.
example : (fun x : Nat => x + 1) 2 = 3 := by
  rfl

-- `<;>` runs the tactic on every goal produced by the preceding tactic.
example (value : Bool) : value = true ∨ value = false := by
  cases value <;> simp

-- From an impossible value, `cases` can prove any proposition.
example (h : False) : p := by
  cases h

/- Quick choice guide:
- implication or universal quantifier: `intro`;
- known theorem ending in the goal: `apply`;
- equality by computation: `rfl`;
- equality hypothesis: `rw`;
- routine simplification: `simp`;
- recursive data and recursive claim: `induction`;
- alternatives stored in a value: `cases`.

Exercises:
1. Re-prove every example using a slightly different tactic or proof term.
2. Add one original example for each tactic in this file.
3. Build a personal reference file named `MyTactics.lean`.
-/
