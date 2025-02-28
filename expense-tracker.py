import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App Title
st.title("💰 Expense Tracker")
st.subheader("Track your daily expenses easily!")

# Expense Data List
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# User Input Fields
date = st.date_input("Date")
category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])
amount = st.number_input("Amount", min_value=0.0, format="%.2f")
note = st.text_input("Note (optional)")

# Add Expense Button
if st.button("Add Expense"):
    new_expense = {"Date": date, "Category": category, "Amount": amount, "Note": note}
    st.session_state.expenses.append(new_expense)
    st.success("Expense added successfully!")

# Convert to DataFrame for Display
df = pd.DataFrame(st.session_state.expenses)

if not df.empty:
    st.write("### Expense List")
    st.dataframe(df)

    # Expense Summary by Category
    st.write("### Expense Summary")
    summary = df.groupby("Category")["Amount"].sum()
    st.bar_chart(summary)
