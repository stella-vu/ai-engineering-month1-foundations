import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('data/budgetwise_synthetic_cleaned.csv')

# Get unique categories
categories = sorted(df['category'].dropna().unique())

# Save the categories to a csv file
pd.DataFrame(categories, columns=['category_name']).to_csv('data/categories.csv', index=False)
