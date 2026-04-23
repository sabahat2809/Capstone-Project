import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("world_happiness.csv")

# Sort and select top 15
top15 = df.sort_values(by="Log GDP per capita", ascending=False).head(15)

# Bar chart
plt.figure()
plt.bar(top15["Country name"], top15["Log GDP per capita"])

plt.title("Top 15 Wealthiest Countries (Log GDP per Capita)")
plt.xlabel("Country")
plt.ylabel("Log GDP per Capita")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()