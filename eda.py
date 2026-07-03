import pandas as pd

# Load dataset
df = pd.read_csv("insurance.data.aggregated.csv")

print("\n========== FIRST FIVE ROWS ==========")
print(df.head())

print("\n========== DATASET INFORMATION ==========")
print(df.info())

print("\n========== COLUMN NAMES ==========")
print(df.columns)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== SUMMARY STATISTICS ==========")
print(df.describe())

print("\n========== MARKETING CHANNELS ==========")
print(df["Marketing Channel"].value_counts())

print("\n========== DEVICE TYPES ==========")
print(df["Device Category"].value_counts())

print("\n========== TOTAL REVENUE ==========")
print(df["Revenue"].sum())

print("\n========== AVERAGE REVENUE ==========")
print(df["Revenue"].mean())

print("\n========== TOTAL USERS ==========")
print(df["Users"].sum())

print("\n========== TOTAL QUOTES ==========")
print(df["TotalNumberOfInsuranceQuotes"].sum())

print("\n========== TOTAL POLICIES SOLD ==========")
print(df["TotalNumberOfInsurancePoliciesPurchaed"].sum())

print("\n========== CORRELATION ==========")

print("\n========== CORRELATION ==========")

print(df[[
    "Users",
    "Pages / Session",
    "Avg. Session Duration",
    "Revenue",
    "TotalNumberOfInsuranceQuotes",
    "TotalNumberOfInsurancePoliciesPurchaed"
]].corr())