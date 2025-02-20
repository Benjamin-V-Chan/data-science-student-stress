import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("../outputs/cleaned_data.csv")

# Histograms for each variable
for col in df.columns:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], kde=True, bins=10)
    plt.title(f"Distribution of {col}")
    plt.savefig(f"../outputs/{col}_histogram.png")
    plt.close()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.savefig("../outputs/correlation_heatmap.png")
plt.close()

print("Visualization complete. Plots saved.")
