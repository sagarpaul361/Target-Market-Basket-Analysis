import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("Basket/Target.csv")

# Display basic information
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
print("\nFirst 5 Rows:")
print(df.head())
print("\nData Types:")
print(df.dtypes)
# Rename duplicate/misformatted column
df.columns.values[17] = "Personalized_Recommendation_Frequency_Rating"
# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("\nCleaned Column Names:")
print(df.columns.tolist())

# Check missing values
missing_values = df.isnull().sum()
# Check duplicate rows
duplicate_count = df.duplicated().sum()

print("\nNumber of duplicate rows:", duplicate_count)

print("\nMissing values in each column:")
print(missing_values)
# 4. Check unique values of categorical columns
categorical_columns = [
    "Gender",
    "Purchase_Frequency",
    "Purchase_Categories",
    "Personalized_Recommendation_Frequency",
    "Browsing_Frequency",
    "Product_Search_Method",
    "Search_Result_Exploration",
    "Add_to_Cart_Browsing",
    "Cart_Completion_Frequency",
    "Cart_Abandonment_Factors",
    "Saveforlater_Frequency",
    "Review_Left",
    "Review_Reliability",
    "Review_Helpfulness",
    "Recommendation_Helpfulness",
    "Service_Appreciation",
    "Improvement_Areas"
]

for column in categorical_columns:
    print("\n", column)
    print(df[column].unique())

# Remove extra spaces from string values
for column in categorical_columns:
    df[column] = df[column].str.strip()

# Standardize inconsistent category name
df["Product_Search_Method"] = df["Product_Search_Method"].replace(
    "categories", "Categories"
)

print("\nProduct Search Method after cleaning:")
print(df["Product_Search_Method"].unique())

print("\nService Appreciation after cleaning:")
print(df["Service_Appreciation"].unique())

# Handle missing values
df["Product_Search_Method"] = df["Product_Search_Method"].fillna("Unknown")

print("\nMissing values after handling:")
print(df.isnull().sum())

# Convert rating columns to numeric
numeric_columns = [
    "Customer_Reviews_Importance",
    "Personalized_Recommendation_Frequency_Rating",
    "Rating_Accuracy",
    "Shopping_Satisfaction"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

print("\nNumeric columns data types:")
print(df[numeric_columns].dtypes)
print("\nFinal Dataset Shape:", df.shape)

print("\nFinal Missing Values:")
print(df.isnull().sum().sum())

print("\nFinal Duplicate Rows:")
print(df.duplicated().sum())

df.to_csv("Basket/Target_Cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")

# TASK 2: DESCRIPTIVE BEHAVIOR ANALYSIS
# Age summary
print("\n===== AGE SUMMARY =====")
print(df["age"].describe())

print("\nMean Age:", round(df["age"].mean(), 2))
print("Median Age:", df["age"].median())
print("Minimum Age:", df["age"].min())
print("Maximum Age:", df["age"].max())
# Gender distribution
gender_counts = df["Gender"].value_counts()

print("\n===== GENDER DISTRIBUTION =====")
print(gender_counts)

print("\nGender Percentage:")
print((gender_counts / len(df) * 100).round(2))
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))

gender_counts.plot(kind="bar")

