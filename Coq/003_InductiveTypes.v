(*
  003_InductiveTypes.v

  Goals:
  - define a custom inductive type;
  - write exhaustive pattern matches;
  - prove a theorem by case analysis.
*)

From Coq Require Import Bool.

Inductive day : Type :=
  | Monday
  | Tuesday
  | Wednesday
  | Thursday
  | Friday
  | Saturday
  | Sunday.

Definition is_weekend (value : day) : bool :=
  match value with
  | Saturday | Sunday => true
  | _ => false
  end.

Definition next_day (value : day) : day :=
  match value with
  | Monday => Tuesday
  | Tuesday => Wednesday
  | Wednesday => Thursday
  | Thursday => Friday
  | Friday => Saturday
  | Saturday => Sunday
  | Sunday => Monday
  end.

Definition previous_day (value : day) : day :=
  match value with
  | Monday => Sunday
  | Tuesday => Monday
  | Wednesday => Tuesday
  | Thursday => Wednesday
  | Friday => Thursday
  | Saturday => Friday
  | Sunday => Saturday
  end.

Compute is_weekend Sunday.
Compute next_day Friday.

(* The seven branches correspond exactly to the seven constructors of `day`. *)
Theorem previous_after_next (value : day) :
  previous_day (next_day value) = value.
Proof.
  destruct value.
  - reflexivity.
  - reflexivity.
  - reflexivity.
  - reflexivity.
  - reflexivity.
  - reflexivity.
  - reflexivity.
Qed.

(* A polymorphic result can carry either a successful value or an error. *)
Inductive result (value_type : Type) : Type :=
  | Success : value_type -> result value_type
  | Failure : result value_type.

Arguments Success {value_type} value.
Arguments Failure {value_type}.

Definition get_or_else {value_type : Type}
    (default : value_type) (possible_value : result value_type) : value_type :=
  match possible_value with
  | Success value => value
  | Failure => default
  end.

Compute get_or_else 0 (Success 10).
Compute get_or_else 0 Failure.

(*
  Study notes:
  - Constructors are the only ways to create values of an inductive type.
  - A `match` must handle every possible constructor.
  - `destruct` brings the same case analysis into a proof.
*)
