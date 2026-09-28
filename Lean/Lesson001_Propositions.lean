/-!
Lesson001_Propositions.lean

Goals:
- understand that propositions are types
- understand that proofs are values
- use `example`
- write first proof terms
- use `intro`, `exact`, and `rfl`
-/

/-
In Lean, a proposition is an expression whose type is `Prop`.

Examples of propositions:

  2 = 2
  p → q
  ∀ n : Nat, n = n

According to the propositions-as-types interpretation:

- a proposition is a type;
- a proof of that proposition is a value of that type.

Lean accepts a theorem only when its proof term has the required type.
The kernel checks the final proof term independently.
-/

/-
`example` declares and checks a proposition together with its proof.

Unlike `def` or `theorem`, an `example` does not introduce a reusable
name in the environment. It is commonly used for demonstrations,
experiments, and exercises.

General form:

  example : Proposition :=
    proof
-/

-- `rfl` is a proof of reflexive equality: every value equals itself.
example : 2 = 2 :=
  rfl

example : true = true :=
  rfl

/-
`p`, `q`, and `r` are arbitrary propositions.

Writing:

  variable (p q r : Prop)

means that later examples may depend on any propositions named
`p`, `q`, and `r`.
-/
variable (p q r : Prop)

/-
A proof of `p → p` is a function that:

1. receives a proof of `p`;
2. returns that same proof.

`by` starts tactic mode.

`intro hp` introduces the assumption `p` into the local context
and names its proof `hp`.

`exact hp` closes the current goal because `hp` has exactly
the required type.
-/
example : p → p := by
  intro hp
  exact hp

/-
Implication associates to the right:

  p → q → p

means:

  p → (q → p)

The proof receives a proof of `p`, then a proof of `q`,
and finally returns the proof of `p`.
-/
example : p → q → p := by
  intro hp
  intro hq
  exact hp

-- Here the final goal is `q`, so we return the hypothesis `hq`.
example : p → q → q := by
  intro hp
  intro hq
  exact hq

/-
`hpq` is a proof of `p → q`, so it behaves like a function
from proofs of `p` to proofs of `q`.

Applying `hpq` to `hp` produces a proof of `q`.
-/
example : (p → q) → p → q := by
  intro hpq
  intro hp
  exact hpq hp

/-
The universal quantifier also behaves like a function type.

To prove:

  ∀ n : Nat, n = n

we introduce an arbitrary natural number `n` and prove `n = n`.
-/
example : ∀ n : Nat, n = n := by
  intro n
  rfl

/-
The proof above can also be written directly as a proof term.

The anonymous function receives `n`, and `rfl` proves `n = n`.
-/
example : ∀ n : Nat, n = n :=
  fun n => rfl

/-
Important commands and tactics:

- `example` asks Lean to elaborate and verify an unnamed declaration.
- `by` starts a tactic block that constructs a proof term.
- `intro` introduces an implication hypothesis or a universally
  quantified variable.
- `exact` closes the goal with a term of exactly the required type.
- `rfl` proves an equality whose two sides reduce to the same expression.

Tactics are not an alternative proof system. They construct proof terms,
which are then checked by Lean's kernel.

Proofs in `Prop` are generally erased from executable code because they
are used for verification rather than runtime computation.
-/

/-
Exercise 1

Prove:

  q → p → q

The proof receives a proof of `q`, then a proof of `p`,
and returns the original proof of `q`.
-/
example : q → p → q := by
  intro hq
  intro hp
  exact hq

/-
The same proof written directly as a function.
-/
example : q → p → q :=
  fun hq hp => hq

/-
Exercise 2

Prove:

  (p → q) → (q → r) → p → r

The hypotheses form a chain:

  p → q
  q → r

Starting from a proof of `p`, we obtain a proof of `q`,
and then a proof of `r`.
-/
example : (p → q) → (q → r) → p → r := by
  intro hpq
  intro hqr
  intro hp
  exact hqr (hpq hp)

/-
The same proof can be written in smaller intermediate steps.
-/
example : (p → q) → (q → r) → p → r := by
  intro hpq
  intro hqr
  intro hp
  have hq : q := hpq hp
  have hr : r := hqr hq
  exact hr

/-
Direct proof-term version.

This is ordinary function composition applied to proofs.
-/
example : (p → q) → (q → r) → p → r :=
  fun hpq hqr hp => hqr (hpq hp)
