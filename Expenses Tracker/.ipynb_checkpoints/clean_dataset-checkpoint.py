import pandas as pd

df = pd.read_csv('budgetwise_synthetic_dirty.csv')

print(df.shape)
print(df.isnull().sum())

