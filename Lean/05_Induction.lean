/-
Induction.lean

Goal:
- understand induction
- prove properties on natural numbers
- see a recursive function
-/

-- Recursive function: factorial
def fact : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fact n

#eval fact 0
#eval fact 1
#eval fact 5

-- Simple proof by induction
example (n : Nat) : n + 0 = n := by
  induction n with
  | zero =>
      rfl
  | succ n ih =>
      simp [Nat.succ_eq_add_one, ih]

-- Another classic property
example (n : Nat) : 0 + n = n := by
  simp

-- Double defined recursively
def myDouble : Nat → Nat
  | 0 => 0
  | n + 1 => myDouble n + 2

#eval myDouble 0
#eval myDouble 4

-- Property of myDouble
example (n : Nat) : myDouble n = 2 * n := by
  induction n with
  | zero =>
      rfl
  | succ n ih =>
      simp [myDouble, ih, Nat.mul_add, Nat.add_assoc, Nat.add_left_comm, Nat.add_comm]

/-
Exercises:
1. Define sumTo : Nat → Nat, computing 0 + 1 + ... + n
2. Prove by induction that sumTo 0 = 0
3. Prove a simple property about one of your recursive functions
-/
