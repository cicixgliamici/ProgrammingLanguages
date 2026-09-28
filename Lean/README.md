# Learning Lean 4

This directory provides a progressive introduction to functional programming,
formal reasoning, and verified transformations in Lean 4. It starts with small
definitions and propositions, then develops recursion, inductive data, reusable
proof patterns, dependent types, and a verified expression optimizer.

The material is designed to be readable during a technical review. Each lesson
is self-contained, uses explicit names, explains important decisions, and keeps
the exercise statement next to its solution. Files can be checked individually
and are intended to be studied in numeric order.

## Learning objectives

After completing the sequence, a reader should be able to:

- read and write typed functional programs in Lean;
- model data with structures, products, sums, and inductive types;
- define terminating functions through structural recursion;
- understand propositions as types and proofs as values;
- construct proofs with terms and common tactics;
- prove properties by induction over natural numbers, lists, and trees;
- use typeclasses to express generic capabilities;
- recognize how dependent types move invariants into signatures;
- verify that a program transformation preserves program meaning.

## What Lean is

Lean 4 is both a functional programming language and an interactive theorem
prover. The same type system checks executable definitions and mathematical
proofs:

```lean
def double (number : Nat) : Nat :=
  number * 2

theorem double_zero : double 0 = 0 := by
  rfl
```

`double` is a program. `double_zero` is a value whose type states the property
being proved. Lean's kernel checks that the generated proof term really has
that type.

This is the computational perspective behind the Curry–Howard correspondence:

- a proposition is a type;
- a proof is a value of that type;
- `p → q` is a function from evidence for `p` to evidence for `q`;
- `p ∧ q` contains evidence for both propositions;
- `p ∨ q` contains evidence for one alternative, identified by a constructor;
- `¬p` is notation for `p → False`.

Lean relies heavily on inductive types. Natural numbers, lists, `Option`, and
the custom trees in this directory are all described by constructors. Pattern
matching handles every possible constructor, while structural recursion makes
recursive calls on smaller pieces of data. This structure gives Lean enough
information to check termination.

## Prerequisites

The early lessons require only basic programming knowledge. Familiarity with
functions, recursion, and algebraic data types is useful but not mandatory.
No previous theorem-proving experience is assumed.

Recommended tools:

