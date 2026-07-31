(*
  004_Lists.v

  Goals:
  - use polymorphic lists;
  - define structurally recursive functions;
  - prove a list property by induction.
*)

From Coq Require Import List Arith Bool.
Import ListNotations.

Fixpoint sum_list (values : list nat) : nat :=
  match values with
  | [] => 0
  | value :: rest => value + sum_list rest
  end.

Fixpoint my_length {element_type : Type}
    (values : list element_type) : nat :=
  match values with
  | [] => 0
  | _ :: rest => 1 + my_length rest
  end.

Fixpoint my_map {input_type output_type : Type}
    (transform : input_type -> output_type)
    (values : list input_type) : list output_type :=
  match values with
  | [] => []
  | value :: rest => transform value :: my_map transform rest
  end.

Fixpoint snoc {element_type : Type}
    (values : list element_type) (last_value : element_type) : list element_type :=
  match values with
  | [] => [last_value]
  | value :: rest => value :: snoc rest last_value
  end.

Compute sum_list [1; 2; 3; 4].
Compute my_length [true; false; true].
Compute my_map (fun number => number + 1) [1; 2; 3].

Example sum_empty : sum_list [] = 0.
Proof.
  reflexivity.
Qed.

(* The induction hypothesis describes the shorter tail of the list. *)
Theorem length_snoc {element_type : Type}
    (values : list element_type) (last_value : element_type) :
  my_length (snoc values last_value) = my_length values + 1.
Proof.
  induction values as [| value rest induction_hypothesis].
  - reflexivity.
  - simpl.
    rewrite induction_hypothesis.
    reflexivity.
Qed.

(* Solved exercise: append two lists without using the library implementation. *)
Fixpoint my_append {element_type : Type}
    (left right : list element_type) : list element_type :=
  match left with
  | [] => right
  | value :: rest => value :: my_append rest right
  end.

Theorem append_empty_right {element_type : Type}
    (values : list element_type) : my_append values [] = values.
Proof.
  induction values as [| value rest induction_hypothesis].
  - reflexivity.
  - simpl.
    rewrite induction_hypothesis.
    reflexivity.
Qed.

(*
  Study notes:
  - `[]` and `::` are notation for the two list constructors.
  - `Fixpoint` accepts recursive calls on structurally smaller arguments.
  - List induction has an empty case and a head-and-tail case.
*)
