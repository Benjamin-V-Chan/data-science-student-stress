import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../outputs/cleaned_data.csv")

# Compute summary statistics
summary_stats = df.describe()

# Save statistics
summary_stats.to_csv("../outputs/summary_statistics.csv")
print("Exploratory analysis complete. Summary statistics saved.")
