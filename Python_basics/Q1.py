import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data.csv")

# Check missing values
print(df.isnull().sum())

# Drop missing values
df_drop = df.dropna()

# Fill missing numerical values with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Fill categorical values with mode
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)

# Remove duplicates
df = df.drop_duplicates()
