import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Read the California housing dataset
df = pd.read_csv("housing.csv")

# Save all available location types before filtering
location_types = df["ocean_proximity"].unique().tolist()

# App title
st.title("California Housing Data (1990) by Selina He")

# Filter by median house value
minimum_house_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000
)

df = df[df["median_house_value"] >= minimum_house_value]

# Sidebar filters
st.subheader("See more filters in the sidebar:")

selected_location_types = st.sidebar.multiselect(
    "Choose the location type",
    options=location_types,
    default=location_types
)

df = df[df["ocean_proximity"].isin(selected_location_types)]

income_level = st.sidebar.radio(
    "Choose income level",
    options=["Low", "Medium", "High"]
)

# Filter by income level
if income_level == "Low":
    df = df[df["median_income"] <= 2.5]
elif income_level == "Medium":
    df = df[
        (df["median_income"] > 2.5)
        & (df["median_income"] < 4.5)
    ]
else:
    df = df[df["median_income"] >= 4.5]

# Display the filtered districts on a map
st.map(df[["latitude", "longitude"]])

# Display a histogram with 30 bins
st.subheader("Distribution of Median House Value")

fig, ax = plt.subplots()
ax.hist(
    df["median_house_value"],
    bins=30,
    edgecolor="black"
)
ax.set_xlabel("Median House Value (US Dollars)")
ax.set_ylabel("Number of Districts")

st.pyplot(fig)