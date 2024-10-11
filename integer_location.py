
#! Python Lesson: `iloc` and `loc` in Pandas with Rows and Columns

import pandas as pd

# Sample DataFrame with labels as index
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Paris', 'London', 'Berlin']
}

df = pd.DataFrame(data)
df.index = ['ID1', 'ID2', 'ID3', 'ID4']  # Setting row labels

print("Original DataFrame:")
print(df)

# --------------------------------------------------
# 1. Using `.loc[]` (Label-based selection)
# --------------------------------------------------

# Select a single row by label
print("\n1.1 Select the row with label 'ID1'")
row = df.loc['ID1']
print(row)

# Select a specific cell by label
print("\n1.2 Select the Age of 'ID2'")
age = df.loc['ID2', 'Age']
print(age)

# Select multiple rows and columns by label
print("\n1.3 Select 'Name' and 'City' columns for 'ID1' and 'ID3'")
subset = df.loc[['ID1', 'ID3'], ['Name', 'City']]
print(subset)

# Use conditions to filter rows
print("\n1.4 Select rows where Age is greater than 25")
age_filter = df.loc[df['Age'] > 25]
print(age_filter)

# --------------------------------------------------
# 2. Using `.iloc[]` (Position-based selection)
# --------------------------------------------------

# Select a single row by position
print("\n2.1 Select the first row (index position 0)")
first_row = df.iloc[0]
print(first_row)

# Select a specific cell by position
print("\n2.2 Select the first row and second column (index positions: row=0, column=1)")
age = df.iloc[0, 1]
print(age)

# Select multiple rows and columns by position
print("\n2.3 Select the first two rows and first two columns")
subset = df.iloc[0:2, 0:2]
print(subset)

# Slice all rows and first two columns
print("\n2.4 Select all rows but only the first two columns")
subset = df.iloc[:, 0:2]
print(subset)


#! Run the below code-snippet by itself!
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Paris', 'London', 'Berlin']
}

df = pd.DataFrame(data)

# Accessing a single column as a Series
age_series = df['Age']
print(type(age_series))  # Output: <class 'pandas.core.series.Series'>
print(age_series)
