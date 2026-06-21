import numpy as np
import pandas as pd

# Student marks using NumPy
marks = np.array([85, 90, 78, 88, 95])

print("Original Marks:", marks)
print("Marks + 5 Bonus:", marks + 5)
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))

# Create Pandas DataFrame using dictionary
data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha", "Riya"],
    "Marks": marks
}

df = pd.DataFrame(data)

print("\nStudent Dataset:")
print(df)

# Filter students with marks above 80
high_scorers = df[df["Marks"] > 80]

print("\nStudents Scoring Above 80:")
print(high_scorers)

# Calculate average using Pandas
print("\nAverage Marks:", df["Marks"].mean())