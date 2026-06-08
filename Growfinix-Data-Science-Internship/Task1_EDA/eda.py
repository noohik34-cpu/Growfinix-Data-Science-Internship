import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Task1_EDA/real_estate.csv", sep=";")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

# Price Distribution
plt.figure(figsize=(8,5))
df["price"].hist(bins=20)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.savefig("Task1_EDA/outputs/price_distribution.png")
plt.show()

print("\nEDA Completed Successfully")
