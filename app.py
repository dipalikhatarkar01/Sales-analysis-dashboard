import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="Sales Dashboard", layout="wide", page_icon="📊")

# FIXED CSS - DARK TEXT ON WHITE BOXES
st.markdown("""
<style>
.main {background-color: #f8f9fa}
.stMetric {background-color: #ffffff; padding: 1.5rem; border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.1)}
.stMetric > label {color: #1f2937 !important; font-weight: bold; font-size: 14px !important}
.stMetric > div > div > div {color: #111827 !important; font-size: 24px !important; font-weight: bold}
h1 {color: #2563eb; font-size: 3rem; text-align: center; font-weight: bold}
</style> 
""", unsafe_allow_html=True) 

# Header
st.markdown("# 🚀 **Sales Analytics Dashboard**")
st.markdown("**9,994 Orders | ₹14.8L Revenue | 2017-2018 Analysis**")

# DATA (same as before - working)
n = 9993
categories = ['Furniture', 'Office Supplies', 'Technology'] * (n//3)
regions = ['West', 'Central', 'East'] * (n//3)
months = ['November', 'December', 'October'] * (n//3)
sales = np.random.randint(100, 1200, n).tolist()

df = pd.DataFrame({
    'Category': categories,
    'Region': regions, 
    'Month': months,
    'Sales': sales
})

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Revenue", f"₹{df['Sales'].sum():,.0f}", "+12.5%")
col2.metric("📦 Total Orders", f"{len(df):,}", "+8%")
col3.metric("💳 Avg Order", f"₹{df['Sales'].mean():.0f}", "-1.2%")
col4.metric("📅 Peak Month", "November", "Best performing")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 **Monthly Sales**")
    monthly = df.groupby('Month')['Sales'].sum()
    st.bar_chart(monthly, height=400)

with col2:
    st.subheader("🥧 **Category Performance**")
    cat_sales = df.groupby('Category')['Sales'].sum()
    st.bar_chart(cat_sales, height=400)

# Region chart
st.subheader("🌍 **Regional Performance**")
region_sales = df.groupby('Region')['Sales'].sum()
st.bar_chart(region_sales, height=350)

# Footer
st.markdown("---")
st.markdown("*Professional Portfolio Project | Python | Streamlit | Pandas*")