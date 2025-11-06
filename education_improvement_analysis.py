

# This script analyzes global literacy rates and educational investment trends to identify factors that affect literacy improvement.

# Import necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set plot style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load dataset
file_path = "/home/fiyin/project_data/world-education-data.csv"
df = pd.read_csv(file_path)

print("Dataset loaded successfully!\n")
print(df.head())

# Check dataset info and missing values
print("\nChecking dataset information...\n")
df.info()

print("\nChecking for missing values...\n")
print(df.isnull().sum())

# Data cleaning
df.drop_duplicates(inplace=True)
df = df.dropna(subset=["lit_rate_adult_pct"])
df["year"] = df["year"].astype(int)

print("\nAfter cleaning:\n")
df.info()
df.to_csv("cleaned_world_education_data.csv", index=False)

# Summary statistics
print("\nSummary statistics:\n")
print(df.describe())

# Exploratory Data Analysis (EDA)
# Distribution of literacy rates
plt.figure()
sns.histplot(df["lit_rate_adult_pct"], bins=30, kde=True)
plt.title("Distribution of Adult Literacy Rates")
plt.xlabel("Adult Literacy Rate (%)")
plt.ylabel("Number of Countries")
plt.tight_layout()
plt.savefig("literacy_distribution.png")
plt.close()

# Literacy vs Government Spending
plt.figure()
sns.scatterplot(data=df, x="gov_exp_pct_gdp", y="lit_rate_adult_pct")
plt.title("Government Spending vs Adult Literacy Rate")
plt.xlabel("Education Expenditure (% of GDP)")
plt.ylabel("Adult Literacy Rate (%)")
plt.tight_layout()
plt.savefig("literacy_vs_spending.png")
plt.close()

# Correlation heatmap
plt.figure()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Key Variables")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

# Literacy rate trend for Nigeria
country_name = "Nigeria"
country_data = df[df["country"] == country_name]

if not country_data.empty:
    plt.figure()
    sns.lineplot(data=country_data, x="year", y="lit_rate_adult_pct", marker="o")
    plt.title(f"Literacy Rate Trend in {country_name}")
    plt.xlabel("Year")
    plt.ylabel("Literacy Rate (%)")
    plt.tight_layout()
    plt.savefig(f"literacy_trend_{country_name.lower()}.png")
    plt.close()

# Top 10 countries by literacy rate (latest year)
latest_year = df["year"].max()
top10 = df[df["year"] == latest_year].nlargest(10, "lit_rate_adult_pct")

plt.figure()
sns.barplot(data=top10, x="lit_rate_adult_pct", y="country", palette="Greens_r")
plt.title(f"Top 10 Countries by Literacy Rate ({latest_year})")
plt.xlabel("Adult Literacy Rate (%)")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("top10_literacy.png")
plt.close()

print("\nQuick Insights:")
print(f"- Number of countries: {df['country'].nunique()}")
print(f"- Years covered: {df['year'].min()} to {df['year'].max()}")
print(f"- Average global literacy rate: {round(df['lit_rate_adult_pct'].mean(), 2)}%")
print(f"- Average government spending on education: {round(df['gov_exp_pct_gdp'].mean(), 2)}% of GDP")

print("\nPossible Observations:")
print("- Countries with higher education spending tend to have better literacy rates.")
print("- Literacy rates have generally improved over time in most regions.")
print("- Some developing countries still show low literacy despite reasonable spending, suggesting other social factors play a role.")

print("\nAll visualizations and cleaned data have been saved in your current directory.")
print("Project completed successfully!")
