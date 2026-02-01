import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Segmentation (RFM)", layout="wide")

st.title("Customer Segmentation using RFM Analysis")
st.write("This Streamlit app displays clustered customer data using RFM analysis.")

df = pd.read_csv("streamlit_app/rfm_clustered_data.csv")

st.subheader("Clustered Customer Dataset")
st.dataframe(df)

st.subheader("Number of Customers per Cluster")
cluster_counts = df["Cluster"].value_counts()
st.bar_chart(cluster_counts)

st.subheader("Monetary Value vs Purchase Frequency")

st.scatter_chart(df, x="Frequency", y="Monetary")
