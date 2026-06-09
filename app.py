import streamlit as st
import pandas as pd

st.title("Unveiling the Android App Market")

df = pd.read_csv("data/apps.csv/datasets/apps.csv")
st.sidebar.title("Filters")
category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(df["Category"].dropna().unique())
    )
app_type = st.sidebar.selectbox(
    "Select App Type",
    ["All", "Free", "Paid"]
)
filtered_df = df

if category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == category]

if app_type != "All":
    filtered_df = filtered_df[filtered_df["Type"] == app_type]


st.subheader("Dataset Preview")
st.dataframe(filtered_df.head())

st.subheader("Dataset Shape")
st.write(filtered_df.shape)


import streamlit as st
import pandas as pd

st.title("📱 Unveiling the Android App Market")

df = pd.read_csv("data/apps.csv/datasets/apps.csv")

# KPI Calculations
total_apps = len(df)
avg_rating = round(df["Rating"].mean(), 2)
total_categories = df["Category"].nunique()

# KPI Display
col1, col2, col3 = st.columns(3)

col1.metric("Total Apps", total_apps)
col2.metric("Average Rating", avg_rating)
col3.metric("Categories", total_categories)

st.subheader("Dataset Preview")
st.dataframe(df.head())
st.subheader("Top 10 App Categories")

top_categories = df["Category"].value_counts().head(10)

st.bar_chart(top_categories)
st.subheader("⭐ Top Rated Categories")

top_rated = (
    df.groupby("Category")["Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_rated)