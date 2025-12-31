import pandas as pd

data = {
  "Year" : [2020, 2021, 2022, 2023], 
  "GDP Growth": [-3.4, 5.9, 2.1, 2.5]
}

df = pd.DataFrame(data)
print("Sample GDP growth data:")
print(df)
