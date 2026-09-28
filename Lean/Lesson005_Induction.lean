/-!
Lesson005_Induction.lean

Goals:
- understand structural recursion on natural numbers;
- understand the base case and the inductive step;
- use an induction hypothesis in a proof.
-/

/- `fact` follows the two constructors of `Nat`: zero and successor.
   Lean accepts the definition because every recursive call uses the smaller `n`. -/
def fact : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fact n

#eval fact 0
#eval fact 5

/- Induction creates one goal for zero and one for `n + 1`.
   In the successor case, `ih` is the result already known for `n`. -/
theorem add_zero_by_induction (n : Nat) : n + 0 = n := by
  induction n with
  | zero => rfl
  | succ n ih =>
      change n + 0 + 1 = n + 1
      rw [ih]

-- This theorem does not require induction because `simp` knows the library rule.
theorem zero_add_with_simp (n : Nat) : 0 + n = n := by
  simp

def myDouble : Nat → Nat
  | 0 => 0
  | n + 1 => myDouble n + 2

theorem myDouble_eq_twice (n : Nat) : myDouble n = 2 * n := by
  induction n with
  | zero => rfl
  | succ n ih => simp [myDouble, ih, Nat.mul_add]

/-
Solved exercises

Exercise 1: define `sumTo : Nat → Nat`, computing `0 + 1 + ... + n`.
Exercise 2: prove that `sumTo 0 = 0`.
Exercise 3: prove a simple property of the recursive function `sumTo`.

The statements remain next to their solutions so the file can be used both as
an exercise sheet and as a worked reference.
-/

-- `sumTo n` computes 0 + 1 + ... + n.
def sumTo : Nat → Nat
  | 0 => 0
  | n + 1 => sumTo n + (n + 1)

#eval sumTo 0
#eval sumTo 5

-- The base equation is true by computation, so reflexivity is sufficient.
example : sumTo 0 = 0 := by
  rfl

-- Expanding the recursive equation exposes exactly the successor case.
theorem sumTo_succ (n : Nat) : sumTo (n + 1) = sumTo n + (n + 1) := by
  rfl

-- A recursive computation never decreases its previous partial sum.
theorem sumTo_le_succ (n : Nat) : sumTo n ≤ sumTo (n + 1) := by
  simp [sumTo]

/- Study notes:
- Use `rfl` when both sides reduce to the same expression by computation.
- Use `simp [definition, ih]` to unfold a definition and apply known facts.
- Induction is appropriate when the statement for `n + 1` depends on the
  same statement for `n`.
-/
