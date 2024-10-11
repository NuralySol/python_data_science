# Import necessary libraries
import numpy as np
import pandas as pd
import array
import tensorflow as tf

# ------------------------------
# 1. Python Built-in Lists
# ------------------------------
# Lists in Python can hold any data type, and types can be mixed
python_list = [1, "hello", 3.14, True]  # A list with mixed data types
print("Python List:", python_list)
print("Type of Python List:", type(python_list))

# ------------------------------
# 2. NumPy Arrays
# ------------------------------
# NumPy arrays are homogeneous; all elements must be of the same type
int_array = np.array([1, 2, 3], dtype="int32")  # Integer array
float_array = np.array([1.0, 2.0, 3.0], dtype="float64")  # Float array
bool_array = np.array([True, False, True], dtype="bool")  # Boolean array

# Print arrays and their data types
print("\nNumPy Integer Array:", int_array)
print("Data Type of NumPy Integer Array:", int_array.dtype)

print("NumPy Float Array:", float_array)
print("Data Type of NumPy Float Array:", float_array.dtype)

print("NumPy Boolean Array:", bool_array)
print("Data Type of NumPy Boolean Array:", bool_array.dtype)

# ------------------------------
# 3. Pandas Series (DataFrame Columns)
# ------------------------------
# Each column in a pandas DataFrame is a Series, which is built on top of NumPy arrays
data = pd.Series([1, 2, 3, 4.0])  # A pandas Series with mixed int and float
print("\nPandas Series:")
print(data)
print("Data Type of Pandas Series:", data.dtype)

# You can also create a DataFrame and access columns as Series
df = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [24, 27, 22, 32],
        "City": ["New York", "Paris", "London", "Berlin"],
    }
)

# Accessing the 'Age' column as a pandas Series
age_series = df["Age"]
print("\nPandas DataFrame 'Age' Column (Series):")
print(age_series)
print("Data Type of 'Age' Column:", age_series.dtype)

# ------------------------------
# 4. Python's `array` Module
# ------------------------------
# The `array` module supports arrays of specific types. Here, 'i' stands for integers.
int_array_module = array.array("i", [1, 2, 3, 4])  # Integer array
float_array_module = array.array("f", [1.1, 2.2, 3.3])  # Float array

# Print arrays from the array module and their type codes
print("\nArray Module Integer Array:", int_array_module)
print("Type Code of Integer Array:", int_array_module.typecode)

print("Array Module Float Array:", float_array_module)
print("Type Code of Float Array:", float_array_module.typecode)

# ------------------------------
# 5. TensorFlow Tensors
# ------------------------------
# TensorFlow arrays are called tensors, and they can hold various types of data
tensor_float = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)  # Tensor of float32 type
tensor_int = tf.constant([1, 2, 3], dtype=tf.int32)  # Tensor of int32 type
tensor_bool = tf.constant([True, False, True], dtype=tf.bool)  # Tensor of bool type

# Print the TensorFlow tensors and their data types
print("\nTensorFlow Float Tensor:", tensor_float)
print("Data Type of Float Tensor:", tensor_float.dtype)

print("TensorFlow Int Tensor:", tensor_int)
print("Data Type of Int Tensor:", tensor_int.dtype)

print("TensorFlow Bool Tensor:", tensor_bool)
print("Data Type of Bool Tensor:", tensor_bool.dtype)

# ------------------------------
# Summary of Array Data Types
# ------------------------------

# 1. Python lists are flexible and can hold mixed data types, but they are not memory efficient.
# 2. NumPy arrays are homogeneous and optimized for numerical computations. Their dtype can be 'int32', 'float64', 'bool', etc.
# 3. Pandas Series, which are used in DataFrames, are built on NumPy arrays and can have data types like 'int64', 'float64', 'object', etc.
# 4. Python's `array` module supports typed arrays like 'i' (integers) and 'f' (floats) for better memory efficiency.
# 5. TensorFlow tensors are arrays used in machine learning, supporting types like 'tf.float32', 'tf.int32', and 'tf.bool'.

# Each type of array has its specific use case:
# - Python lists are best for general-purpose use where the data type doesn't matter.
# - NumPy arrays are ideal for numerical and scientific computations.
# - Pandas Series/DataFrames are great for handling structured data, especially in data analysis tasks.
# - The `array` module is a memory-efficient choice for simple arrays.
# - TensorFlow tensors are used in machine learning for handling large amounts of data in computations.

