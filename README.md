# Target Market Basket Analysis – Customer Behavior & Segmentation

## Project Overview
This project analyzes customer purchasing behavior, shopping satisfaction, browsing patterns, and personalized recommendation engagement using Python.

The analysis uses 800 customer survey responses across 24 columns. Data cleaning, exploratory data analysis, customer segmentation, and visualization were performed to identify actionable insights for customer engagement and retention.

## Objectives
- Clean and prepare customer survey data for analysis.
- Analyze customer demographics and purchase frequency.
- Identify popular product categories and cart abandonment factors.
- Segment customers using K-Means clustering.
- Examine relationships between recommendation helpfulness, shopping satisfaction, review reliability, and rating accuracy.
- Generate data-driven recommendations for improving customer experience.

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- K-Means Clustering
- Jupyter Notebook / VS Code

## Project Workflow

### 1. Data Cleaning & Preparation
- Standardized column names and categorical values.
- Handled missing values in product search methods.
- Converted rating columns to numeric data types.
- Checked duplicate records and data consistency.

### 2. Exploratory Data Analysis
- Analyzed customer age and gender distributions.
- Examined purchase frequency and popular product categories.
- Investigated browsing behavior and cart abandonment factors.
- Summarized shopping satisfaction and recommendation-related ratings.

### 3. Customer Segmentation
Applied K-Means clustering using purchase frequency scores and shopping satisfaction.

Four customer segments were identified:

| Customer Segment | Customers | Percentage |
|---|---:|---:|
| At-Risk / Low-Engagement Customers | 236 | 29.5% |
| Frequent but Dissatisfied Buyers | 202 | 25.3% |
| Occasional & Highly Satisfied Shoppers | 183 | 22.9% |
| Frequent & Satisfied Buyers | 179 | 22.4% |

### 4. Recommendation & Review Analysis
- Examined recommendation helpfulness against shopping satisfaction.
- Analyzed review reliability and product rating accuracy.
- Explored personalized recommendation engagement.

### 5. Visualization & Reporting
Created charts to communicate customer demographics, purchase frequency, product categories, shopping satisfaction, cart abandonment, and customer segments.

## Key Findings
- **Customer dataset:** 800 survey responses and 24 columns.
- **Popular categories:** Beauty & Personal Care and Clothing & Fashion were among the leading product categories.
- **Cart abandonment:** High shipping costs were the most frequently reported factor, with 216 responses.
- **Largest segment:** At-Risk / Low-Engagement Customers represented 29.5% of the dataset.
- **Retention opportunity:** Frequent but Dissatisfied Buyers represented 202 customers and may benefit from initiatives focused on improving satisfaction.
- **Loyalty opportunity:** Frequent & Satisfied Buyers represented 179 customers and may respond well to retention and loyalty initiatives.

## Recommendations
- Investigate shipping costs and their impact on cart abandonment.
- Develop re-engagement strategies for low-engagement customers.
- Investigate the causes of dissatisfaction among frequent buyers.
- Strengthen personalized recommendations and review transparency.
- Use customer segments to guide targeted marketing and retention campaigns.

## Project Files
- `Market_Basket_Analysis.py` – Python analysis code.
- `Target.csv` – Original dataset.
- `Target_Cleaned.csv` – Cleaned dataset.
- `Market_Basket_Analysis.pdf` – Project report.
- `Market_Basket_Analysis.pptx` – Presentation.

## Project Presentation
[Watch the project walkthrough on Loom](https://www.loom.com/share/3050ba64daa649cd8f5183c65116c995)

## Disclaimer
This project is an educational customer analytics project based on the supplied survey dataset. The findings describe patterns in the available data and should not be interpreted as verified business results from Target.

## Author
Sagar

**Skills:** Python | Pandas | NumPy | Exploratory Data Analysis | Data Visualization | K-Means Clustering | Customer Segmentation
