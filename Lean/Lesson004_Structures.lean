/-!
Lesson004_Structures.lean

Goals:
- understand `structure`
- create records with named fields
- access fields
- update existing records
-/

/-
A `structure` defines a new type whose values contain several
named pieces of data, called fields.

General form:

  structure TypeName where
    field₁ : Type₁
    field₂ : Type₂

Lean automatically generates:

- a constructor used to create values;
- one projection function for each field.

Structures are implemented as inductive types with one constructor.
Field access and record notation are convenient syntax built on top
of that representation.
-/

structure Point where
  x : Nat
  y : Nat
deriving Repr

/-
The declaration above creates:

  Point       : Type
  Point.mk    : Nat → Nat → Point
  Point.x     : Point → Nat
  Point.y     : Point → Nat

`Point.mk` is the constructor, while `Point.x` and `Point.y`
are field projection functions.
-/

#check Point
-- Point : Type

#check Point.mk
-- Point.mk : Nat → Nat → Point

#check Point.x
-- Point.x : Point → Nat

#check Point.y
-- Point.y : Point → Nat

/-
`deriving Repr` asks Lean to generate a printable representation
for values of type `Point`.

This allows commands such as:

  #eval p1

to display the entire structure.
-/

-- Create a point using record notation.
def p1 : Point :=
  { x := 3, y := 4 }

/-
Record notation:

  { x := 3, y := 4 }

is convenient syntax for constructing a `Point`.

It is equivalent to:

  Point.mk 3 4
-/

def p2 : Point :=
  Point.mk 10 20

#eval p1
-- { x := 3, y := 4 }

#eval p1.x
-- 3

#eval p1.y
-- 4

/-
The notation:

  p1.x

accesses the field `x`.

It is equivalent to applying the projection function:

  Point.x p1
-/

#eval Point.x p1
-- 3

-- Function that sums the coordinates.
def sumCoords (p : Point) : Nat :=
  p.x + p.y

#check sumCoords
-- sumCoords : Point → Nat

#eval sumCoords p1
-- 7

/-
When compiled, field access becomes a projection from the structure.

Since the shape of a structure is known statically, Lean can compile
operations such as `p.x` into efficient access to the corresponding
stored value.
-/

/-
A structure can contain fields of different types.
-/

structure Student where
  name : String
  age : Nat
  passed : Bool
deriving Repr

/-
A `Student` contains:

- a `String`;
- a natural number;
- a Boolean value.

Lean checks that every field receives a value of the declared type.
-/

#check Student
-- Student : Type

#check Student.mk
-- Student.mk : String → Nat → Bool → Student

def s1 : Student :=
  { name := "Luca", age := 23, passed := true }

#eval s1
-- { name := "Luca", age := 23, passed := true }

#eval s1.name
-- "Luca"

#eval s1.age
-- 23

#eval s1.passed
-- true

/-
Record update syntax creates a new structure from an existing one.

General form:

  { oldValue with field := newValue }

Structures are immutable: the original value is not modified.
Instead, Lean creates a new value, copying unchanged fields and
replacing the specified ones.
-/

-- Return a new student whose age is increased by one.
def birthday (s : Student) : Student :=
  { s with age := s.age + 1 }

#eval birthday s1
-- { name := "Luca", age := 24, passed := true }

#eval (birthday s1).age
-- 24

-- The original student is unchanged.
#eval s1.age
-- 23

/-
Parentheses are needed in:

  (birthday s1).age

because we first evaluate `birthday s1` and then access the field
of the resulting structure.
-/

/-
Multiple fields can be updated at the same time.
-/
def markAsPassed (s : Student) : Student :=
  { s with passed := true }

def renameStudent (s : Student) (newName : String) : Student :=
  { s with name := newName }

#eval renameStudent s1 "Marco"
-- { name := "Marco", age := 23, passed := true }

/-
Important concepts:

- `structure` defines a record-like type with named fields;
- record notation creates a value by assigning its fields;
- `value.field` accesses a field;
- field access is syntactic sugar for a projection function;
- `{ value with field := ... }` creates an updated copy;
- structures are immutable;
- `deriving Repr` makes values printable with `#eval`;
- Lean checks all field names and field types during elaboration.
-/

/-
Exercise 1

Define a structure `Book` with:

- `title : String`
- `pages : Nat`
- `available : Bool`
-/
structure Book where
  title : String
  pages : Nat
  available : Bool
deriving Repr

def book1 : Book :=
  {
    title := "The Little Prince"
    pages := 96
    available := true
  }

#check Book
-- Book : Type

#check Book.mk
-- Book.mk : String → Nat → Bool → Book

#eval book1
-- { title := "The Little Prince", pages := 96, available := true }

#eval book1.title
-- "The Little Prince"

#eval book1.pages
-- 96

#eval book1.available
-- true

/-
Exercise 2

Define:

  isAdult : Student → Bool

The result is `true` when the student's age is at least 18.

The expression:

  decide (18 ≤ s.age)

converts the decidable proposition `18 ≤ s.age` into a `Bool`.
-/
def isAdult (s : Student) : Bool :=
  decide (18 ≤ s.age)

#check isAdult
-- isAdult : Student → Bool

#eval isAdult s1
-- true

def youngStudent : Student :=
  { name := "Anna", age := 16, passed := false }

#eval isAdult youngStudent
-- false

/-
An alternative version uses a Boolean comparison directly.
-/
def isAdult' (s : Student) : Bool :=
  s.age >= 18

#eval isAdult' s1
-- true

/-
Exercise 3

Define:

  moveRight : Point → Nat → Point

The function increases the `x` coordinate while leaving `y`
unchanged.
-/
def moveRight (p : Point) (distance : Nat) : Point :=
  { p with x := p.x + distance }

#check moveRight
-- moveRight : Point → Nat → Point

#eval moveRight p1 5
-- { x := 8, y := 4 }

#eval (moveRight p1 5).x
-- 8

#eval (moveRight p1 5).y
-- 4

/-
The same function can be written by explicitly rebuilding the point.
-/
def moveRight' (p : Point) (distance : Nat) : Point :=
  {
    x := p.x + distance
    y := p.y
  }

#eval moveRight' p1 5
-- { x := 8, y := 4 }
