This project involves a comprehensive data cleaning and exploratory analysis of a global health dataset containing 1,500 entries. 
The raw data was "dirty," containing inconsistencies in naming, mathematical errors (infinite and negative values), and missing records. I developed a Python-based pipeline to standardize this data and analyze global health trends, specifically focusing on India’s healthcare standing.

Data Cleaning Steps:
I handled several critical data quality issues using the Pandas and NumPy libraries:
String Standardization: Corrected misspelled "India" entries and removed hidden whitespaces from column headers and categorical values using .str.strip().
Infinite Value Handling: Detected and replaced inf values (caused by division-by-zero errors in the raw data) with the column median using np.isinf() and .replace().
Negative Value Correction: Identified illogical negative values in numeric columns (like Salary or Population) and replaced them with the mean using np.where().
Missing Data Imputation: Handled null values by applying column-specific mean/median strategies to maintain data integrity.
Type Conversion: Converted columns from object strings to appropriate integer and float types for mathematical analysis.

Key Analysis & Insights:
After cleaning, I performed a year-wise analysis to track global health metrics:
Yearly Trends: Analyzed the mean Life Expectancy over time across multiple countries using .groupby('Year').
India Deep Dive: Filtered data specifically for India to track its healthcare trajectory.
2024 Healthcare Standing: India's Life Expectancy: 76 years.
                          Hospital Beds          : 9 beds per 1000 people.
Statistical Summary: Generated full summary statistics (mean, standard deviation, quartiles) to understand the distribution of global health wealth
