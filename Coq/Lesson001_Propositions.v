(**
  Lesson001_Propositions.v

  Goals:
  - understand propositions as types;
  - prove implications, conjunctions, and disjunctions;
  - see a proof as a term checked by the kernel.
*)

Section PropositionalLogic.

Variables p q r : Prop.

Theorem identity : p -> p.
Proof.
  intro proof_of_p.
  exact proof_of_p.
Qed.

(* An implication is used like a function from one proof to another. *)
Theorem compose_implications :
  (p -> q) -> (q -> r) -> p -> r.
Proof.
  intros p_implies_q q_implies_r proof_of_p.
  apply q_implies_r.
  apply p_implies_q.
  exact proof_of_p.
Qed.

Theorem build_conjunction : p -> q -> p /\ q.
Proof.
  intros proof_of_p proof_of_q.
  split.
  - exact proof_of_p.
  - exact proof_of_q.
Qed.

Theorem use_conjunction : p /\ q -> q.
Proof.
  intros [_ proof_of_q].
  exact proof_of_q.
Qed.

Theorem choose_disjunction : p -> p \/ q.
Proof.
  intro proof_of_p.
  left.
  exact proof_of_p.
Qed.

(* Consuming a disjunction requires handling both possible constructors. *)
Theorem use_disjunction : (p -> r) -> (q -> r) -> p \/ q -> r.
Proof.
  intros p_implies_r q_implies_r either_p_or_q.
  destruct either_p_or_q as [proof_of_p | proof_of_q].
  - exact (p_implies_r proof_of_p).
  - exact (q_implies_r proof_of_q).
Qed.

(* Solved exercises. *)

Theorem and_commutative : p /\ q -> q /\ p.
Proof.
  intros [proof_of_p proof_of_q].
  split.
  - exact proof_of_q.
  - exact proof_of_p.
Qed.

Theorem contrapositive : (p -> q) -> (~ q -> ~ p).
Proof.
  intros p_implies_q not_q proof_of_p.
  apply not_q.
  apply p_implies_q.
  exact proof_of_p.
Qed.

End PropositionalLogic.

(*
  Study notes:
  - `intro` moves an implication premise into the context.
  - `split` constructs a conjunction; `left` and `right` choose a disjunction.
  - `destruct` examines which constructor produced an available proof.
  - `Qed` closes the proof and asks the kernel to check its proof term.
*)