# Pandas DataFrames can be thought of as schemaless in the sense that they don’t have a strictly enforced schema like a SQL database. However, you can still treat a DataFrame as if it had a schema by ensuring that specific data types are assigned to each column.

# A primary key is a column (or combination of columns) that uniquely identifies each row in a table. In pandas, there is no native primary key enforcement, but you can manually enforce uniqueness by checking for duplicates in the column.

# A foreign key in a relational database is a column that creates a link between two tables, referencing a primary key from another table. While pandas doesn’t enforce foreign key constraints, you can simulate them by ensuring that the values in one DataFrame (the “child”) exist in another DataFrame (the “parent”).

import pandas as pd

# ------------------------------
# Simulating Primary Key
# ------------------------------
# Create a DataFrame with a primary key column
data = {
    "ID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
}

df = pd.DataFrame(data)

# Check for duplicate primary key values (ID column)
if df["ID"].is_unique:
    print("Primary key constraint is satisfied (no duplicates in 'ID').")
else:
    print("Primary key constraint violated (duplicates found in 'ID').")

# ------------------------------
# Simulating Foreign Key
# ------------------------------
# Parent table (with primary key)
parent_data = {
    "DepartmentID": [101, 102, 103],
    "DepartmentName": ["HR", "Finance", "Engineering"],
}

parent_df = pd.DataFrame(parent_data)

# Child table (with foreign key referencing the parent's primary key)
child_data = {
    "EmployeeID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "DepartmentID": [101, 102, 101],  # Foreign key column
}

child_df = pd.DataFrame(child_data)

# Check if all foreign keys in 'child_df' exist in the 'parent_df'
if child_df["DepartmentID"].isin(parent_df["DepartmentID"]).all():
    print(
        "Foreign key constraint is satisfied (all DepartmentIDs exist in the parent table)."
    )
else:
    print(
        "Foreign key constraint violated (some DepartmentIDs do not exist in the parent table)."
    )

# ------------------------------
# Merging the DataFrames based on Foreign Key
# ------------------------------
# Merge the child and parent DataFrames on 'DepartmentID'
merged_df = pd.merge(child_df, parent_df, on="DepartmentID")

print("\nMerged DataFrame:")
print(merged_df)

#! User input for dynamic entry to a Data Frame (PUT)
import pandas as pd

new_item = pd.DataFrame(columns=["Item", "Price", "Cals", "Vegan"])


def append_to_df():
    user_input = input("Enter Item, Price, Cals, and Vegan (comma separated): ").split(
        ","
    )

    data_list = [
        str(user_input[0]),
        float(user_input[1]),
        int(user_input[2]),
        user_input[3].strip().lower() == "true",
    ]

    global new_item
    new_item = pd.concat(
        [new_item, pd.DataFrame([data_list], columns=new_item.columns)],
        ignore_index=True,
    )

    print("\nUpdated DataFrame:")
    print(new_item)


while True:
    append_to_df()

    continue_input = (
        input("\nDo you want to add another entry? (yes/no): ").strip().lower()
    )
    if continue_input != "yes":
        break


#! Below code is CRUD operations on Data Frame arrays from Pandas
import pandas as pd

# Create an empty DataFrame
new_item = pd.DataFrame(columns=["Item", "Price", "Cals", "Vegan"])


def append_to_df():
    user_input = input("Enter Item, Price, Cals, and Vegan (comma separated): ").split(
        ","
    )
    data_list = [
        str(user_input[0]),
        float(user_input[1]),
        int(user_input[2]),
        user_input[3].strip().lower() == "true",
    ]
    global new_item
    new_item = pd.concat(
        [new_item, pd.DataFrame([data_list], columns=new_item.columns)],
        ignore_index=True,
    )
    print("\nItem added:")
    print(new_item)


def read_from_df(item_name):
    global new_item
    result = new_item[new_item["Item"] == item_name]
    if not result.empty:
        print("\nItem found:")
        print(result)
    else:
        print("\nItem not found.")