- [Lean 4](https://lean-lang.org/);
- Elan, the Lean toolchain manager;
- Visual Studio Code with the **Lean 4** extension;
- Lake when working with package-based Lean projects.

The official installation guide recommends installing Elan so each project can
select its required Lean toolchain automatically.

## Repository contents

| File | Main topic | Key ideas |
| --- | --- | --- |
| `Lesson000_BasicDefs.lean` | Basic definitions | Types, functions, evaluation, local bindings |
| `Lesson001_Propositions.lean` | Propositions | Implication, conjunction, disjunction, negation |
| `Lesson002_RewritingAndSimp.lean` | Equality reasoning | `rw`, `simp`, definitional equality |
| `Lesson003_PatternMatching.lean` | Pattern matching | Constructors, exhaustive cases, recursion |
| `Lesson004_Structures.lean` | Structures | Records, projections, immutable updates |
| `Lesson005_Induction.lean` | Natural-number induction | Base cases, inductive steps, hypotheses |
| `Lesson006_Lists.lean` | Lists | Structural recursion, map, append, length |
| `Lesson007_LogicExercises1.lean` | Logic exercises | Proof construction and case analysis |
| `Lesson007a_Solved.lean` | Alternative solutions | Longer tactic proofs with visible steps |
| `Lesson008_CustomInductiveTypes.lean` | Custom data | Enumerations, options, recursive trees |
| `Lesson009_TacticsCheatsheet.lean` | Tactic reference | Common tactics and when to use them |
| `Lesson010_OptionAndErrorHandling.lean` | Safe partial functions | `Option`, mapping, binding, explicit failure |
| `Lesson011_ProductSumTypes.lean` | Products and sums | Pairs, alternatives, eliminators |
| `Lesson012_MoreLists.lean` | List processing | Filter, take, drop, zip, folds |
| `Lesson013_ListProofs.lean` | List proofs | Helper lemmas and structural induction |
| `Lesson014_Trees.lean` | Binary trees | Traversals, mapping, size, height |
| `Lesson015_TreeProofs.lean` | Tree proofs | Invariants preserved by recursive functions |
| `Lesson016_TypeclassesAndGenericCode.lean` | Typeclasses | Instances, capability constraints, generic APIs |
| `Lesson017_DependentVectors.lean` | Dependent types | Length-indexed lists and safe indexing with `Fin` |
| `Lesson018_VerifiedExpressionOptimizer.lean` | Verification project | Syntax, semantics, optimization, correctness |

## Suggested study path

The sequence is divided into five stages:

1. **Foundations (`000`–`004`)** — Learn Lean syntax, propositions, rewriting,
   pattern matching, and structures.
2. **Recursion and logic (`005`–`009`)** — Connect recursive definitions with
   induction and practice constructing logical proofs.
3. **Reusable data patterns (`010`–`012`)** — Work with optional values, sums,
   products, and standard list-processing patterns.
4. **Structural proofs (`013`–`015`)** — Prove properties that follow the shape
   of recursive lists and trees.
5. **Advanced guarantees (`016`–`018`)** — Explore generic programming,
   dependent types, and end-to-end verification of an optimizer.

The numbering expresses a recommended order, not a strict dependency graph.
Most files repeat the definitions they need so that a reader can open one
lesson without first building a large project.

## How to work through a lesson

A productive workflow is:

1. Read the goals and explanatory comments at the top of the file.
2. Predict the type or output of each definition before using `#check` or
   `#eval`.
3. Hide a solved exercise and reconstruct it independently.
4. Inspect the goal state after each tactic in the editor.
5. Compare the attempted solution with the provided one.
6. Replace broad automation with a more explicit proof when doing so reveals
   the underlying idea.
7. Change an example and observe which definitions or proofs must change.

For proofs that use `simp`, `simp?` can suggest a smaller and more explicit set
of simplification lemmas. The suggestion is worth reading rather than accepting
mechanically: it explains which facts actually close the goal.

## Commands inside Lean files

The lessons use development commands to make types and computations visible:

```lean
def square (number : Nat) : Nat :=
  number * number

#check square
#eval square 5

example (number : Nat) : number = number := by
  rfl
```

- `#check expression` reports the inferred type without running the program.
- `#eval expression` evaluates an expression and prints its result.
- `example` checks a declaration without adding a public theorem name.
- `#synth Capability Type` asks Lean to display the selected typeclass instance.

These commands help explore a file, but they are not part of the returned value
of a function.

## Checking the lessons

From the repository root, a standalone lesson can be checked with:

```powershell
lake env lean .\Lean\Lesson005_Induction.lean
```

On macOS or Linux, the equivalent command is:

```bash
lake env lean ./Lean/Lesson005_Induction.lean
```

If the command exits without an error, Lean accepted every definition and proof
in that file. Any `#eval` command will also print its result.

The repository is a Lake package. Every lesson is built as an independent
module so repeated teaching definitions in different lessons do not collide.
Check the complete track from the repository root with:

```powershell
lake build
lake env lean .\Lean\Lesson005_Induction.lean
```

`lake build` checks every lesson incrementally. `lake env lean` invokes Lean in
the pinned workspace environment when checking one file directly.

## Elan and reproducible toolchains

Elan installs and selects Lean toolchains. Useful commands include:

```powershell
elan --version
elan show
elan toolchain list
elan default stable
elan update
```

A package can pin a toolchain in a `lean-toolchain` file:

```text
leanprover/lean4:v4.x.y
```

Replace `v4.x.y` with the version chosen for the project. Pinning the toolchain
helps keep builds reproducible because compiler and standard-library changes do
not silently alter proof behavior.

If `lean` or `lake` reports that no default toolchain is configured, install or
select one with Elan before checking the lessons.

## Lake and larger projects

Lake is Lean's standard build tool and package manager. It configures builds,
tracks dependencies, builds libraries and executables, and supports project
workflows such as tests and linters.

A typical package contains:

- `lean-toolchain`, selecting the Lean version;
- `lakefile.toml` or `lakefile.lean`, declaring targets and dependencies;
- `lake-manifest.json`, recording resolved dependency revisions;
- `.lake/`, containing downloaded packages and generated build artifacts;
- source modules, imported using names such as `Geometry.Point`.

Common commands are:

```powershell
lake new MyLeanProject
cd MyLeanProject
lake build
lake update
lake exe executableName
lake lean .\MyLeanProject.lean
```

For example, a file at `Geometry/Point.lean` is normally imported with
`import Geometry.Point`. Lake configures the module search paths and performs
incremental builds when files or dependencies change.

## Elaboration, kernel checking, and execution

Lean processes a source file through several conceptually distinct stages:

1. The parser turns source text into syntax.
2. The elaborator resolves names, notation, implicit arguments, coercions, and
   typeclass instances. Tactics also generate proof terms during elaboration.
3. The kernel checks the resulting terms against their declared types.
4. Executable definitions may be evaluated in Lean or compiled to native code.

The distinction between elaboration and kernel checking is important. Tactics
may be sophisticated, but their final output is still a proof term checked by
the smaller trusted kernel. A theorem usually needs to be type-checked rather
than executed; a program with a `main` function can additionally be compiled
and run.

## Proof terms and tactics

The `by` keyword opens tactic mode. A tactic transforms a proof state containing
local hypotheses and one or more goals:

```lean
example (p q : Prop) : p → q → p ∧ q := by
  intro hp hq
  constructor
  · exact hp
  · exact hq
```

The same proof can be written directly as a term:

```lean
example (p q : Prop) : p → q → p ∧ q :=
  fun hp hq => ⟨hp, hq⟩
```

Both styles are valuable. Tactics expose the incremental reasoning process,
while proof terms make the program-like structure of a proof especially clear.

Frequently used tactics include:

- `intro` to introduce a function argument or hypothesis;
- `exact` to provide a term with exactly the required type;
- `apply` to use a theorem whose conclusion matches the goal;
- `constructor` to build a value with multiple required fields;
- `left` and `right` to select a disjunction constructor;
- `cases` to handle every constructor of a value;
- `rw` to substitute using an equality;
- `simp` to perform routine, rule-driven simplification;
- `induction` to obtain hypotheses for structurally smaller data;
- `rfl` to prove equality by computation.

## Recursion and induction

Recursive functions and inductive proofs often share the same shape. A list
function has an empty-list branch and a `head :: tail` branch; a proof about
that function typically uses the same two cases. In the recursive branch, the
induction hypothesis describes the already-known result for the smaller tail.

When a proof becomes difficult, check whether:

- the induction variable follows the recursive argument of the definition;
- the induction hypothesis is general enough;
- unfolding one definition exposes the expected constructor case;
- a helper lemma is needed for a nested operation such as append inside reverse;
- the goal differs only by a standard associativity or commutativity lemma.

## Typeclasses and dependent types

The final lessons introduce two ways to express stronger APIs.

A typeclass constraint such as `[BEq α]` asks Lean to find behavior associated
with the type `α`. This supports generic functions without hard-coding concrete
types. Instances can depend on other instances, allowing capabilities to be
composed.

A dependent type allows later parts of a type to mention earlier values.
`SizedList α n`, for example, records length `n` in the type. Combined with
`Fin n`, it makes out-of-bounds indexing unrepresentable, so a lookup function
does not need to return `Option α`.

These guarantees have a cost: callers must supply stronger values or evidence.
The lesson is not that every invariant belongs in a type, but that Lean lets an
API designer choose which invalid states should be rejected before execution.

## Final mini-project

`Lesson018_VerifiedExpressionOptimizer.lean` connects the earlier topics in one small
verification project:

1. `Expr` defines the syntax of a tiny arithmetic language.
2. `Expr.evaluate` assigns semantics to expressions.
3. `Expr.optimize` performs constant folding and removes neutral elements.
4. helper lemmas verify the local addition and multiplication rewrites;
5. `Expr.optimize_correct` proves by induction that optimization preserves
   evaluation for every expression and environment.

This separation between syntax, semantics, transformation, and correctness is
a compact example of a pattern used in verified compilers and interpreters.

## Common errors

### Unknown identifier

The name is not in scope, is spelled differently, or requires an import. Check
capitalization and namespace qualifiers before changing the proof.

### Type mismatch

Lean produced a value of a different type from the expected one. Read both
types in the error message and identify the first place where they diverge.

### Unsolved goals

The tactic block ended while goals remained open. Inspect each goal in the
editor and determine which constructor, hypothesis, or equality it requires.

### Failed to synthesize an instance

Lean could not find a requested capability, such as `BEq α`, `Decidable p`, or
an application-specific typeclass. Add a suitable constraint or instance.

### Failed to show termination

Lean cannot see that recursive calls use smaller data. Prefer structural
recursion when possible; otherwise, redesign the recursion or provide a
well-founded termination argument.

### Invalid constructor or impossible case

The expected type may rule out the constructor being used. With dependent
types, inspect the indices as well as the outer type name.

### Toolchain error

Use `elan show` and inspect the project's `lean-toolchain` file. A missing or
incompatible toolchain prevents Lean from checking otherwise valid code.

## Style principles used in this directory

- Definitions and variables use descriptive English names.
- Functions remain short and focus on one idea.
- Comments explain why a definition or proof has its shape.
- Exercise statements are preserved beside their worked solutions.
- Pattern matches make base cases and recursive cases visible.
- Helper lemmas isolate reusable reasoning from larger proofs.
- Automation is used when it improves clarity, not to hide the central idea.
- Lessons favor understandable code over compressed or clever proofs.

## Ideas for further development

Natural extensions of this learning path include:

- converting the standalone lessons into a Lake library with imports;
- adding unsolved companion files for independent practice;
- introducing `Mathlib` and theorem search;
- proving additional algebraic laws for maps, folds, and traversals;
- defining balanced or ordered trees with explicit invariants;
- adding a typed expression language and a type-safety proof;
- extending the optimizer with subtraction, conditionals, or variables stored
  in a finite environment;
- adding automated checks that compile every lesson in continuous integration.

## Further reading

- [Lean installation guide](https://lean-lang.org/install/manual/)
- [Lean Language Reference](https://lean-lang.org/doc/reference/latest/)
- [Lake reference](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/)
- [Managing toolchains with Elan](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/)

The most useful habit throughout the directory is to read every goal as a type:
ask which constructor, function, or previously proved theorem can produce a
value of that type. Tactics then become tools guided by structure rather than a
list of commands to memorize.
