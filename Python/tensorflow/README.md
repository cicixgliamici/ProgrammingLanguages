# TensorFlow and Keras

This track connects tensor operations and automatic differentiation to a small
Keras training workflow. It uses CPU-compatible code and deterministic local
data, so a GPU is optional.

## Compatibility and setup

TensorFlow 2.21 supports Python 3.10–3.13. Use Python 3.12, matching CI; the
repository's current Python 3.14 development environment is intentionally not
used for this dependency.

```powershell
py -3.12 -m venv .venv-tensorflow
.\.venv-tensorflow\Scripts\Activate.ps1
python -m pip install -r .\Python\requirements\tensorflow.txt
```

Native Windows supports CPU execution. For supported NVIDIA GPU execution on
Windows, use WSL2 and follow TensorFlow's official installation matrix.

## Lessons and objectives

| File | Topic |
| --- | --- |
| `000_tensors_and_gradients.py` | Shapes, reductions, broadcasting, `GradientTape` |
| `001_keras_regression.py` | Keras model, loss, optimizer, training history, serialization |

Afterward, explain tensor shape and dtype, the forward pass, gradient, loss,
batch, epoch, optimizer step, training/evaluation distinction, and why a saved
model must be validated after loading.

The regression dataset deliberately follows a known linear rule. This verifies
the mechanics; it is not evidence that a neural network is appropriate for a
real task. The fixed seed improves repeatability but deterministic behavior can
still depend on hardware and specific operations.

## Training mental model

One optimization step performs: forward computation, scalar loss calculation,
automatic differentiation, parameter update, then repetition over batches.
Keras packages that loop in `fit`, while callbacks, validation data, and the
returned history expose the process for monitoring.

Common mistakes include evaluating on training data, confusing batches with
epochs, applying activation functions unsuitable for the target, using test
data for early stopping, and saving weights without recording architecture or
preprocessing.

Exercises: add a validation split; implement early stopping; reload the `.keras`
file and compare predictions; add noise and inspect residuals; then replace the
linear layer with a small nonlinear network and justify whether it is needed.

Further reading: [TensorFlow tensors](https://www.tensorflow.org/guide/tensor),
[automatic differentiation](https://www.tensorflow.org/guide/autodiff), and
[Keras training](https://www.tensorflow.org/guide/keras/training_with_built_in_methods).
