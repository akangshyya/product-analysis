# Load Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load Data
orders_df = pd.read_csv("D:\\download_gaargi\\Orders.csv")
details_df = pd.read_csv("D:\\download_gaargi\\Details.csv")

# Merge on 'Order ID'
df = pd.merge(orders_df, details_df, on="Order ID")

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d-%m-%Y")

# Add Month Column
df['Month'] = df['Order Date'].dt.to_period('M').astype(str)

#Plotting Sales Data
plt.figure(figsize=(12, 6)) 
sns.barplot(data=df, x='Category', y='Amount', palette='Set1')
plt.title("Total Sales Amount by Category")

# Monthly Sales
plt.figure(figsize=(14, 6))
monthly_sales = df.groupby('Month')['Amount'].sum().reset_index()
sns.lineplot(data=monthly_sales, x='Month', y='Amount', marker='o')
plt.xticks(rotation=45)
plt.title("Monthly Sales Amount")
plt.xlabel("Month")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.show()

# Profit by Category
plt.figure(figsize=(8, 5))
sns.barplot(data=df.groupby('Category')['Profit'].sum().reset_index(), x='Category', y='Profit', palette='Set2')
plt.title("Total Profit by Category")
plt.tight_layout()
plt.show()

# Quantity Sold by Sub-Category
plt.figure(figsize=(10, 6))
sns.barplot(data=df.groupby('Sub-Category')['Quantity'].sum().reset_index(), x='Sub-Category', y='Quantity', palette='Set2')
plt.title("Total Quantity Sold by Sub-Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()








"""
#ML modeling
# Prepare Data for Machine Learning
# Features and Target
X = df[['Amount', 'Quantity', 'Category', 'Sub-Category', 'PaymentMode', 'State']]
y = df['Profit']

# Categorical and Numerical Columns
categorical_features = ['Category', 'Sub-Category', 'PaymentMode', 'State']

# Preprocessing Pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ],
    remainder='passthrough'
)

# Final Pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
pipeline.fit(X_train, y_train)

# Predict
y_pred = pipeline.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)"""
