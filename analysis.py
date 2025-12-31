import pandas as pd

# Simple example dataset (economic-style)
data = {
    "year": [2020, 2021, 2022, 2023],
    "gdp_growth": [-3.4, 5.7, 2.1, 2.4]
}

df = pd.DataFrame(data)

# Basic analysis
average_growth = df["gdp_growth"].mean()

print("GDP Growth Data:")
print(df)
print("\nAverage GDP growth:", round(average_growth, 2), "%")
