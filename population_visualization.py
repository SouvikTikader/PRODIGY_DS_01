import pandas as pd
import matplotlib.pyplot as plt

# Loading dataset
df = pd.read_csv("Dataset/API_SP.POP.TOTL_DS2_en_csv_v2_2590.csv", skiprows=4)

# Selecting year
year = "2023"
population_2023 = df[["Country Name", year]].dropna()

# Removed non-countries
non_countries = [
  "World","IDA & IBRD total","Low & middle income","Middle income","IBRD only","Early-demographic dividend","Lower middle income","Upper middle income","East Asia & Pacific","Late-demographic dividend","East Asia & Pacific (excluding high income)","East Asia & Pacific (IDA & IBRD countries)","South Asia","South Asia (IDA & IBRD)","IDA total","High income","OECD members","IDA only","Sub-Saharan Africa","Sub-Saharan Africa (IDA & IBRD countries)","Sub-Saharan Africa (excluding high income)","Least developed countries: UN classification","Post-demographic dividend","Pre-demographic dividend","Fragile and conflict affected situations","Europe & Central Asia","Heavily indebted poor countries (HIPC)","Africa Eastern and Southern","Low income","Latin America & Caribbean","Latin America & the Caribbean (IDA & IBRD countries)","IDA blend","Latin America & Caribbean (excluding high income)","Africa Western and Central","Middle East & North Africa","Arab World","Europe & Central Asia (IDA & IBRD countries)","Not classified","European Union","Middle East & North Africa (excluding high income)","Middle East & North Africa (IDA & IBRD countries)","North America","Euro area","Europe & Central Asia (excluding high income)"
]

population_2023 = population_2023[~population_2023['Country Name'].isin(non_countries)]



# 1. Bar Chart: Top 10 Most Populous Countries in 2023 
top_10 = population_2023.sort_values(by=year, ascending=False).head(10)
top_10[year] = top_10[year] / 1_000_000
plt.figure(figsize=(10, 6))
plt.bar(top_10["Country Name"], top_10[year], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title("Top 10 Most Populous Countries in 2023")
plt.xlabel("Country")
plt.ylabel("Population (Millions)")
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
