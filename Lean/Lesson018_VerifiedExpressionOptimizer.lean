/-!
Lesson018_VerifiedExpressionOptimizer.lean

Mini-project: a tiny arithmetic language with an optimizer.

Goals:
- separate syntax from semantics;
- implement a recursive program transformation;
- prove that optimization preserves the meaning of every expression.
-/

/- An expression is syntax: it describes a computation instead of performing it
   immediately. Variables are represented by numeric positions in an environment. -/
inductive Expr where
  | literal (value : Nat)
  | var (index : Nat)
  | add (left right : Expr)
  | multiply (left right : Expr)
deriving Repr, DecidableEq

-- An environment assigns a natural value to every variable index.
abbrev Environment := Nat → Nat

def Expr.evaluate (environment : Environment) : Expr → Nat
  | .literal value => value
  | .var index => environment index
  | .add left right => evaluate environment left + evaluate environment right
  | .multiply left right => evaluate environment left * evaluate environment right

/- The optimizer performs constant folding and removes neutral elements. Each
   recursive call optimizes a smaller subexpression before simplifying the root. -/
def Expr.optimize : Expr → Expr
  | .literal value => .literal value
  | .var index => .var index
  | .add left right =>
      match optimize left, optimize right with
      | .literal 0, optimizedRight => optimizedRight
      | optimizedLeft, .literal 0 => optimizedLeft
      | .literal a, .literal b => .literal (a + b)
      | optimizedLeft, optimizedRight => .add optimizedLeft optimizedRight
  | .multiply left right =>
      match optimize left, optimize right with
      | .literal 0, _ => .literal 0
      | _, .literal 0 => .literal 0
      | .literal 1, optimizedRight => optimizedRight
      | optimizedLeft, .literal 1 => optimizedLeft
      | .literal a, .literal b => .literal (a * b)
      | optimizedLeft, optimizedRight => .multiply optimizedLeft optimizedRight

def exampleExpression : Expr :=
  .multiply
    (.add (.literal 0) (.var 0))
    (.add (.literal 2) (.literal 3))

def exampleEnvironment : Environment
  | 0 => 7
  | _ => 0

#eval exampleExpression
#eval exampleExpression.optimize
#eval exampleExpression.evaluate exampleEnvironment
#eval exampleExpression.optimize.evaluate exampleEnvironment

/-
Verification exercise

Prove that `Expr.optimize` preserves evaluation for every expression and every
environment. The helper lemmas below first verify the local rewrite rules for
addition and multiplication; the final theorem combines them by structural
induction on the expression.
-/

/- Helper lemmas describe the behavior of the optimizer after its recursive
   results are already known. Separating them keeps the main induction readable. -/
theorem optimizeAdd_correct (environment : Environment) (left right : Expr) :
    Expr.evaluate environment
        (match left, right with
        | .literal 0, optimizedRight => optimizedRight
        | optimizedLeft, .literal 0 => optimizedLeft
        | .literal a, .literal b => .literal (a + b)
        | optimizedLeft, optimizedRight => .add optimizedLeft optimizedRight) =
      Expr.evaluate environment left + Expr.evaluate environment right := by
  cases left <;> cases right <;>
    simp only [Expr.evaluate] <;> split <;> simp_all [Expr.evaluate]

theorem optimizeMultiply_correct (environment : Environment) (left right : Expr) :
    Expr.evaluate environment
        (match left, right with
        | .literal 0, _ => .literal 0
        | _, .literal 0 => .literal 0
        | .literal 1, optimizedRight => optimizedRight
        | optimizedLeft, .literal 1 => optimizedLeft
        | .literal a, .literal b => .literal (a * b)
        | optimizedLeft, optimizedRight => .multiply optimizedLeft optimizedRight) =
      Expr.evaluate environment left * Expr.evaluate environment right := by
  cases left <;> cases right <;>
    simp only [Expr.evaluate] <;> split <;> simp_all [Expr.evaluate]

/- This is the project's correctness statement. It quantifies over every
   expression and every environment, rather than checking only selected tests. -/
theorem Expr.optimize_correct (expression : Expr) (environment : Environment) :
    (optimize expression).evaluate environment = expression.evaluate environment := by
  induction expression with
  | literal value => rfl
  | var index => rfl
  | add left right leftIH rightIH =>
      simp only [optimize, evaluate]
      rw [optimizeAdd_correct, leftIH, rightIH]
  | multiply left right leftIH rightIH =>
      simp only [optimize, evaluate]
      rw [optimizeMultiply_correct, leftIH, rightIH]

example :
    exampleExpression.optimize.evaluate exampleEnvironment =
      exampleExpression.evaluate exampleEnvironment := by
  apply Expr.optimize_correct

/- Study notes:
- `Expr` is an abstract syntax tree; `evaluate` gives it semantics.
- Tests cover examples, while `optimize_correct` covers every possible input.
- Proof structure follows program structure: induction follows recursive calls.
- Helper lemmas isolate local transformations from the global correctness proof.
-/
