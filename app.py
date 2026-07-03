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

# KPI Section
st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

total_users = filtered_df["Users"].sum()
total_revenue = filtered_df["Revenue"].sum()
total_quotes = filtered_df["TotalNumberOfInsuranceQuotes"].sum()
total_policies = filtered_df["TotalNumberOfInsurancePoliciesPurchaed"].sum()

with col1:
    st.metric("👥 Total Users", f"{total_users:,}")

with col2:
    st.metric("💰 Total Revenue", f"${total_revenue:,.2f}")

with col3:
    st.metric("📝 Insurance Quotes", f"{total_quotes:,}")

with col4:
    st.metric("📄 Policies Purchased", f"{total_policies:,}")

st.markdown("---") 

st.subheader("📊 Users by Marketing Channel")
users_channel = filtered_df.groupby("Marketing Channel")["Users"].sum().reset_index()
fig_users = px.bar(
    users_channel,
    x="Marketing Channel",
    y="Users",
    color="Marketing Channel",
    text="Users",
    title="Total Users by Marketing Channel"
)
fig_users.update_layout(
    xaxis_title="Marketing Channel",
    yaxis_title="Number of Users",
    showlegend=False
)
st.plotly_chart(fig_users, use_container_width=True)

st.subheader("💰 Revenue by Marketing Channel")
revenue_channel = filtered_df.groupby("Marketing Channel")["Revenue"].sum().reset_index()
fig_revenue = px.bar(
    revenue_channel,
    x="Marketing Channel",
    y="Revenue",
    color="Marketing Channel",
    text="Revenue",
    title="Revenue by Marketing Channel"
)

fig_revenue.update_layout(
    xaxis_title="Marketing Channel",
    yaxis_title="Revenue",
    showlegend=False
)

st.plotly_chart(fig_revenue, use_container_width=True)

st.subheader("📱 Users by Device Category")
device_users = filtered_df.groupby("Device Category")["Users"].sum().reset_index()
fig_device = px.pie(
    device_users,
    names="Device Category",
    values="Users",
    title="Users by Device Category",
    hole=0.4
)

st.plotly_chart(fig_device, use_container_width=True)