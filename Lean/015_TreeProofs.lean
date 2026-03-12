/-
015_TreeProofs.lean

Goal:
- prove basic properties about binary trees
- practice induction on custom inductive types
-/

inductive BTree (α : Type) where
  | empty : BTree α
  | node : α → BTree α → BTree α → BTree α
deriving Repr

def size : BTree α → Nat
  | BTree.empty => 0
  | BTree.node _ l r => 1 + size l + size r

def height : BTree α → Nat
  | BTree.empty => 0
  | BTree.node _ l r => 1 + max (height l) (height r)

def mirror : BTree α → BTree α
  | BTree.empty => BTree.empty
  | BTree.node x l r => BTree.node x (mirror r) (mirror l)

-- Mirror preserves size
theorem size_mirror (t : BTree α) : size (mirror t) = size t := by
  induction t with
  | empty =>
      rfl
  | node x l r ihl ihr =>
      simp [mirror, size, ihl, ihr, Nat.add_comm, Nat.add_left_comm, Nat.add_assoc]

-- Mirror preserves height
theorem height_mirror (t : BTree α) : height (mirror t) = height t := by
  induction t with
  | empty =>
      rfl
  | node x l r ihl ihr =>
      simp [mirror, height, ihl, ihr, max_comm]

-- Mirroring twice returns the original tree
theorem mirror_mirror (t : BTree α) : mirror (mirror t) = t := by
  induction t with
  | empty =>
      rfl
  | node x l r ihl ihr =>
      simp [mirror, ihl, ihr]

-- Basic examples
example : size (BTree.empty : BTree Nat) = 0 := rfl
example : height (BTree.empty : BTree Nat) = 0 := rfl
example : mirror (BTree.empty : BTree Nat) = BTree.empty := rfl

/-
Exercises:
1. Define countLeaves and prove: countLeaves (mirror t) = countLeaves t
2. Define mapTree and prove: size (mapTree f t) = size t
3. Prove: height (BTree.node x BTree.empty BTree.empty) = 1
4. Prove: size (BTree.node x l r) = 1 + size l + size r
-/