plt.title("Customer Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

plt.hist(df["age"], bins=10)

plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()
# Purchase frequency
purchase_frequency = df["Purchase_Frequency"].value_counts()

print("\n===== PURCHASE FREQUENCY =====")
print(purchase_frequency)

print("\nPurchase Frequency Percentage:")
print((purchase_frequency / len(df) * 100).round(2))

plt.figure(figsize=(9, 5))

purchase_frequency.plot(kind="bar")

plt.title("Customer Purchase Frequency")
plt.xlabel("Purchase Frequency")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

category_counts = (
    df["Purchase_Categories"]
    .str.split(";")
    .explode()
    .str.strip()
    .value_counts()
)

print("\n===== PRODUCT CATEGORY POPULARITY =====")
print(category_counts)

category_percentage = (
    category_counts / len(df) * 100
).round(2)

print("\nProduct Category Percentage:")
print(category_percentage)
plt.figure(figsize=(10, 6))

category_counts.plot(kind="bar")

plt.title("Most Popular Product Categories")
plt.xlabel("Product Category")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Browsing frequency
browsing_frequency = df["Browsing_Frequency"].value_counts()

print("\n===== BROWSING FREQUENCY =====")
print(browsing_frequency)

print("\nBrowsing Frequency Percentage:")
print((browsing_frequency / len(df) * 100).round(2))
plt.figure(figsize=(9, 5))

browsing_frequency.plot(kind="bar")

plt.title("Customer Browsing Frequency")
plt.xlabel("Browsing Frequency")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
# Cart abandonment factors
abandonment_factors = df["Cart_Abandonment_Factors"].value_counts()

print("\n===== CART ABANDONMENT FACTORS =====")
print(abandonment_factors)

print("\nCart Abandonment Percentage:")
print((abandonment_factors / len(df) * 100).round(2))
plt.figure(figsize=(10, 6))

abandonment_factors.plot(kind="bar")

plt.title("Cart Abandonment Factors")
plt.xlabel("Abandonment Factor")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()

numeric_analysis_columns = [
    "Customer_Reviews_Importance",
    "Personalized_Recommendation_Frequency_Rating",
    "Rating_Accuracy",
    "Shopping_Satisfaction"
]

print("\n===== NUMERICAL SUMMARY =====")

for column in numeric_analysis_columns:
    print("\n", column)
    print("Mean:", round(df[column].mean(), 2))
    print("Median:", df[column].median())
    print("Minimum:", df[column].min())
    print("Maximum:", df[column].max())

# Shopping Satisfaction Distribution

satisfaction_counts = df["Shopping_Satisfaction"].value_counts().sort_index()

print("\n===== SHOPPING SATISFACTION DISTRIBUTION =====")
print(satisfaction_counts)

plt.figure(figsize=(8, 5))

satisfaction_counts.plot(kind="bar")

plt.title("Shopping Satisfaction Distribution")
plt.xlabel("Shopping Satisfaction Rating")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Recommendation Helpfulness vs Shopping Satisfaction

recommendation_satisfaction = pd.crosstab(
    df["Recommendation_Helpfulness"],
    df["Shopping_Satisfaction"]
)

print("\n===== RECOMMENDATION HELPFULNESS VS SATISFACTION =====")
print(recommendation_satisfaction)

plt.figure(figsize=(9, 5))

recommendation_satisfaction.plot(kind="bar")

plt.title("Recommendation Helpfulness vs Shopping Satisfaction")
plt.xlabel("Recommendation Helpfulness")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# TASK 3: CUSTOMER SEGMENTATION AND PROFILING
# Convert purchase frequency into numerical scores

purchase_frequency_mapping = {
    "Less than once a month": 1,
    "Once a month": 2,
    "Few times a month": 3,
    "Once a week": 4,
    "Multiple times a week": 5
}

df["Purchase_Frequency_Score"] = df["Purchase_Frequency"].map(
    purchase_frequency_mapping
)

print("\n===== PURCHASE FREQUENCY SCORES =====")
print(
    df[
        ["Purchase_Frequency", "Purchase_Frequency_Score"]
    ].head(10)
)

print("\nMissing Purchase Frequency Scores:")
print(df["Purchase_Frequency_Score"].isnull().sum())

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
clustering_data = df[
    [
        "Purchase_Frequency_Score",
        "Shopping_Satisfaction"
    ]
].copy()

print("\n===== CLUSTERING DATA =====")
print(clustering_data.head())


# Standardize the data

scaler = StandardScaler()

scaled_data = scaler.fit_transform(clustering_data)

print("\nScaled data created successfully!")
inertia = []

for k in range(2, 7):
    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

print("\n===== ELBOW METHOD =====")

for k, value in zip(range(2, 7), inertia):
    print("K =", k, "Inertia =", round(value, 2))
plt.figure(figsize=(8, 5))

plt.plot(range(2, 7), inertia, marker="o")

plt.title("Elbow Method for Optimal Number of Clusters")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")

plt.xticks(range(2, 7))
plt.tight_layout()
plt.show()

# K-MEANS CUSTOMER SEGMENTATION
# ==================================================

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(scaled_data)

print("\n===== CLUSTER DISTRIBUTION =====")
print(df["Cluster"].value_counts().sort_index())

# Cluster profile
cluster_profile = df.groupby("Cluster")[
    [
        "Purchase_Frequency_Score",
        "Shopping_Satisfaction"
    ]
].mean().round(2)

print("\n===== CLUSTER PROFILE =====")
print(cluster_profile)
# Assign meaningful customer segment names

segment_names = {
    0: "Frequent & Satisfied Buyers",
    1: "At-Risk / Low-Engagement Customers",
    2: "Frequent but Dissatisfied Buyers",
    3: "Occasional & Highly Satisfied Shoppers"
}

df["Customer_Segment"] = df["Cluster"].map(segment_names)

print("\n===== CUSTOMER SEGMENTS =====")
print(df["Customer_Segment"].value_counts())
segment_profile = df.groupby("Customer_Segment").agg(
    Customers=("Customer_Segment", "count"),
    Avg_Purchase_Frequency=("Purchase_Frequency_Score", "mean"),
    Avg_Satisfaction=("Shopping_Satisfaction", "mean"),
    Avg_Age=("age", "mean")
).round(2)

segment_profile["Percentage"] = (
    segment_profile["Customers"] / len(df) * 100
).round(2)

print("\n===== FINAL CUSTOMER SEGMENT PROFILE =====")
print(segment_profile)
# Average age by segment
age_by_segment = df.groupby("Customer_Segment")["age"].mean().round(2)

print("\n===== AVERAGE AGE BY SEGMENT =====")
print(age_by_segment)


# Gender distribution by segment
gender_by_segment = pd.crosstab(
    df["Customer_Segment"],
    df["Gender"]
)

print("\n===== GENDER DISTRIBUTION BY SEGMENT =====")
print(gender_by_segment)

# Browsing frequency by segment

browsing_by_segment = pd.crosstab(
    df["Customer_Segment"],
    df["Browsing_Frequency"]
)

print("\n===== BROWSING FREQUENCY BY SEGMENT =====")
print(browsing_by_segment)
# CUSTOMER SEGMENT VISUALIZATION
# ==================================================

segment_counts = df["Customer_Segment"].value_counts()

plt.figure(figsize=(10, 6))

segment_counts.plot(kind="bar")

plt.title("Customer Segment Distribution")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=30, ha="right")

plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 6))

plt.scatter(
    df["Purchase_Frequency_Score"],
    df["Shopping_Satisfaction"],
    c=df["Cluster"]
)

plt.title("Customer Segmentation: Purchase Frequency vs Satisfaction")
plt.xlabel("Purchase Frequency Score")
plt.ylabel("Shopping Satisfaction")

plt.xticks([1, 2, 3, 4, 5])
plt.yticks([1, 2, 3, 4, 5])

plt.tight_layout()
plt.show()

# TASK 4: RECOMMENDATION AND REVIEW INSIGHTS
# Part 1: Recommendation Helpfulness vs Satisfaction

recommendation_satisfaction = df.groupby(
    "Recommendation_Helpfulness"
)["Shopping_Satisfaction"].agg(
    ["count", "mean", "median"]
).round(2)

print("\n===== RECOMMENDATION HELPFULNESS VS SATISFACTION =====")
print(recommendation_satisfaction)

plt.figure(figsize=(8, 5))

df.groupby(
    "Recommendation_Helpfulness"
)["Shopping_Satisfaction"].mean().plot(kind="bar")

plt.title("Recommendation Helpfulness vs Shopping Satisfaction")
plt.xlabel("Recommendation Helpfulness")
plt.ylabel("Average Shopping Satisfaction")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
# Review reliability vs rating accuracy

