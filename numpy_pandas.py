import tkinter as tk
import pandas as pd
import numpy as np

# Step 1: Create a NumPy array (5x5 random integers from 1 to 100)
array = np.random.randint(1, 101, size=(5, 5))

# Step 2: Convert the NumPy array to a Pandas DataFrame with column and row labels
df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'], index=[1, 2, 3, 4, 5])

# Step 3: Create a Tkinter window to display the DataFrame
def show_dataframe_in_tkinter(df):
    root = tk.Tk()
    root.title("DataFrame Display (5x5 Random Integers)")

    # Create labels for DataFrame columns
    for j, column in enumerate(df.columns):
        tk.Label(root, text=column, borderwidth=2, relief="solid", width=10, height=2).grid(row=0, column=j+1)

    # Create labels for DataFrame index
    for i, index in enumerate(df.index):
        tk.Label(root, text=index, borderwidth=2, relief="solid", width=10, height=2).grid(row=i+1, column=0)

    # Display the DataFrame values in the grid
    for i in range(df.shape[0]):  # Rows
        for j in range(df.shape[1]):  # Columns
            cell_value = df.iloc[i, j]
            tk.Label(root, text=cell_value, borderwidth=2, relief="solid", width=10, height=2).grid(row=i+1, column=j+1)

    # Run the Tkinter main loop
    root.mainloop()

# Show the DataFrame using Tkinter GUI
show_dataframe_in_tkinter(df)