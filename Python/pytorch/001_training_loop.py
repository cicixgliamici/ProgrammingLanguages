"""Train and checkpoint a minimal PyTorch regression model."""

from __future__ import annotations

from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


def create_dataset() -> TensorDataset:
    """Create observations from y = 2x + 1 without sampling noise."""
    features = torch.linspace(-2.0, 2.0, 81).reshape(-1, 1)
    targets = 2.0 * features + 1.0
    return TensorDataset(features, targets)


def build_model() -> nn.Module:
    """Build one linear layer matching the data-generating process."""
    return nn.Linear(in_features=1, out_features=1)


def train_model(epochs: int = 120) -> tuple[nn.Module, list[float]]:
    """Run an explicit optimization loop and return epoch losses."""
    if epochs < 1:
        raise ValueError("epochs must be positive")
    torch.manual_seed(42)
    model = build_model()
    loader = DataLoader(create_dataset(), batch_size=16, shuffle=False)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.05)
    loss_function = nn.MSELoss()
    losses: list[float] = []

    for _ in range(epochs):
        total_loss = 0.0
        for features, targets in loader:
            optimizer.zero_grad()
            loss = loss_function(model(features), targets)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * len(features)
        losses.append(total_loss / len(loader.dataset))
    return model, losses


def save_checkpoint(model: nn.Module, destination: Path) -> Path:
    """Save model parameters rather than serializing arbitrary Python objects."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), destination)
    return destination


def main() -> None:
    model, losses = train_model()
    model.eval()
    with torch.no_grad():
        prediction = model(torch.tensor([[3.0]])).item()
    print(f"Initial loss: {losses[0]:.4f}")
    print(f"Final loss: {losses[-1]:.4f}")
    print(f"Prediction for x=3: {prediction:.3f}")
    print("Saved:", save_checkpoint(model, Path("build/pytorch/linear_model.pt")))


if __name__ == "__main__":
    main()
