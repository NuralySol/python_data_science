# Pandas DataFrame Indexing with `iloc` and `loc`

This guide covers in-depth information on how to use `.iloc` and `.loc` in pandas for DataFrame indexing and selection.

---

## 1. Core Concepts

- **`loc`**: Label-based indexing that allows selection using row and column labels (i.e., the actual values of the index and columns).
- **`iloc`**: Position-based indexing that selects rows and columns by their integer positions (starting from 0).

Both are used to access subsets of a DataFrame, but they operate fundamentally differently.

---

## 2. `loc[]`: Label-Based Indexing

### How it Works

`loc[]` accesses rows and columns using the actual labels of the index and column names. If your DataFrame has an index of strings, dates, or other non-integer labels, `loc[]` will refer to these values directly.

### Key Features

- **Label-based selection**: Use row or column labels instead of numeric positions.
- **Inclusive range**: When slicing, the endpoint is included.
  
### Examples

- **Access a single row by label**:

  ```python
  df.loc['row_label']
