"""Clean missing values and summarize groups with explicit policies."""

from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS = {"region", "product", "units", "unit_price"}


def create_incomplete_sales() -> pd.DataFrame:
    """Create deterministic input containing duplicates and missing values."""
    return pd.DataFrame(
        {
            "region": ["North", " south ", "North", "West", "West", "West"],
            "product": ["Keyboard", "Mouse", "Keyboard", "Monitor", "Mouse", "Mouse"],
            "units": [3.0, 5.0, 3.0, 2.0, None, None],
            "unit_price": [70.0, 25.0, 70.0, 220.0, 25.0, 25.0],
        }
    )


def clean_sales(sales: pd.DataFrame) -> pd.DataFrame:
    """Normalize text, remove duplicates, and impute units by product median."""
    missing_columns = REQUIRED_COLUMNS.difference(sales.columns)
    if missing_columns:
        raise ValueError(f"missing required columns: {sorted(missing_columns)}")

    cleaned = sales.copy()
    for column in ["region", "product"]:
        cleaned[column] = cleaned[column].str.strip().str.lower()
    cleaned = cleaned.drop_duplicates().reset_index(drop=True)

    # A product-level median uses a more relevant peer group than one global
    # value. The policy is still a modelling decision and must be documented.
    product_medians = cleaned.groupby("product")["units"].transform("median")
    cleaned["units"] = cleaned["units"].fillna(product_medians)
    if cleaned["units"].isna().any():
        raise ValueError("units cannot be imputed for products with no observed value")

    cleaned["revenue"] = cleaned["units"] * cleaned["unit_price"]
    return cleaned


def revenue_by_region(sales: pd.DataFrame) -> pd.DataFrame:
    """Return ordered region summaries with stable, named columns."""
    cleaned = clean_sales(sales)
    summary = (
        cleaned.groupby("region", as_index=False)
        .agg(total_units=("units", "sum"), total_revenue=("revenue", "sum"))
        .sort_values("total_revenue", ascending=False)
        .reset_index(drop=True)
    )
    return summary


def main() -> None:
    sales = create_incomplete_sales()
    print("Missing values before cleaning:\n", sales.isna().sum())
    print("Clean data:\n", clean_sales(sales))
    print("Revenue by region:\n", revenue_by_region(sales))


if __name__ == "__main__":
    main()
