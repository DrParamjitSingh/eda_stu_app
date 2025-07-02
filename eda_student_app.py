# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 01:49:44 2025

@author: Dr Paramjit Singh
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("📊 Student Performance EDA Project")
#st.write("##### 📊 Student Performance EDA Project")
#st.write("This app explores a student performance dataset using EDA techniques.")

# Using padding-left or margin-left to push the text over.
# 'em' units are relative to the font size, so it can be more robust than 'px'
# for text alignment, but still requires tuning.
st.markdown(
    """
    <p style="margin-top: -15px;padding-left: 6ch; font-weight: 400; font-size: normal;margin-bottom: 0px;">
        (This app explores a student performance dataset using EDA techniques.)
    </p>
    <p style="padding-left: 8ch; font-weight: 300; font-size: small;color: #666;margin-bottom: 0px;">
        © Copyright Dr Paramjit Singh, 2025. All Rights Reserved.
    </p>
    <p style="padding-left: 8ch; font-weight: 300; font-size: small;color: #666;margin-bottom: 0px;">
        ______________________________________
    </p>
    """,
    unsafe_allow_html=True
)






# Load Data
df = pd.read_csv("student_performance.csv")

st.subheader("🔍 Dataset Preview")
st.write(df.head())

st.subheader("📊 Descriptive Statistics")
st.write(df.describe())

st.subheader("❓ Missing Values")
st.write(df.isnull().sum())

# Plot 1: Histogram
st.subheader("🎯 Math Score Distribution")
sns.histplot(df['math score'], kde=True)
st.pyplot(plt.gcf())
plt.clf()

# Plot 2: Boxplot by Gender
st.subheader("📚 Reading Scores by Gender")
sns.boxplot(x='gender', y='reading score', data=df)
st.pyplot(plt.gcf())
plt.clf()

# Plot 3: Pairplot
st.subheader("📈 Pairplot of Scores")
st.text("This may take a few seconds...")
sns.pairplot(df[['math score', 'reading score', 'writing score']])
st.pyplot(plt.gcf())
plt.clf()

# Plot 4: Heatmap
st.subheader("🔥 Correlation Heatmap")
sns.heatmap(df[['math score', 'reading score', 'writing score']].corr(), annot=True, cmap='coolwarm')
st.pyplot(plt.gcf())
plt.clf()

