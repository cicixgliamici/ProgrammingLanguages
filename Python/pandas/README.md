# Learning pandas

This track introduces labelled tabular data through small, executable examples.
It focuses on operations needed before a trustworthy machine-learning workflow:
schema inspection, selection, cleaning, aggregation, relational joins, and time
series.

## Learning objectives

After the lessons, a reader should be able to:

- explain the roles of a `Series`, `DataFrame`, index, row, and column;
- distinguish label selection with `loc` from position selection with `iloc`;
- filter rows with Boolean masks without accidentally mutating input data;
- inspect data types, missing values, duplicates, and required columns;
- apply and justify an explicit missing-value policy;
- use `groupby` and named aggregations to produce stable summaries;
- choose a join type and validate its expected cardinality;
- detect unmatched relational keys rather than silently discarding them;
- parse datetimes and resample observations into calendar periods.

## Prerequisites and setup

Study Python fundamentals and NumPy first. Install the pinned dependency from
the repository root:

```powershell
python -m pip install -r .\Python\requirements\pandas.txt
```

## Lesson index

| File | Topic | Central question |
| --- | --- | --- |
| `000_series_and_dataframes.py` | Construction, labels, selection, derived columns | How does a labelled table differ from a nested list or NumPy array? |
| `001_cleaning_and_grouping.py` | Missing data, duplicates, normalization, grouping | Which cleaning decisions change the meaning of the data? |
| `002_joins_and_time_series.py` | Validated joins, unmatched keys, datetimes, resampling | How do tables and events combine without losing observations? |

Run each lesson from the repository root:

```powershell
python .\Python\pandas\000_series_and_dataframes.py
python .\Python\pandas\001_cleaning_and_grouping.py
python .\Python\pandas\002_joins_and_time_series.py
```

Run the complete Python test suite with:

```powershell
python -m unittest discover -s .\Python\tests -v
```

## Mental model

A `Series` is a one-dimensional sequence of values with an index. A `DataFrame`
is a two-dimensional collection of aligned Series. The index is part of the
data model: pandas aligns many operations by labels rather than only by physical
position.

- `frame.loc[row_labels, column_labels]` selects by label.
- `frame.iloc[row_positions, column_positions]` selects by integer position.
- `frame["column"]` returns one Series.
- `frame[["a", "b"]]` returns a DataFrame containing selected columns.

Alignment is powerful but can silently create missing values if labels differ.
Inspect indexes before arithmetic or joins when their origin is uncertain.

## Cleaning is a policy

Cleaning is not a neutral sequence of API calls. Dropping a row, replacing a
missing value, coercing a type, or merging categories changes the dataset and
can change a later conclusion. A reproducible cleaning function should:

1. validate the expected schema;
2. work on a copy unless mutation is part of its contract;
3. normalize known inconsistencies;
4. make missing-value and duplicate policies explicit;
5. verify important postconditions.

Prefer vectorized string, datetime, and numeric operations over row-by-row
`apply` when pandas already provides the operation. Vectorized code usually
states the transformation more clearly and performs it more efficiently.

## Grouping and aggregation

The split-apply-combine model divides rows into groups, applies a calculation,
and combines the results. Named aggregation keeps output columns predictable:

```python
summary = frame.groupby("region", as_index=False).agg(
    total_units=("units", "sum"),
    average_price=("unit_price", "mean"),
)
```

Decide whether missing group keys should be excluded, filled, or retained with
`dropna=False`. Also distinguish `agg`, which normally reduces each group, from
`transform`, which returns values aligned with the original rows.

## Joins and cardinality

Join type expresses which observations must survive:

- inner: only matching keys;
- left: every left row, with missing right values when unmatched;
- right: every right row;
- outer: every key from both sides.

Use `validate="one_to_one"`, `"one_to_many"`, or `"many_to_one"` when the
relationship has an expected cardinality. This catches duplicate keys that
would otherwise multiply rows. `indicator=True` records whether each result
came from both tables or remained unmatched.

## Time data

Parse dates explicitly with `pd.to_datetime`; do not leave dates as strings and
assume lexical order always represents time. A `DatetimeIndex` enables calendar
selection, time differences, rolling windows, and `resample`. Be explicit about
time zones when observations come from more than one locale or cross daylight
saving transitions.

## Common mistakes

- Confusing `loc` labels with `iloc` positions.
- Using chained indexing and expecting assignment to affect the original table.
- Filling every numeric missing value with one global mean without justification.
- Performing a join without checking key uniqueness or unmatched rows.
- Assuming input data types are correct because a file loaded successfully.
- Treating an index as decoration even though operations align by it.
- Converting dates without considering invalid values or time zones.

## Exercises

1. Add discounts to the sales table and calculate net revenue without mutation.
2. Create misaligned Series and explain every missing value in their sum.
3. Compare global median imputation with product-level median imputation.
4. Add a duplicated customer key and observe how join validation responds.
5. Produce monthly revenue per customer segment with `groupby` and `resample`.
6. Load a deliberately malformed CSV and define a schema-validation function.
7. Convert a timestamp column from UTC to `Europe/Rome` and inspect a daylight
   saving transition.

## Further reading

- [pandas getting started](https://pandas.pydata.org/docs/getting_started/)
- [Indexing and selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html)
- [Time series and date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html)
