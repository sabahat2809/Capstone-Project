import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('world_happiness.csv')

mean_column= df["Log GDP per capita"].mean() 

print(f"Mean: {mean_column:.2f}")