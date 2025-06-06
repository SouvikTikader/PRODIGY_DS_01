import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (skip metadata rows)
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_2590.csv", skiprows=4)

# Select year
year = "2023"
population_2023 = df[["Country Name", year]].dropna()

# 1. Bar Chart: Top 10 Most Populous Countries in 2023 
top_10 = population_2023.sort_values(by=year, ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_10["Country Name"], top_10[year], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title("Top 10 Most Populous Countries in 2023")
plt.xlabel("Country")
plt.ylabel("Population")
plt.tight_layout()
plt.savefig("top10_population_2023.png")
plt.show()

#  2. Histogram: Population Distribution (in Millions) 
plt.figure(figsize=(8, 5))
plt.hist(population_2023[year] / 1_000_000, bins=20, color='orange', edgecolor='black')
plt.title("Histogram of Country Populations (in millions) - 2023")
plt.xlabel("Population (Millions)")
plt.ylabel("Number of Countries")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("population_distribution_histogram_2023.png")
plt.show()
