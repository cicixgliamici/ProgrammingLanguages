import Lake

open Lake DSL

package programmingLanguagesLessons where
  version := v!"0.1.0"

@[default_target]
lean_lib LearningLessons where
  -- Configuration lives separately from lessons, so the source root is the
  -- repository root two directories above this Lake project.
  srcDir := "../.."
  -- Every lesson is an independent module, so repeated teaching definitions
  -- do not collide in one artificial aggregate module.
  globs := #[.submodules `Lean]
