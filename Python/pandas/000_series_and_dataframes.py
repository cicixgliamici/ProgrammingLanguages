"""Create labelled pandas objects and select data predictably."""

from __future__ import annotations

import pandas as pd


def create_sales_data() -> pd.DataFrame:
    """Create a small table with explicit column names and row labels."""
    return pd.DataFrame(
        {
            "product": ["keyboard", "mouse", "monitor", "keyboard"],
            "units": [3, 5, 2, 4],
            "unit_price": [70.0, 25.0, 220.0, 70.0],
        },
        index=pd.Index(["order-101", "order-102", "order-103", "order-104"], name="order_id"),
    )


def add_revenue(sales: pd.DataFrame) -> pd.DataFrame:
    """Return an enriched copy without mutating the caller's table."""
    enriched = sales.copy()
    enriched["revenue"] = enriched["units"] * enriched["unit_price"]
    return enriched


def select_large_orders(sales: pd.DataFrame, minimum_revenue: float) -> pd.DataFrame:
    """Select rows by label-aware Boolean filtering."""
    if minimum_revenue < 0:
        raise ValueError("minimum_revenue must be non-negative")
    with_revenue = add_revenue(sales)
    columns = ["product", "revenue"]
    return with_revenue.loc[with_revenue["revenue"] >= minimum_revenue, columns]


def main() -> None:
    sales = create_sales_data()
    print("Table shape:", sales.shape)
    print("Column data types:\n", sales.dtypes)
    print("One labelled row:\n", sales.loc["order-102"])
    print("First two physical rows:\n", sales.iloc[:2])
    print("Large orders:\n", select_large_orders(sales, minimum_revenue=200.0))


if __name__ == "__main__":
    main()
