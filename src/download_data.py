from sklearn.datasets import fetch_california_housing
import pandas as pd

# Load the California Housing dataset
housing = fetch_california_housing(as_frame=True)

# Create a DataFrame
df = housing.frame

# Save the dataset as a CSV file
df.to_csv("data/housing.csv", index=False)

print("Dataset downloaded successfully!")
print(f"Dataset shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())