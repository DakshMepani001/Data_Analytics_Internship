import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset: AI Student Impact Dataset
# Description:
# This dataset contains information about students' academic performance,
# AI tool usage, study habits, major categories, and skill levels.
#
# Key Columns:
# Student_ID               -> Unique student identifier
# Major_Category           -> Student's field of study
# Year_of_Study            -> Academic year (Freshman, Sophomore, etc.)
# Pre_Semester_GPA         -> GPA before the semester
# Weekly_GenAI_Hours       -> Hours spent using AI tools per week
# Primary_Use_Case         -> Main purpose of AI usage
# Prompt_Engineering_Skill -> AI prompting skill level
# Tool_Diversity           -> Number of different AI tools used
# Paid_Subscription        -> Whether the student uses paid AI services
# Traditional_Study_Hours  -> Weekly study hours without AI assistance

# Load dataset
df = pd.read_csv(
    "C:/Users/DELL/OneDrive/Documents/Internship/Week_4/ai_student_impact_dataset.csv"
)

print(df.info())
print(df.describe())

fig, axes = plt.subplots(2, 2, figsize=(16, 10))

plt.subplots_adjust(
    hspace=0.4,  # vertical space
    wspace=0.3   # horizontal space
)

# Histogram
axes[0,0].hist(df["Pre_Semester_GPA"], bins=20)
axes[0,0].set_title("GPA Distribution")
axes[0,0].set_xlabel("GPA")
axes[0,0].set_ylabel("Frequency")

# Scatter Plot
axes[0,1].scatter(
    df["Weekly_GenAI_Hours"],
    df["Pre_Semester_GPA"]
)
axes[0,1].set_title("GenAI Hours vs GPA")
axes[0,1].set_xlabel("Weekly GenAI Hours")
axes[0,1].set_ylabel("Pre Semester GPA")

# Bar Chart
avg_gpa = df.groupby("Major_Category")["Pre_Semester_GPA"].mean()
avg_gpa.plot(kind="bar", ax=axes[1,0])
axes[1,0].set_title("Average GPA by Major")
axes[1,0].set_xlabel("Major Category")
axes[1,0].set_ylabel("Average GPA")

# Boxplot
sns.boxplot(
    x="Major_Category",
    y="Pre_Semester_GPA",
    data=df,
    ax=axes[1,1]
)
axes[1,1].set_title("GPA by Major")
axes[1,1].set_xlabel("Major Category")
axes[1,1].set_ylabel("Pre Semester GPA")
axes[1,1].set_title("GPA by Major")

plt.tight_layout()
plt.savefig(
    "C:/Users/DELL/OneDrive/Documents/Internship/Week_4/week4_ Client_Side_Dashboard.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()