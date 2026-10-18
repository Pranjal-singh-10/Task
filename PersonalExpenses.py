import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Expenses Dashboard")

upload_file = st.file_uploader("Upload your file", type=["csv", "xlsx"])

if upload_file is not None:

    if upload_file.name.endswith(".csv"):
        df = pd.read_csv(upload_file)
    else:
        df = pd.read_excel(upload_file)

    st.subheader("📊 Raw Data")
    st.write(df.head())

    # Category Filter
    category = st.selectbox(
        "Filter by Category",
        options=df["Category"].dropna().unique()
    )

    filtered_df = df[df["Category"] == category]

    st.subheader("🔎 Filtered Expenses")
    st.write(filtered_df)

    # Pie Chart - All Categories
    st.subheader("💸 Expense Breakdown")

    fig = px.pie(
        df,
        names="Category",
        values="Amount",
        title="Expenses by Category",
        color="Category",
        hole=0.3
    )

    st.plotly_chart(fig, use_container_width=True)

    # Monthly Trend - All Categories
    st.subheader("📈 Monthly Trend")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    monthly = (
        df.dropna(subset=["Date"])
        .groupby(["Month", "Category"], as_index=False)["Amount"]
        .sum()
    )

    fig2 = px.line(
        monthly,
        x="Month",
        y="Amount",
        color="Category",
        markers=True,
        title="Monthly Spending Trend by Category"
    )

    st.plotly_chart(fig2, use_container_width=True)

else:
    st.info("Please upload a CSV or Excel file to view your expenses dashboard.")

