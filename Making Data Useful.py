import pandas as pd

df = pd.read_csv(r"C:\Users\rajsa\OneDrive\Documents\Python\DATA CLEANING USING PYTHON (PROJECT)\cleaned_health_data.csv")


# 1. Remove leading and trailing spaces from the data values
df['Year'] = df['Year'].astype(str).str.strip()

# 2. Convert to numeric, turning any truly non-numeric text to NaN 
# (This prevents a crash if there's a typo like '2022a')
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# 3. Fill any NaNs with a default value (like 0) so you don't have to drop the row
df['Year'] = df['Year'].fillna(0)

# 4. Now convert to integer
df['Year'] = df['Year'].astype(int)

print(df['Year'].dtype)

# Calculate the average Life Expectancy and GDP per year
year_summary = df.groupby(['Year','Country'])['Life_Expectancy'].mean()

print("Yearly Averages:")
print(year_summary)

# Only rows for India
india_data = df[df['Country'] == 'India']
print("Health Data of India:")
print(india_data)

# # Only rows where Life Expectancy is above 75
high_life_exp = df[df['Life_Expectancy'] > 75]
print("High Life Expectancy:") 
print(high_life_exp)

# # High Life Expectancy AND high Hospital Beds in the year 2024
top_tier_2024 = df[(df['Life_Expectancy'] > 70) & 
                         (df['Hospital_Beds_Per_1000'] > 5) & 
                         (df['Year'] == 2024)]
print('High Life Expectancy AND high Hospital Beds in the year 2024:')
print(top_tier_2024)

print(df.describe())