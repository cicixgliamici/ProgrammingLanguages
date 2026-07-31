/-
003_PatternMatching.lean

Goals:
- understand `match`
- see pattern matching on `Nat` and `Bool`
- introduce custom inductive types
- understand constructors and exhaustive cases
-/

/-
`match` inspects how a value was constructed and selects the
corresponding branch.

General form:

  match value with
  | pattern₁ => result₁
  | pattern₂ => result₂

Lean checks that:

1. every pattern is compatible with the type of the value;
2. every branch returns the expected type;
3. all possible constructors are covered.

For executable definitions, pattern matching is compiled into branching
code similar to a decision tree. Internally, Lean elaborates matches
using the elimination principles of inductive types.
-/

-- Returns `true` if `n` is zero.
def isZero (n : Nat) : Bool :=
  match n with
  | 0 => true
  | _ => false

/-
`_` is a wildcard pattern.

It matches any value without giving that value a name.
Here it covers every natural number different from zero.
-/

#check isZero
-- isZero : Nat → Bool

#eval isZero 0
-- true

#eval isZero 5
-- false

/-
Natural numbers are an inductive type with two constructors:

  Nat.zero   : Nat
  Nat.succ   : Nat → Nat

Therefore, every natural number is either:

- zero;
- the successor of another natural number.
-/

-- Safe predecessor: `safePred 0 = 0`.
def safePred (n : Nat) : Nat :=
  match n with
  | 0 => 0
  | Nat.succ m => m

/-
In the second branch:

  Nat.succ m

matches a positive natural number and gives the predecessor the name `m`.

For example, `9` is represented conceptually as `Nat.succ 8`,
so `safePred 9` returns `8`.
-/

#check safePred
-- safePred : Nat → Nat

#eval safePred 0
-- 0

#eval safePred 9
-- 8

/-
An `inductive` declaration introduces a new type by listing
all the ways in which values of that type can be constructed.

Here, a value of type `Color` can only be one of three constructors:

  Color.red
  Color.green
  Color.blue

These constructors are values of type `Color`.
-/
inductive Color where
  | red
  | green
  | blue
deriving Repr, DecidableEq

/-
The `deriving` clause asks Lean to automatically generate useful
type-class instances.

- `Repr` allows values to be converted to a printable representation.
- `DecidableEq` allows equality between colors to be computed,
  for example with `==`.
-/

#check Color
-- Color : Type

#check Color.red
-- Color.red : Color

#check Color.green
-- Color.green : Color

/-
A function on an inductive type can inspect each constructor.

Because `Color` has exactly three constructors, the match must account
for `red`, `green`, and `blue`.
-/
def colorCode (c : Color) : Nat :=
  match c with
  | Color.red => 1
  | Color.green => 2
  | Color.blue => 3

#check colorCode
-- colorCode : Color → Nat

#eval colorCode Color.red
-- 1

#eval colorCode Color.blue
-- 3

-- `DecidableEq` makes computable equality available for `Color`.
#eval Color.green == Color.green
-- true

#eval Color.green == Color.red
-- false

/-
Boolean values also form an inductive type with two constructors:

  false : Bool
  true  : Bool

A Boolean function can therefore be defined by handling these two cases.
-/

-- Boolean negation written explicitly with pattern matching.
def myNot (b : Bool) : Bool :=
  match b with
  | true => false
  | false => true

#check myNot
-- myNot : Bool → Bool

#eval myNot true
-- false

#eval myNot false
-- true

/-
For simple functions, Lean also supports equation syntax.

The following definition is equivalent to the previous `match`:
-/
def myNot' : Bool → Bool
  | true => false
  | false => true

#eval myNot' true
-- false

/-
Important concepts:

- `match` inspects the constructor used to build a value.
- each `| pattern => result` line defines one branch;
- `_` matches any value without naming it;
- patterns can extract data contained inside constructors;
- Lean checks that pattern matching is exhaustive;
- all branches must return values of compatible types;
- `inductive` creates a type together with its constructors;
- `deriving` can automatically generate standard functionality.
-/

/-
Exercise 1

Define:

  isGreen : Color → Bool

Only the `green` constructor should produce `true`.
-/
def isGreen (c : Color) : Bool :=
  match c with
  | Color.green => true
  | _ => false

#check isGreen
-- isGreen : Color → Bool

#eval isGreen Color.green
-- true

#eval isGreen Color.red
-- false

/-
The same function could be written by listing every constructor explicitly.
-/
def isGreen' : Color → Bool
  | Color.red => false
  | Color.green => true
  | Color.blue => false

/-
Exercise 2

Define:

  natToBool : Nat → Bool

The result is `false` only for zero and `true` for every successor.
-/
def natToBool (n : Nat) : Bool :=
  match n with
  | 0 => false
  | Nat.succ _ => true

#check natToBool
-- natToBool : Nat → Bool

#eval natToBool 0
-- false

#eval natToBool 1
-- true

#eval natToBool 12
-- true

/-
Exercise 3

Define a type `Day` with seven constructors.

Since the constructors do not contain additional data, every value
of type `Day` is exactly one of these seven possibilities.
-/
inductive Day where
  | monday
  | tuesday
  | wednesday
  | thursday
  | friday
  | saturday
  | sunday
deriving Repr, DecidableEq

#check Day
-- Day : Type

#check Day.monday
-- Day.monday : Day

#eval Day.monday
-- Day.monday

#eval Day.saturday == Day.sunday
-- false

/-
A small additional function demonstrates pattern matching on `Day`.
-/
def isWeekend (day : Day) : Bool :=
  match day with
  | Day.saturday => true
  | Day.sunday => true
  | _ => false

#eval isWeekend Day.monday
-- false

#eval isWeekend Day.sunday
-- true
