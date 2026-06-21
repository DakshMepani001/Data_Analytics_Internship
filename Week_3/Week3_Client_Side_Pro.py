# Analysis of sample complete data ,which is created by own using pandas and numpy library. 

import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha", "Riya"],
    "Department": ["IT", "IT", "HR", "HR", "IT"],
    "Marks": [85, np.nan, 78, 88, 92] #np.nan means null value
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Remove missing values
df = df.dropna()

print("\nCleaned Dataset:")
print(df)

# Overall average
print("\nOverall Average Marks:")
print(df["Marks"].mean())

# Department-wise average
print("\nDepartment-wise Average Marks:")
print(df.groupby("Department")["Marks"].mean())