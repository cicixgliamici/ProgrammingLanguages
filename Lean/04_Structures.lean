/-
Structures.lean

Goal:
- understand structure
- create records with named fields
- access fields
-/

structure Point where
  x : Nat
  y : Nat
deriving Repr

-- Create a point
def p1 : Point := { x := 3, y := 4 }

#eval p1.x
#eval p1.y

-- Function that sums the coordinates
def sumCoords (p : Point) : Nat :=
  p.x + p.y

#eval sumCoords p1

-- Structure representing a student
structure Student where
  name : String
  age : Nat
  passed : Bool
deriving Repr

def s1 : Student :=
  { name := "Luca", age := 23, passed := true }

#eval s1.name
#eval s1.age
#eval s1.passed

-- Function that updates one field
def birthday (s : Student) : Student :=
  { s with age := s.age + 1 }

#eval (birthday s1).age

/-
Things to notice:
- { x := ..., y := ... } creates a structure
- p.x accesses a field
- { s with age := ... } updates a record

Exercises:
1. Define a structure Book with title, pages, and available
2. Write a function isAdult : Student → Bool
3. Write a function moveRight : Point → Nat → Point
-/
