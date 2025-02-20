import pandas as pd

# Load dataset
file_path = "../data/Student_Stress_Factors.csv"
df = pd.read_csv(file_path)

# Rename columns for clarity
df.columns = [
    "Sleep_Quality",
    "Headache_Frequency",
    "Academic_Performance",
    "Study_Load",
    "Extracurricular_Activity",
    "Stress_Levels"
]

# Save cleaned dataset
df.to_csv("../outputs/cleaned_data.csv", index=False)
print("Preprocessing complete. Cleaned data saved.")
