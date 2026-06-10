import streamlit as st
import pandas as pd
import os
# Page Title
st.title("Tour Enquiry Dashboard")

# Read CSV


file_path = os.path.join(os.path.dirname(__file__), "tour_enquiry.csv")
df = pd.read_csv(file_path)

# Show Dataset
st.subheader("Dataset")
st.write(df)

# Destination Wise Enquiries
st.subheader("Destination Wise Enquiries")
destination = df.groupby("Destination")["Enquiries"].sum()
st.bar_chart(destination)

# Month Wise Enquiries
st.subheader("Month Wise Enquiries")
month = df.groupby("Month")["Enquiries"].sum()
st.line_chart(month)

st.success("Task 3 Completed Successfully")