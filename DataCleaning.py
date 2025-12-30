"""Importing necessary libraries"""
import numpy as np
import pandas as pd

"""Loading dataset"""
df = pd.read_csv(r"C:\Users\rajsa\OneDrive\Documents\Python\DATA CLEANING USING PYTHON (PROJECT)\dirty_health_data.csv")
print(df.head())
print(df.tail())

"""Checking structure of dataset"""
print(df.info())
print(df.shape)

"""Checking Quality of data"""
print(df.describe())
print(df['Country'].value_counts())

"""Removing wrong spellings"""
# df.replace(["Inida","india","INDIA", "Indai"], "India" , inplace = True)
# print(df['Country'].value_counts())

"""Checking null values & duplicates"""
print(df.isnull().sum())
print(df.duplicated().sum())

"""Handling infinte values"""
df.replace([np.inf, -np.inf], np.nan, inplace = True)

"""Filling the null values"""
df['GDP_Billion'].fillna(df['GDP_Billion'].mean(), inplace = True)

df['Life_Expectancy'].fillna(df['Life_Expectancy'].median(), inplace = True)


"""Removing Negative values"""
df["Population_Million"] = np.where(df["Population_Million"]<0,df["Population_Million"].mean(),df["Population_Million"])


df["Hospital_Beds_Per_1000"].replace([np.inf,-np.inf], np.nan, inplace = True)
df["Hospital_Beds_Per_1000"].fillna(df["Hospital_Beds_Per_1000"].median(), inplace = True)
print(df["Hospital_Beds_Per_1000"].unique())

"""Round to 2 decimal places & convert to integers"""
df["GDP_Billion"]=df["GDP_Billion"].round(2).astype(int)
df["Population_Million"]=df["Population_Million"].round(2).astype(int)
df["Life_Expectancy"]=df["Life_Expectancy"].round(1).astype(int)
df["Hospital_Beds_Per_1000"]=df["Hospital_Beds_Per_1000"].round(0).astype(int)
print(df)

"""Saving the cleaned data"""
df.to_csv(r"C:\Users\rajsa\OneDrive\Documents\Python\DATA CLEANING USING PYTHON (PROJECT)\cleaned_health_data.csv", index = False)

print('Data cleaning completed! Saved as "cleaned_health_data.csv"')