review_reliability_rating = df.groupby(
    "Review_Reliability"
)["Rating_Accuracy"].agg(
    ["count", "mean", "median"]
).round(2)

print("\n===== REVIEW RELIABILITY VS RATING ACCURACY =====")
print(review_reliability_rating)

plt.figure(figsize=(9, 5))

df.groupby(
    "Review_Reliability"
)["Rating_Accuracy"].mean().plot(kind="bar")

plt.title("Review Reliability vs Rating Accuracy")
plt.xlabel("Review Reliability")
plt.ylabel("Average Rating Accuracy")
plt.xticks(rotation=30)

plt.tight_layout()
plt.show()
review_helpfulness_rating = df.groupby(
    "Review_Helpfulness"
)["Rating_Accuracy"].agg(
    ["count", "mean", "median"]
).round(2)

print("\n===== REVIEW HELPFULNESS VS RATING ACCURACY =====")
print(review_helpfulness_rating)
plt.figure(figsize=(8, 5))

df.groupby(
    "Review_Helpfulness"
)["Rating_Accuracy"].mean().plot(kind="bar")

plt.title("Review Helpfulness vs Rating Accuracy")
plt.xlabel("Review Helpfulness")
plt.ylabel("Average Rating Accuracy")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Personalized recommendation engagement

recommendation_frequency = (
    df["Personalized_Recommendation_Frequency"]
    .value_counts()
)

print("\n===== PERSONALIZED RECOMMENDATION ENGAGEMENT =====")
print(recommendation_frequency)

print("\nPercentage:")
print(
    (recommendation_frequency / len(df) * 100).round(2)
)
plt.figure(figsize=(8, 5))

recommendation_frequency.plot(kind="bar")

plt.title("Personalized Recommendation Engagement")
plt.xlabel("Personalized Recommendation Frequency")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# TASK 5: VISUALIZATION AND REPORTING
# 1. Purchase Category Visualization

category_counts = (
    df["Purchase_Categories"]
    .str.split(";")
    .explode()
    .str.strip()
    .value_counts()
)

plt.figure(figsize=(10, 6))

category_counts.plot(kind="bar")

plt.title("Most Popular Product Categories", fontsize=14)
plt.xlabel("Product Category")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()
# 2. Browsing Frequency Visualization

browsing_counts = df["Browsing_Frequency"].value_counts()

plt.figure(figsize=(9, 6))

browsing_counts.plot(kind="bar")

plt.title("Customer Browsing Frequency", fontsize=14)
plt.xlabel("Browsing Frequency")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()

# 3. Shopping Satisfaction Visualization

satisfaction_counts = (
    df["Shopping_Satisfaction"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(8, 5))

satisfaction_counts.plot(kind="bar")

plt.title("Shopping Satisfaction Distribution", fontsize=14)
plt.xlabel("Shopping Satisfaction Rating")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# 4. Recommendation Helpfulness vs Shopping Satisfaction

recommendation_satisfaction = pd.crosstab(
    df["Recommendation_Helpfulness"],
    df["Shopping_Satisfaction"]
)

recommendation_satisfaction.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title(
    "Recommendation Helpfulness vs Shopping Satisfaction",
    fontsize=14
)

plt.xlabel("Recommendation Helpfulness")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.legend(
    title="Shopping Satisfaction",
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)

plt.tight_layout()
plt.show()

# 5. Customer Segment Distribution

segment_counts = df["Customer_Segment"].value_counts()

plt.figure(figsize=(10, 6))

segment_counts.plot(kind="bar")

plt.title("Customer Segment Distribution", fontsize=14)
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=30, ha="right")

plt.tight_layout()
plt.show()

# 6. Cart Abandonment Factors

abandonment_counts = (
    df["Cart_Abandonment_Factors"]
    .value_counts()
)

plt.figure(figsize=(10, 6))

abandonment_counts.plot(kind="bar")

plt.title("Cart Abandonment Factors", fontsize=14)
plt.xlabel("Cart Abandonment Factor")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()