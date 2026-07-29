/-
002_RewritingAndSimp.lean

Goals:
- use equality hypotheses
- understand `rw`
- understand rewriting direction
- understand `simp`
-/

/-
An equality hypothesis such as:

  h : a = b

can be used to replace occurrences of `a` with `b`.

The tactic:

  rw [h]

rewrites the current goal using the equality from left to right.

The tactic does not directly prove the theorem. It transforms the goal
into an equivalent one and generates a proof term that Lean's kernel checks.
-/

-- If `a = b`, replacing `a` with `b` reduces the goal to `b + 1 = b + 1`.
example (a b : Nat) (h : a = b) : a + 1 = b + 1 := by
  rw [h]

/-
Rewriting can be performed multiple times.

Initial goal:

  a = c

After `rw [h1]`:

  b = c

After `rw [h2]`:

  c = c

The final reflexive equality is closed automatically by `rw`.
-/
example (a b c : Nat) (h1 : a = b) (h2 : b = c) : a = c := by
  rw [h1]
  rw [h2]

/-
The arrow `←` reverses the direction of an equality.

If:

  h : a = b

then:

  rw [← h]

replaces occurrences of `b` with `a`.
-/
example (a b : Nat) (h : a = b) : b + 1 = a + 1 := by
  rw [← h]

/-
`simp` is a simplification tactic.

It repeatedly applies a collection of standard simplification rules,
such as:

  n + 0 = n
  0 + n = n
  n * 1 = n
  true && b = b

Unlike `rw`, which uses explicitly listed equalities in a controlled order,
`simp` searches its simplification database and applies suitable rules
automatically.

The resulting proof term is checked by Lean's kernel.
-/

example (n : Nat) : n + 0 = n := by
  simp

example (n : Nat) : 0 + n = n := by
  simp

/-
For a Boolean value, we can inspect all possible cases.

`cases b` creates one goal for `b = false` and another for `b = true`.

The combinator `<;>` applies `rfl` to every goal produced by `cases b`.
-/
example (b : Bool) : not (not b) = b := by
  cases b <;> rfl

-- The same fact is also known to the simplifier.
example (b : Bool) : not (not b) = b := by
  simp

/-
Rewriting can also prove symmetry.

Initial goal:

  b = a

Using `h : a = b`, `rw [h]` replaces the occurrence of `a`
on the right-hand side with `b`.

The goal becomes:

  b = b
-/
example (a b : Nat) (h : a = b) : b = a := by
  rw [h]

/-
An equality hypothesis can also be passed directly to `simp`.

`simp [h]` adds `h` to the simplification rules used for this goal.
-/
example (a b : Nat) (h : a = b) : a + 0 = b := by
  simp [h]

/-
Important tactics:

- `rw [h]` rewrites using `h` from left to right.
- `rw [← h]` rewrites using `h` from right to left.
- `rw [h1, h2]` performs multiple rewrites in sequence.
- `simp` applies standard simplification rules automatically.
- `simp [h]` also uses the explicitly supplied hypothesis or definition.
- `cases` splits a value according to its possible constructors.
- `<;>` applies the following tactic to every generated goal.
-/

/-
Exercise 1

If:

  h : x = y

then replacing `x` with `y` changes the goal into:

  y * 2 = y * 2
-/
example (x y : Nat) (h : x = y) : x * 2 = y * 2 := by
  rw [h]

/-
Exercise 2

The identity:

  n * 1 = n

is already available as a standard simplification rule.
-/
example (n : Nat) : n * 1 = n := by
  simp

/-
Exercise 3

We rewrite the two components independently:

  a + c = b + d
      ↓ h1
  b + c = b + d
      ↓ h2
  b + d = b + d
-/
example (a b c d : Nat) (h1 : a = b) (h2 : c = d) :
    a + c = b + d := by
  rw [h1]
  rw [h2]

/-
The same proof can be written with both rewrites in one command.
-/
example (a b c d : Nat) (h1 : a = b) (h2 : c = d) :
    a + c = b + d := by
  rw [h1, h2]

/-
`simp` can also use both equality hypotheses.
-/
example (a b c d : Nat) (h1 : a = b) (h2 : c = d) :
    a + c = b + d := by
  simp [h1, h2]
