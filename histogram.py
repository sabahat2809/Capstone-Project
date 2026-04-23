import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("world_happiness.csv")

# Get top 15 wealthiest countries
top15 = df.sort_values(by="Log GDP per capita", ascending=False).head(15)

# Histogram for top 15
plt.figure()
plt.hist(top15["Log GDP per capita"], bins=10)

plt.title("Histogram of Top 15 Wealthiest Countries")
plt.xlabel("Log GDP per Capita")
plt.ylabel("Frequency")

plt.show()