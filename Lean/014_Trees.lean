/-
014_Trees.lean

Goal:
- define a binary tree
- write recursive functions on trees
- practice structural recursion
-/

inductive BTree (α : Type) where
  | empty : BTree α
  | node : α → BTree α → BTree α → BTree α
deriving Repr

-- Example trees
def tree1 : BTree Nat :=
  BTree.node 10
    (BTree.node 5 BTree.empty BTree.empty)
    (BTree.node 20 BTree.empty BTree.empty)

def tree2 : BTree Nat :=
  BTree.node 1
    (BTree.node 2
      (BTree.node 3 BTree.empty BTree.empty)
      BTree.empty)
    BTree.empty

-- Number of nodes
def size : BTree α → Nat
  | BTree.empty => 0
  | BTree.node _ l r => 1 + size l + size r

#eval size tree1
#eval size tree2

-- Height of the tree
def height : BTree α → Nat
  | BTree.empty => 0
  | BTree.node _ l r => 1 + max (height l) (height r)

#eval height tree1
#eval height tree2

-- Number of leaves, counting only non-empty leaves
def countLeaves : BTree α → Nat
  | BTree.empty => 0
  | BTree.node _ BTree.empty BTree.empty => 1
  | BTree.node _ l r => countLeaves l + countLeaves r

#eval countLeaves tree1
#eval countLeaves tree2

-- Mirror the tree
def mirror : BTree α → BTree α
  | BTree.empty => BTree.empty
  | BTree.node x l r => BTree.node x (mirror r) (mirror l)

#eval mirror tree1

-- Inorder traversal
def inorder : BTree α → List α
  | BTree.empty => []
  | BTree.node x l r => inorder l ++ [x] ++ inorder r

#eval inorder tree1
#eval inorder tree2

-- Preorder traversal
def preorder : BTree α → List α
  | BTree.empty => []
  | BTree.node x l r => [x] ++ preorder l ++ preorder r

#eval preorder tree1

-- Postorder traversal
def postorder : BTree α → List α
  | BTree.empty => []
  | BTree.node x l r => postorder l ++ postorder r ++ [x]

#eval postorder tree1

/-
Exercises:
1. Define countEmpty : BTree α → Nat
2. Define contains [DecidableEq α] : α → BTree α → Bool
3. Define mapTree : (α → β) → BTree α → BTree β
4. Define treeSum : BTree Nat → Nat
5. Prove: size BTree.empty = 0
-/
