# PyTorch

This track makes the mechanics of deep-learning training explicit: tensors,
autograd, modules, data loaders, optimization steps, evaluation mode, and safe
parameter checkpoints.

## Setup

The pinned requirements use CPU wheels so the lessons do not depend on a local
CUDA installation. Use Python 3.12 to match CI:

```powershell
py -3.12 -m venv .venv-pytorch
.\.venv-pytorch\Scripts\Activate.ps1
python -m pip install -r .\Python\requirements\pytorch.txt
```

Use PyTorch's official installation selector instead when GPU acceleration is
required because the command depends on the operating system and CUDA or ROCm
version.

## Lessons and objectives

| File | Topic |
| --- | --- |
| `000_tensors_and_gradients.py` | Shapes, reductions, broadcasting, autograd |
| `001_training_loop.py` | `nn.Module`, `DataLoader`, optimizer, loop, checkpoint |

Afterward, explain why gradients accumulate, why `zero_grad()` occurs before
each update, how `backward()` populates `.grad`, and how `train()`, `eval()`, and
`no_grad()` affect behavior and resource use.

## Training loop mental model

For every batch: clear old gradients, compute predictions, calculate one scalar
loss, backpropagate, and update parameters. Evaluation switches the model to
evaluation mode and disables gradient tracking. The distinction matters for
dropout, batch normalization, memory use, and reproducibility.

The lesson saves a `state_dict`, which contains parameter tensors without
serializing an arbitrary Python model object. Loading therefore requires the
same architecture definition and an explicit call to `load_state_dict`.

Common mistakes include forgetting to clear accumulated gradients, mixing
devices, using incompatible shapes that broadcast silently, evaluating without
`eval()`, and trusting checkpoints from untrusted sources.

Exercises: reload the checkpoint into a fresh model; introduce shuffled batches;
split training and validation data; move tensors and model through one selected
device; and compare the explicit loop with the equivalent Keras workflow.

Further reading: [tensor tutorial](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html),
[autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html), and
[optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html).
