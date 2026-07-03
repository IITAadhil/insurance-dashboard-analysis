import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Insurance Website Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Insurance Website Analytics Dashboard")

st.markdown("""
Analyse website user behaviour, marketing performance, and insurance sales using interactive visualisations.
""")

df = pd.read_csv("insurance.data.aggregated.csv")

st.subheader("Dataset Preview")

st.subheader("Filtered Dataset")

st.sidebar.header("Dashboard Filters")

marketing_channel = st.sidebar.multiselect(
    "Select Marketing Channel",
    options=df["Marketing Channel"].unique(),
    default=df["Marketing Channel"].unique()
)

device_category = st.sidebar.multiselect(
    "Select Device Category",
    options=df["Device Category"].unique(),
    default=df["Device Category"].unique()
)

filtered_df = df[
    (df["Marketing Channel"].isin(marketing_channel)) &
    (df["Device Category"].isin(device_category))
]

st.dataframe(filtered_df)

