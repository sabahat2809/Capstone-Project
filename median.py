import pandas as pd
import matplotlib.pyplot as plt 

df= pd.read_csv("world_happiness.csv")

median_column= df["Log GDP per capita"].median()

print(f"Median: {median_column:.2f}") 