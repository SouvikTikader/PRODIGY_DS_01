import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_2590.csv", skiprows=4)
meta = pd.read_csv("Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_2590.csv")

# Merge on Country Code
merged_df = df.merge(meta, on="Country Code")

# Select year
year = "2023"

# Filter needed columns
merged = merged_df[["Country Name", "Region", "IncomeGroup", year]].dropna()

# Convert population to millions for readability
merged[year] = merged[year] / 1_000_000

# --- 1. Bar Chart: Average Population by Region ---
region_avg = merged.groupby("Region")[year].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
region_avg.plot(kind="bar", color="lightgreen", edgecolor='black')
plt.title(f"Average Country Population by Region ({year})")
plt.ylabel("Average Population (Millions)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("avg_population_by_region.png")
plt.show()

# --- 2. Bar Chart: Average Population by Income Group ---
income_avg = merged.groupby("IncomeGroup")[year].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
income_avg.plot(kind="bar", color="lightcoral", edgecolor='black')
plt.title(f"Average Country Population by Income Group ({year})")
plt.ylabel("Average Population (Millions)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("avg_population_by_income_group.png")
plt.show()
