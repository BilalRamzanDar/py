import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the breast cancer wisconsin dataset
breast_cancer_dataset = load_breast_cancer()
data_frame = pd.DataFrame(breast_cancer_dataset.data, columns=breast_cancer_dataset.feature_names)
data_frame['label'] = breast_cancer_dataset.target

# Split the data into features (x) and target (y)
x = data_frame.drop(columns='label')
y = data_frame['label']

# Scale the data
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=2)

# Create a logistic regression model
model = LogisticRegression(max_iter=1000)  # Increase max_iter value
model.fit(x_train, y_train)

# Create the GUI
window = tk.Tk()
window.title("Breast Cancer Classification")
window.geometry("400x400")

# Create a canvas with scrollbars
canvas = tk.Canvas(window)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(window, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

def predict():
    # Get the input data from the entry fields
    input_data = [float(entry.get()) for entry in entries]
    input_data = np.array([input_data])
    input_data_scaled = scaler.transform(input_data)

    # Make predictions with the input data
    prediction = model.predict(input_data_scaled)

    # Show the predicted label in a message box
    messagebox.showinfo("Prediction Result", f"The predicted label is: {prediction[0]}")

# Create labels and entry fields for input features
labels = ['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4', 'Feature 5',
          'Feature 6', 'Feature 7', 'Feature 8', 'Feature 9', 'Feature 10',
          'Feature 11', 'Feature 12', 'Feature 13', 'Feature 14', 'Feature 15',
          'Feature 16', 'Feature 17', 'Feature 18', 'Feature 19', 'Feature 20',
          'Feature 21', 'Feature 22', 'Feature 23', 'Feature 24', 'Feature 25',
          'Feature 26', 'Feature 27', 'Feature 28', 'Feature 29', 'Feature 30']

entries = []
for i in range(len(labels)):
    label = tk.Label(frame, text=labels[i])
    label.grid(row=i, column=0, padx=10, pady=5)