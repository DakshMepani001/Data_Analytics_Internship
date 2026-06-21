import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# Week 4 Hands-On Project
# Health & Lifestyle Dataset Analysis
# ==========================================

# Dataset Description:
# This dataset contains information about sleep habits,
# exercise frequency, health scores, stress levels,
# mood scores, fitness levels, and wellness categories.
# The objective is to analyze relationships between
# lifestyle factors and overall health.

# Load Dataset
df = pd.read_csv("C:/Users/DELL/OneDrive/Documents/Internship/Week_4/early_wakeup_health_dataset.csv")

# Display Basic Information
print("\nDataset Information:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

# Set Seaborn Style
sns.set_style("whitegrid")

# Create Dashboard
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# 1. Health Score Distribution
axes[0,0].hist(
    df["Health_Score"],
    bins=20
)

axes[0,0].set_title("Health Score Distribution")
axes[0,0].set_xlabel("Health Score")
axes[0,0].set_ylabel("Frequency")


# 2. Sleep Duration vs Health Score
sns.scatterplot(
    data=df,
    x="Sleep_Duration_Hours",
    y="Health_Score",
    hue="Gender",
    ax=axes[0,1]
)

axes[0,1].set_title("Sleep Duration vs Health Score")

# 3. Average Health Score by Gender
gender_health = df.groupby("Gender")["Health_Score"].mean()

gender_health.plot(
    kind="bar",
    ax=axes[1,0]
)

axes[1,0].set_title("Average Health Score by Gender")
axes[1,0].set_xlabel("Gender")
axes[1,0].set_ylabel("Average Health Score")

# 4. Wellness Category Distribution
wellness = df["Wellness_Category"].value_counts()

wellness.plot(
    kind="bar",
    ax=axes[1,1]
)

axes[1,1].set_title("Wellness Category Distribution")
axes[1,1].set_xlabel("Category")
axes[1,1].set_ylabel("Count")

# Dashboard Layout
plt.tight_layout()

# Save Dashboard
plt.savefig(
    "C:/Users/DELL/OneDrive/Documents/Internship/Week_4/Week4_health_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nDashboard saved as: week4_health_dashboard.png")