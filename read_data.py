import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/apps.csv/datasets/apps.csv")

print("Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)
print("\nTotal Missing Values:")
print(df.isnull().sum().sort_values(ascending=False))
print("\nDataset Information")
print("\nMissing Values Count:")
print(df.isnull().sum())
print("Before Cleaning:", df.shape)

df = df.dropna(subset=["Rating"])

print("After Cleaning:", df.shape)
print("\nTop 10 Categories:")

print(df["Category"].value_counts().head(10))
top_categories = df["Category"].value_counts().head(10)

plt.figure(figsize=(12,6))
top_categories.plot(kind="bar")

plt.title("Top 10 App Categories")
plt.xlabel("Category")
plt.ylabel("Number of Apps")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
print("\nTop Rated Categories")

top_rated = df.groupby("Category")["Rating"].mean().sort_values(ascending=False)

print(top_rated.head(10))
plt.figure(figsize=(12,6))

top_rated.head(10).plot(kind="bar")

plt.title("Top Rated Categories")
plt.xlabel("Category")
plt.ylabel("Average Rating")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
print("\nSample Installs Values")

print(df["Installs"].head(10))
df["Installs"] = df["Installs"].str.replace(",", "")
df["Installs"] = df["Installs"].str.replace("+", "", regex=False)

df["Installs"] = pd.to_numeric(df["Installs"])

print("\nInstalls Column Converted")
print(df["Installs"].head())
print("\nTop 10 Most Installed Apps")

top_installs = df.sort_values(
    by="Installs",
    ascending=False
)[["App", "Installs"]]

print(top_installs.head(10))
print("\nAverage Installs by Category")

category_installs = df.groupby("Category")["Installs"].mean()

category_installs = category_installs.sort_values(ascending=False)

print(category_installs.head(10))
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

category_installs.head(10).plot(kind="bar")

plt.title("Average Installs by Category")
plt.xlabel("Category")
plt.ylabel("Average Installs")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
print("\nFree vs Paid Apps")

type_count = df["Type"].value_counts()

print(type_count)
import matplotlib.pyplot as plt

plt.figure(figsize=(6,6))

type_count.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Free vs Paid Apps")
plt.ylabel("")

plt.show()
print("\nContent Rating Distribution")

content = df["Content Rating"].value_counts()

print(content)
plt.figure(figsize=(10,6))

content.plot(kind="bar")

plt.title("Content Rating Distribution")
plt.xlabel("Content Rating")
plt.ylabel("Number of Apps")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
plt.figure(figsize=(10,6))

plt.scatter(df["Reviews"], df["Rating"])

plt.title("Reviews vs Ratings")
plt.xlabel("Reviews")
plt.ylabel("Rating")

plt.show()
print("\nTop Categories by Average Reviews")

category_reviews = df.groupby("Category")["Reviews"].mean()

category_reviews = category_reviews.sort_values(ascending=False)

print(category_reviews.head(10))
plt.figure(figsize=(12,6))

category_reviews.head(10).plot(kind="bar")

plt.title("Top Categories by Average Reviews")
plt.xlabel("Category")
plt.ylabel("Average Reviews")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
print("\nTop Categories by Average Rating")

avg_rating = df.groupby("Category")["Rating"].mean()

avg_rating = avg_rating.sort_values(ascending=False)

print(avg_rating.head(10))
plt.figure(figsize=(12,6))

avg_rating.head(10).plot(kind="bar")

plt.title("Top 10 Categories by Average Rating")
plt.xlabel("Category")
plt.ylabel("Average Rating")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
print("\nCorrelation between Rating and Reviews")

print(df[["Rating","Reviews"]].corr())
print("\nRating Distribution")

plt.figure(figsize=(8,5))

df["Rating"].hist(bins=20)

plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Apps")

plt.show()
top_reviewed = df.sort_values("Reviews", ascending=False)

print(top_reviewed[["App","Reviews"]].head(10))
paid_apps = df[df["Type"]=="Paid"]

print(paid_apps["Price"].describe())