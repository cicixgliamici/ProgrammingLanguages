/-
002_RewritingAndSimp.lean

Goal:
- use equality hypotheses
- understand rw
- understand simp
-/

-- If a = b, then a + 1 = b + 1
example (a b : Nat) (h : a = b) : a + 1 = b + 1 := by
  rw [h]

-- If a = b and b = c, then a = c
example (a b c : Nat) (h1 : a = b) (h2 : b = c) : a = c := by
  rw [h1]
  rw [h2]

-- simp can simplify many standard expressions
example (n : Nat) : n + 0 = n := by
  simp

example (n : Nat) : 0 + n = n := by
  simp

example (b : Bool) : (not (not b)) = b := by
  cases b <;> rfl

-- simp and rw are often enough for simple equalities
example (a b : Nat) (h : a = b) : b = a := by
  rw [h]

/-
Exercises:
1. Prove: if h : x = y, then x * 2 = y * 2
2. Try simp here:
   example (n : Nat) : n * 1 = n := by ...
3. Prove: if h1 : a = b and h2 : c = d, then a + c = b + d
-/
