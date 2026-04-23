import pandas as pd 

df=pd.read_csv("world_happiness.csv")

std_column= df["Log GDP per capita"].std()

print(f"Standard Deviation: {std_column:.2f}")
