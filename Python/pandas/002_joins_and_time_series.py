"""Join relational tables and aggregate observations over time."""

from __future__ import annotations

import pandas as pd


def create_orders_and_customers() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Create related tables, including one unmatched foreign key."""
    orders = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5],
            "customer_id": [10, 20, 10, 30, 99],
            "ordered_at": [
                "2026-01-05", "2026-01-18", "2026-02-02", "2026-02-20", "2026-03-01"
            ],
            "amount": [120.0, 75.0, 40.0, 210.0, 15.0],
        }
    )
    customers = pd.DataFrame(
        {
            "customer_id": [10, 20, 30],
            "segment": ["business", "consumer", "business"],
        }
    )
    return orders, customers


def enrich_orders(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    """Left-join customers and retain unmatched orders for quality checks."""
    enriched = orders.merge(
        customers,
        on="customer_id",
        how="left",
        validate="many_to_one",
        indicator=True,
    )
    enriched["ordered_at"] = pd.to_datetime(enriched["ordered_at"], errors="raise")
    return enriched


def unmatched_customer_ids(enriched_orders: pd.DataFrame) -> list[int]:
    """Return foreign keys that did not match a customer record."""
    unmatched = enriched_orders.loc[
        enriched_orders["_merge"] == "left_only",
        "customer_id",
    ]
    return sorted(unmatched.astype(int).unique().tolist())


def monthly_revenue(enriched_orders: pd.DataFrame) -> pd.Series:
    """Aggregate revenue into calendar months with a datetime index."""
    dated_orders = enriched_orders.set_index("ordered_at")
    # Month-start labels make each bucket boundary explicit in the result.
    return dated_orders["amount"].resample("MS").sum().rename("monthly_revenue")


def main() -> None:
    orders, customers = create_orders_and_customers()
    enriched = enrich_orders(orders, customers)
    print("Joined orders:\n", enriched)
    print("Unmatched customer IDs:", unmatched_customer_ids(enriched))
    print("Monthly revenue:\n", monthly_revenue(enriched))


if __name__ == "__main__":
    main()
