/-
015_TreeProofs.lean

Goals:
- perform structural induction on binary trees;
- use one induction hypothesis for each recursive child;
- prove that transformations preserve structural measurements.
-/

inductive BTree (α : Type) where
  | empty
  | node (value : α) (left right : BTree α)
deriving Repr

def size {α : Type} : BTree α → Nat
  | .empty => 0
  | .node _ left right => 1 + size left + size right

def height {α : Type} : BTree α → Nat
  | .empty => 0
  | .node _ left right => 1 + max (height left) (height right)

def mirror {α : Type} : BTree α → BTree α
  | .empty => .empty
  | .node value left right => .node value (mirror right) (mirror left)

def countLeaves {α : Type} : BTree α → Nat
  | .empty => 0
  | .node _ .empty .empty => 1
  | .node _ left right => countLeaves left + countLeaves right

def mapTree {α β : Type} (f : α → β) : BTree α → BTree β
  | .empty => .empty
  | .node value left right => .node (f value) (mapTree f left) (mapTree f right)

theorem size_mirror (tree : BTree α) : size (mirror tree) = size tree := by
  induction tree with
  | empty => rfl
  | node value left right leftIH rightIH =>
      simp [mirror, size, leftIH, rightIH, Nat.add_comm, Nat.add_left_comm]

theorem height_mirror (tree : BTree α) : height (mirror tree) = height tree := by
  induction tree with
  | empty => rfl
  | node value left right leftIH rightIH =>
      simp [mirror, height, leftIH, rightIH, Nat.max_comm]

theorem mirror_mirror (tree : BTree α) : mirror (mirror tree) = tree := by
  induction tree with
  | empty => rfl
  | node value left right leftIH rightIH =>
      simp [mirror, leftIH, rightIH]

/-
Solved exercises

Exercise 1: define `countLeaves` and prove that mirroring preserves its result.
Exercise 2: define `mapTree` and prove that mapping preserves tree size.
Exercise 3: prove that a node with two empty children has height one.
Exercise 4: prove the defining size equation for a non-empty node.
-/

/- `countLeaves` has a special leaf pattern, so explicit case splitting after
   induction lets Lean expose the necessary empty/non-empty child shapes. -/
theorem countLeaves_mirror (tree : BTree α) :
    countLeaves (mirror tree) = countLeaves tree := by
  induction tree with
  | empty => rfl
  | node value left right leftIH rightIH =>
      cases left <;> cases right <;>
        simp_all [mirror, countLeaves, Nat.add_comm]

theorem size_mapTree (f : α → β) (tree : BTree α) :
    size (mapTree f tree) = size tree := by
  induction tree with
  | empty => rfl
  | node value left right leftIH rightIH =>
      simp [mapTree, size, leftIH, rightIH]

-- Unfolding computes both empty subtree heights to zero.
example (value : α) : height (BTree.node value .empty .empty) = 1 := by
  rfl

example (value : α) (left right : BTree α) :
    size (BTree.node value left right) = 1 + size left + size right := by
  rfl

/- Study notes:
- Tree induction supplies one hypothesis for `left` and one for `right`.
- Commutativity is needed when mirroring swaps the order of subtrees.
- A theorem true by unfolding a single definition is best proved with `rfl`.
-/
