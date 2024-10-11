
#! .ilock and lock methods Python Data Science
import threading
import pandas as pd
import time

# Shared resource: A bank account balance
balance = 1000

# Lock to prevent race condition
lock = threading.Lock()

def withdraw_money(amount):
    global balance
    with lock:
        if balance >= amount:
            print(f"Withdrawing {amount}")
            balance -= amount
            print(f"New balance: {balance}")
        else:
            print(f"Insufficient funds to withdraw {amount}")

# Simulate multiple threads withdrawing money
threads = []

for i in range(5):
    t = threading.Thread(target=withdraw_money, args=(300,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(f"Final balance: {balance}")


# Create a DataFrame with student names and scores
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 90, 95, 80, 75],
    'English': [88, 78, 84, 85, 92]
}

df = pd.DataFrame(data)

# Print the DataFrame
print("Original DataFrame:")
print(df)

# Select specific rows and columns using iloc
print("\nRow 0 (first row):")
print(df.iloc[0])  # First row (Alice)

print("\nFirst two rows:")
print(df.iloc[:2])  # First two rows

print("\nFirst two columns:")
print(df.iloc[:, :2])  # First two columns (Name and Math)

print("\nCell at row 1, column 2 (Bob's English score):")
print(df.iloc[1, 2])  # Bob's English score

print("\nSubset of rows and columns:")
print(df.iloc[1:4, 1:3])  # Rows 1 to 3 and columns 1 to 2 (Math and English)

# Create a DataFrame with student names and scores
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 90, 95, 80, 75],
    'English': [88, 78, 84, 85, 92]
}

df = pd.DataFrame(data)

# Lock to ensure thread-safe operations
lock = threading.Lock()

def process_row(row_index):
    global df
    with lock:
        # Simulate some processing (e.g., updating a score)
        print(f"Processing row {row_index} by {threading.current_thread().name}")
        df.iloc[row_index, 1] += 5  # Increase Math score by 5
        print(f"Updated row {row_index}: {df.iloc[row_index]}")

# Create threads to process different rows
threads = []
for i in range(len(df)):
    t = threading.Thread(target=process_row, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("\nFinal DataFrame after processing:")
print(df)