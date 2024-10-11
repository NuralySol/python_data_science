import pandas as pd  # Import pandas
import numpy as np   # Import numpy

# Step 1: Create an 8x8 array using NumPy
chess_board_array = np.zeros((8, 8), dtype=str)

# Step 2: Fill the array with chessboard pattern (alternating "white" and "black" cells)
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            chess_board_array[i, j] = "white"
        else:
            chess_board_array[i, j] = "black"

# Step 3: Convert the array to a Pandas DataFrame
chess_board_df = pd.DataFrame(chess_board_array)

# Step 4: Label the rows and columns for better readability (e.g., 1-8 for rows, A-H for columns)
chess_board_df.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
chess_board_df.index = [8, 7, 6, 5, 4, 3, 2, 1]

# Step 5: Display the DataFrame
print(chess_board_df)

