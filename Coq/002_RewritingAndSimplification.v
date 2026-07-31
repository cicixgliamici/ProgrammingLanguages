(*
  002_RewritingAndSimplification.v

  Goals:
  - rewrite with equality hypotheses;
  - distinguish computation from rewriting;
  - use standard arithmetic lemmas.
*)

From Coq Require Import Arith Bool.

Theorem add_equal_values (left right : nat) :
  left = right -> left + 1 = right + 1.
Proof.
  intro values_are_equal.
  rewrite values_are_equal.
  reflexivity.
Qed.

Theorem equality_is_transitive (a b c : nat) :
  a = b -> b = c -> a = c.
Proof.
  intros a_equals_b b_equals_c.
  rewrite a_equals_b.
  exact b_equals_c.
Qed.

(* `simpl` performs definitional computation but does not prove every law. *)
Theorem zero_plus_number (number : nat) : 0 + number = number.
Proof.
  simpl.
  reflexivity.
Qed.

(* Addition recurses on its left argument, so right-zero needs induction. *)
Theorem number_plus_zero (number : nat) : number + 0 = number.
Proof.
  induction number as [| smaller induction_hypothesis].
  - reflexivity.
  - simpl.
    rewrite induction_hypothesis.
    reflexivity.
Qed.

Theorem double_negation_bool (value : bool) :
  negb (negb value) = value.
Proof.
  destruct value.
  - reflexivity.
  - reflexivity.
Qed.

(* Solved exercises. *)

Theorem multiply_equal_values (left right : nat) :
  left = right -> left * 2 = right * 2.
Proof.
  intro values_are_equal.
  rewrite values_are_equal.
  reflexivity.
Qed.

Theorem add_two_equalities (a b c d : nat) :
  a = b -> c = d -> a + c = b + d.
Proof.
  intros a_equals_b c_equals_d.
  rewrite a_equals_b.
  rewrite c_equals_d.
  reflexivity.
Qed.

(*
  Study notes:
  - `rewrite H` substitutes using equality `H`; `rewrite <- H` reverses it.
  - `simpl` unfolds reducible definitions and evaluates pattern matches.
  - Induction is needed when a property follows the recursive shape of data.
*)
