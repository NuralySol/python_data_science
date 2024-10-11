import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTableWidget, QTableWidgetItem, QMessageBox

# Define the main GUI class that inherits from QWidget
class PandasGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize layout and widgets
        self.layout = QVBoxLayout()

        self.label = QLabel("Pandas DataFrame GUI")
        self.layout.addWidget(self.label)

        self.load_csv_button = QPushButton("Load CSV")
        self.load_csv_button.clicked.connect(self.load_csv)
        self.layout.addWidget(self.load_csv_button)

        self.load_json_button = QPushButton("Load JSON")
        self.load_json_button.clicked.connect(self.load_json)
        self.layout.addWidget(self.load_json_button)

        self.show_button = QPushButton("Show DataFrame")
        self.show_button.clicked.connect(self.show_dataframe)
        self.layout.addWidget(self.show_button)

        self.describe_button = QPushButton("Describe DataFrame")
        self.describe_button.clicked.connect(self.describe_dataframe)
        self.layout.addWidget(self.describe_button)

        self.save_csv_button = QPushButton("Save DataFrame as CSV")
        self.save_csv_button.clicked.connect(self.save_csv)
        self.layout.addWidget(self.save_csv_button)

        self.save_json_button = QPushButton("Save DataFrame as JSON")
        self.save_json_button.clicked.connect(self.save_json)
        self.layout.addWidget(self.save_json_button)

        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        self.setLayout(self.layout)
        self.df = None  # Store the DataFrame

    def load_csv(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if file_name:
            self.df = pd.read_csv(file_name)
            QMessageBox.information(self, "Success", "CSV loaded successfully!")
        else:
            QMessageBox.warning(self, "Error", "Failed to load CSV file.")

    def load_json(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open JSON", "", "JSON Files (*.json)")
        if file_name:
            try:
                self.df = pd.read_json(file_name)
                QMessageBox.information(self, "Success", "JSON loaded successfully!")
            except ValueError as e:
                QMessageBox.warning(self, "Error", f"Error loading JSON file: {e}")
        else:
            QMessageBox.warning(self, "Error", "Failed to load JSON file.")

    def show_dataframe(self):
        if self.df is not None:
            self.display_table(self.df)
        else:
            QMessageBox.warning(self, "Error", "No DataFrame loaded.")

    def describe_dataframe(self):
        if self.df is not None:
            description = self.df.describe()
            self.display_table(description)
        else:
            QMessageBox.warning(self, "Error", "No DataFrame loaded.")

    def save_csv(self):
        if self.df is not None:
            try:
                self.df.to_csv("saved_dataframe.csv", index=False)
                QMessageBox.information(self, "Success", "DataFrame saved as CSV successfully!")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to save CSV: {e}")
        else:
            QMessageBox.warning(self, "Error", "No DataFrame to save!")

    def save_json(self):
        if self.df is not None:
            try:
                self.df.to_json("saved_dataframe.json", orient="records", indent=4)
                QMessageBox.information(self, "Success", "DataFrame saved as JSON successfully!")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to save JSON: {e}")
        else:
            QMessageBox.warning(self, "Error", "No DataFrame to save!")

    def display_table(self, df):
        self.table_widget.setRowCount(df.shape[0])
        self.table_widget.setColumnCount(df.shape[1])
        self.table_widget.setHorizontalHeaderLabels(df.columns)

        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

# Initialize the PyQt5 app
app = QApplication(sys.argv)
window = PandasGUI()
window.setWindowTitle("Pandas DataFrame GUI")
window.resize(600, 400)
window.show()
sys.exit(app.exec_())

#! This PyQt5-based GUI application allows users to load, display, describe, and save pandas DataFrames, either from CSV or JSON files. Here’s a detailed breakdown of its functionality:

# 	•	GUI Components: The application provides several buttons and a table widget to interact with the DataFrame:
# 	•	Load CSV: Opens a file dialog for the user to select and load a CSV file into a pandas DataFrame. The loaded data is stored in the df attribute.
# 	•	Load JSON: Similar to CSV loading, this button allows the user to load data from a JSON file.
# 	•	Show DataFrame: Displays the current DataFrame in the table widget. If no DataFrame is loaded, an error message is shown.
# 	•	Describe DataFrame: Calculates summary statistics of the DataFrame (like mean, count, std) using pandas’ describe() method and displays the result.
# 	•	Save as CSV: Saves the current DataFrame as a CSV file (saved_dataframe.csv). If no DataFrame is loaded, an error message is shown.
# 	•	Save as JSON: Saves the current DataFrame as a JSON file (saved_dataframe.json). Again, if no DataFrame is loaded, an error message is shown.
# 	•	Error Handling: The application makes extensive use of error handling with message boxes. For instance, if a file fails to load or the DataFrame is empty, it alerts the user with appropriate error messages.
# 	•	Data Display: When the DataFrame is loaded or described, the display_table() method fills the table widget with the contents of the DataFrame. The table widget automatically adjusts based on the number of rows and columns in the DataFrame.
# 	•	Code Structure:
# 	•	The application is built around the PandasGUI class, which defines the layout and functionality of the GUI.
# 	•	The PyQt5 event system is used to link buttons to their corresponding functions (e.g., load_csv(), show_dataframe()).
# 	•	Integration with pandas: The app leverages pandas for data manipulation and the PyQt5 framework for building the GUI. It seamlessly connects pandas DataFrames with PyQt5 widgets for data handling and display.
# 	•	User Experience: This GUI makes it easy for users to handle data without coding. It is interactive, intuitive, and supports fundamental data operations like loading, displaying, and saving DataFrames.

# This is a lightweight data analysis tool for quick inspection and manipulation of CSV and JSON files, perfect for users who need basic data operations with a graphical interface.