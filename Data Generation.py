import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)

# 1. Setup Base Data
countries = ['USA', 'India', 'China', 'Brazil', 'Nigeria', 'Germany', 'Japan', 'UK', 'France', 'Russia']
years = list(range(2010, 2025))
n_rows = 1500

data = []

# 2. Generate 1500 rows of random data
for _ in range(n_rows):
    row = {
        'Country': random.choice(countries),
        'Year': random.choice(years),
        'GDP_Billion': np.random.uniform(200, 20000),
        'Population_Million': np.random.uniform(10, 1400),
        'Life_Expectancy': np.random.uniform(50, 90),
        'Hospital_Beds_Per_1000': np.random.uniform(1, 10)
    }
    data.append(row)

df = pd.DataFrame(data)

# 3. 🧪 INJECTING ERRORS (The "Dirty" Work)

# A. Spelling Mismatches (Categorical)
# We confuse "India" with typos
dirty_indies = ['Indai', 'india ', 'Inida', 'INDIA'] 
random_indices = np.random.choice(df.index, size=50, replace=False)
df.loc[random_indices, 'Country'] = np.random.choice(dirty_indies, size=50)

# B. Missing Values (Nulls)
# Randomly delete data in GDP and Life Expectancy
for col in ['GDP_Billion', 'Life_Expectancy']:
    mask = np.random.rand(len(df)) < 0.15  # 15% missing
    df.loc[mask, col] = np.nan

# C. Negative Values (Impossible Logic)
# Population cannot be negative
neg_mask = np.random.rand(len(df)) < 0.05
df.loc[neg_mask, 'Population_Million'] = df.loc[neg_mask, 'Population_Million'] * -1

# D. Infinities (Math Errors)
# Simulate division by zero errors in Hospital Beds
inf_mask = np.random.rand(len(df)) < 0.02
df.loc[inf_mask, 'Hospital_Beds_Per_1000'] = np.inf

# E. Outliers (Statistical Anomalies)
# Create a few "super rich" fake entries
outlier_mask = np.random.choice(df.index, size=10, replace=False)
df.loc[outlier_mask, 'GDP_Billion'] = 10000000  # Impossible GDP

# F. Data Type Errors (String in Numbers)
# Change 'Year' to object by adding text
str_mask = np.random.choice(df.index, size=20, replace=False)
df['Year'] = df['Year'].astype(str) # Convert all to string first
df.loc[str_mask, 'Year'] = "2020_est" # Add text pollution

# G. Duplicates
# Duplicate the first 50 rows and append them
df = pd.concat([df, df.iloc[:50]], ignore_index=True)

# 4. Save and View
df.to_csv('dirty_health_data.csv', index=False)
print(f"Dataset Generated! Shape: {df.shape}")
print("First 5 rows with potential errors:")
print(df.head())