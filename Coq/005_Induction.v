(*
  005_Induction.v

  Goals:
  - connect recursive programs with inductive proofs;
  - identify base and successor cases;
  - use standard arithmetic lemmas when computation is insufficient.
*)

From Coq Require Import Arith.

Fixpoint factorial (number : nat) : nat :=
  match number with
  | 0 => 1
  | S smaller => number * factorial smaller
  end.

Fixpoint double (number : nat) : nat :=
  match number with
  | 0 => 0
  | S smaller => S (S (double smaller))
  end.

Fixpoint sum_to (number : nat) : nat :=
  match number with
  | 0 => 0
  | S smaller => sum_to smaller + S smaller
  end.

Compute factorial 5.
Compute double 4.
Compute sum_to 5.

Theorem sum_to_zero : sum_to 0 = 0.
Proof.
  reflexivity.
Qed.

Theorem sum_to_successor (number : nat) :
  sum_to (S number) = sum_to number + S number.
Proof.
  reflexivity.
Qed.

(* The proof follows the same zero/successor structure as `double`. *)
Theorem double_is_addition (number : nat) :
  double number = number + number.
Proof.
  induction number as [| smaller induction_hypothesis].
  - reflexivity.
  - simpl.
    rewrite induction_hypothesis.
    rewrite Nat.add_succ_r.
    reflexivity.
Qed.

(* A theorem may reuse another theorem instead of repeating its induction. *)
Theorem double_successor (number : nat) :
  double (S number) = S (S (double number)).
Proof.
  reflexivity.
Qed.

(*
  Study notes:
  - `induction` creates one goal for each constructor of the input.
  - The successor case receives a hypothesis about the smaller number.
  - Prefer `reflexivity` for computation and named lemmas for algebraic laws.
*)
