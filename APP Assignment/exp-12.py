
# Experiment No. 12
# Exploratory Data Analysis (EDA) on Customer Churn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create a sample customer churn dataset
np.random.seed(42)
n = 200

df = pd.DataFrame({
    "CustomerID": range(1, n + 1),
    "Age": np.random.randint(18, 70, n),
    "Tenure": np.random.randint(1, 72, n),
    "MonthlyCharges": np.random.uniform(20, 120, n).round(2),
    "TotalCharges": np.random.uniform(100, 8000, n).round(2),
    "Contract": np.random.choice(
        ["Month-to-month", "One year", "Two year"], n
    ),
    "InternetService": np.random.choice(
        ["DSL", "Fiber optic", "No"], n
    ),
    "Churn": np.random.choice(
        ["Yes", "No"], n, p=[0.30, 0.70]
    )
})

# Introduce missing values
df.loc[[5, 15, 25, 35], "Age"] = np.nan
df.loc[[10, 20, 30], "MonthlyCharges"] = np.nan
df.loc[[12, 22], "Contract"] = np.nan

print("Original Dataset:")
print(df.head())

# 2. Explore dataset structure
print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nColumn Names:")
print(df.columns.tolist())

# 3. Check and remove duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

df = df.drop_duplicates()

# 4. Identify missing values
print("\nMissing Values:")
print(df.isnull().sum())

print("\nMissing Value Percentage:")
print((df.isnull().mean() * 100).round(2))

# 5. Handle missing numerical values using median
numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Handle missing categorical values using mode
categorical_cols = df.select_dtypes(include="object").columns

for col in categorical_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 6. Generate summary statistics
print("\nNumerical Summary:")
print(df.describe().round(2))

print("\nCategorical Summary:")
print(df.describe(include="object"))

# 7. Calculate overall churn rate
churn_rate = df["Churn"].eq("Yes").mean() * 100

print("\nOverall Churn Rate:")
print(round(churn_rate, 2), "%")

# 8. Analyze churn by contract
print("\nChurn by Contract (%):")
contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100

print(contract_churn.round(2))

# 9. Analyze churn by internet service
print("\nChurn by Internet Service (%):")
service_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"],
    normalize="index"
) * 100

print(service_churn.round(2))

# 10. Compare numerical features by churn
print("\nAverage Customer Details by Churn:")
print(
    df.groupby("Churn")[
        ["Age", "Tenure", "MonthlyCharges", "TotalCharges"]
    ].mean().round(2)
)

# Set a consistent visualization style
sns.set_theme(style="whitegrid")

# 11. Visualization 1: Churn distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# 12. Visualization 2: Churn by contract
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Contract", hue="Churn")
plt.title("Customer Churn by Contract")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# 13. Visualization 3: Tenure and churn
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="Churn", y="Tenure")
plt.title("Tenure Distribution by Churn")
plt.xlabel("Churn")
plt.ylabel("Tenure (Months)")
plt.tight_layout()
plt.show()

# 14. Visualization 4: Monthly charges and churn
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="Churn", y="MonthlyCharges")
plt.title("Monthly Charges by Churn")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.show()

# 15. Visualization 5: Correlation heatmap
corr = df[
    ["Age", "Tenure", "MonthlyCharges", "TotalCharges"]
].corr()

plt.figure(figsize=(7, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 16. Identify patterns
print("\nPattern Analysis:")

print("\nChurn Rate by Contract (%):")
print(
    df.assign(ChurnFlag=df["Churn"].eq("Yes"))
    .groupby("Contract")["ChurnFlag"]
    .mean()
    .mul(100)
    .round(2)
)

print("\nAverage Tenure by Churn:")
print(df.groupby("Churn")["Tenure"].mean().round(2))

print("\nAverage Monthly Charges by Churn:")
print(df.groupby("Churn")["MonthlyCharges"].mean().round(2))

# 17. Save the cleaned dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nCleaned dataset saved successfully.")