def update_df(item_name):
    global new_item
    index = new_item[new_item["Item"] == item_name].index
    if not index.empty:
        print(f"\nUpdating item: {item_name}")
        new_data = input(
            "Enter new Item, Price, Cals, and Vegan (comma separated): "
        ).split(",")
        new_item.at[index[0], "Item"] = str(new_data[0])
        new_item.at[index[0], "Price"] = float(new_data[1])
        new_item.at[index[0], "Cals"] = int(new_data[2])
        new_item.at[index[0], "Vegan"] = new_data[3].strip().lower() == "true"
        print("\nItem updated:")
        print(new_item)
    else:
        print("\nItem not found.")


def delete_from_df(item_name):
    global new_item
    index = new_item[new_item["Item"] == item_name].index
    if not index.empty:
        new_item = new_item.drop(index)
        print(f"\nItem '{item_name}' deleted.")
        print(new_item)
    else:
        print("\nItem not found.")


while True:
    operation = (
        input("\nWhat do you want to do? (add/read/update/delete): ").strip().lower()
    )

    if operation == "add":
        append_to_df()
    elif operation == "read":
        item_name = input("Enter the item name to read: ").strip()
        read_from_df(item_name)
    elif operation == "update":
        item_name = input("Enter the item name to update: ").strip()
        update_df(item_name)
    elif operation == "delete":
        item_name = input("Enter the item name to delete: ").strip()
        delete_from_df(item_name)
    else:
        print("Invalid operation.")

    continue_input = (
        input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
    )
    if continue_input != "yes":
        break

#! make a DF from a dict. resulting df will one row of each item!
import pandas as pd

# Create DataFrame from a dictionary
data = {"Name": ["John", "Mary", "Peter"], "Age": [20, 25, 30]}
df = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df)

# Get the keys (column names)
keys = df.keys() 

print("\nKeys (Column Names):")
print(type(keys))  # Check the type of keys (should be an Index object)

# Convert the keys to a list
keys_list = list(keys)

print("\nKeys as a List:")
print(type(keys_list))  # Check the type of keys_list (should be a list)

# Demonstrate concatenating a new DataFrame to the existing one
# New data to be concatenated
new_data = {"Name": ["Alice", "Bob"], "Age": [28, 22]}
new_df = pd.DataFrame(new_data)

# Concatenating the new DataFrame to the original one
df = pd.concat([df, new_df], ignore_index=True)

print("\nDataFrame after Concatenation:")
print(df)

import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create an initial DataFrame
df = pd.DataFrame(columns=['Name', 'Age'])

def log_dataframe_change(operation, df):
    logging.info(f"{operation} performed. Updated DataFrame:\n{df}")

# Adding initial data
new_row = {'Name': 'John', 'Age': 30}
df = df.append(new_row, ignore_index=True)
log_dataframe_change("Row added", df)

# Adding another row
new_row = {'Name': 'Mary', 'Age': 25}
df = df.append(new_row, ignore_index=True)
log_dataframe_change("Row added", df)

# Dropping a row using inplace=True
# The 'inplace=True' modifies the DataFrame in place, meaning the changes happen directly on the DataFrame without needing reassignment.
df.drop(1, inplace=True)  # Dropping the row at index 1 (Mary's row)
log_dataframe_change("Row deleted for Mary", df)

# Adding a new column
df['City'] = ['New York']
log_dataframe_change("City column added", df)


#! Multi-level sort, and column sort. 
import pandas as pd

# Create a multi-level column DataFrame
arrays = [
    ['Score', 'Score', 'Grade', 'Grade'],
    ['Math', 'Science', 'Math', 'Science']
]
columns = pd.MultiIndex.from_arrays(arrays, names=('Category', 'Subject'))

# Create sample data
data = [
    [85, 90, 'B', 'A'],
    [78, 88, 'C', 'B'],
    [92, 80, 'A', 'B']
]

df = pd.DataFrame(data, columns=columns)

# Display the original DataFrame
print("\nOriginal DataFrame:")
print(df)

# Sort by 'Score' level, 'Math' subject
sorted_df = df.sort_values(by=('Score', 'Math'))

print("\nDataFrame sorted by Score -> Math:")
print(sorted_df)

# Sort by multiple levels ('Grade' -> 'Science', and 'Score' -> 'Math')
sorted_multi_df = df.sort_values(by=[('Grade', 'Science'), ('Score', 'Math')])

print("\nDataFrame sorted by Grade -> Science and Score -> Math:")
print(sorted_multi_df)

