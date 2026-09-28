/-!
Lesson014_Trees.lean

Goals:
- model recursive branching data;
- write structurally recursive tree traversals;
- distinguish size, height, leaves, and empty children.
-/

inductive BTree (α : Type) where
  | empty
  | node (value : α) (left right : BTree α)
deriving Repr

def tree1 : BTree Nat :=
  .node 10 (.node 5 .empty .empty) (.node 20 .empty .empty)

def tree2 : BTree Nat :=
  .node 1 (.node 2 (.node 3 .empty .empty) .empty) .empty

def size {α : Type} : BTree α → Nat
  | .empty => 0
  | .node _ left right => 1 + size left + size right

def height {α : Type} : BTree α → Nat
  | .empty => 0
  | .node _ left right => 1 + max (height left) (height right)

def countLeaves {α : Type} : BTree α → Nat
  | .empty => 0
  | .node _ .empty .empty => 1
  | .node _ left right => countLeaves left + countLeaves right

def mirror {α : Type} : BTree α → BTree α
  | .empty => .empty
  | .node value left right => .node value (mirror right) (mirror left)

def inorder {α : Type} : BTree α → List α
  | .empty => []
  | .node value left right => inorder left ++ [value] ++ inorder right

def preorder {α : Type} : BTree α → List α
  | .empty => []
  | .node value left right => [value] ++ preorder left ++ preorder right

def postorder {α : Type} : BTree α → List α
  | .empty => []
  | .node value left right => postorder left ++ postorder right ++ [value]

/-
Solved exercises

Exercise 1: define `countEmpty : BTree α → Nat`.
Exercise 2: define `contains : α → BTree α → Bool` for comparable values.
Exercise 3: define `mapTree : (α → β) → BTree α → BTree β`.
Exercise 4: define `treeSum : BTree Nat → Nat`.
Exercise 5: prove that the size of an empty tree is zero.
-/

-- Every node has two child positions, including positions containing `empty`.
def countEmpty {α : Type} : BTree α → Nat
  | .empty => 1
  | .node _ left right => countEmpty left + countEmpty right

-- `[BEq α]` keeps the traversal generic while providing Boolean equality.
def contains {α : Type} [BEq α] (wanted : α) : BTree α → Bool
  | .empty => false
  | .node value left right =>
      value == wanted || contains wanted left || contains wanted right

def mapTree {α β : Type} (f : α → β) : BTree α → BTree β
  | .empty => .empty
  | .node value left right => .node (f value) (mapTree f left) (mapTree f right)

-- Empty subtrees contribute zero, while nodes add their value and both sums.
def treeSum : BTree Nat → Nat
  | .empty => 0
  | .node value left right => value + treeSum left + treeSum right

example : size (BTree.empty : BTree Nat) = 0 := by
  rfl

#eval size tree1
#eval height tree2
#eval inorder tree1
#eval contains 20 tree1
#eval treeSum tree1

/- Study notes:
- Structural recursion makes one recursive call for each recursive child.
- Traversal order is determined only by where the root value is placed.
- `BEq α` supplies executable boolean equality for values of type `α`.
-/
