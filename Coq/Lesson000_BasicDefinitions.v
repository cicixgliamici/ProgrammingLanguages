(**
  Lesson000_BasicDefinitions.v

  Goals:
  - define constants and functions;
  - read explicit type annotations;
  - evaluate closed expressions.
*)

From Coq Require Import Arith Bool String.

(* A definition associates a name with a term and its type. *)
Definition my_number : nat := 7.

Definition add_one (number : nat) : nat :=
  number + 1.

Definition add (left right : nat) : nat :=
  left + right.

Definition negate_bool (value : bool) : bool :=
  negb value.

(* Functions are values. This definition has a function type. *)
Definition double : nat -> nat :=
  fun number => number * 2.

Check my_number.
Check add_one.
Check add.
Check double.

Compute add_one 5.
Compute add 3 4.
Compute negate_bool true.
Compute double 6.

(* Solved exercises. *)

Definition triple (number : nat) : nat :=
  number * 3.

Definition is_five (number : nat) : bool :=
  Nat.eqb number 5.

Definition maximum (left right : nat) : nat :=
  Nat.max left right.

Example triple_four : triple 4 = 12.
Proof.
  reflexivity.
Qed.

(*
  Study notes:
  - Every command ends with a period.
  - `Check` displays a type; `Compute` reduces and prints an expression.
  - `reflexivity` proves equalities that become identical by computation.
*)
