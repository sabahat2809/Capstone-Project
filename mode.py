import pandas as pd
import matplotlib.pyplot as plt 

df=pd.read_csv("world_happiness.csv")

mode_column= df["Log GDP per capita"].mode()[0]

print(f"Mode: {mode_column}")
