# Build configuration

This directory keeps cross-project build configuration away from the
multi-language repository root.

| Directory | Contents | Recommended command |
| --- | --- | --- |
| `lean/` | Lake package, manifest, and pinned Lean toolchain | `powershell -File scripts/build-lean.ps1` |
| `coq/` | Source order and logical namespace in `_CoqProject` | `powershell -File scripts/build-coq.ps1` |

The wrappers resolve paths from the repository root and keep generated output
in ignored directories. CI uses the same configuration files directly.

Configuration required to reproduce a build belongs here or in the conventional
directory of its project, such as `Java/pom.xml`, `Scala/build.sbt`, or
`C/CMakeLists.txt`. Personal notes, progress tracking, credentials, and
machine-specific settings do not belong here; use the ignored `local/`
directory for maintainer-only text.
