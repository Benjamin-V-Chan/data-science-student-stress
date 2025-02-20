import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../outputs/cleaned_data.csv")

# Compute correlation matrix
correlation_matrix = df.corr()

# Save correlation matrix
correlation_matrix.to_csv("../outputs/correlation_matrix.csv")
print("Correlation analysis complete. Results saved.")
