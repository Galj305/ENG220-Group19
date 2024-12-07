# -*- coding: utf-8 -*-
"""Project_App_Code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f5egxzOWinxMyV54XTifj49uvrargK4r
"""


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App Title
st.title("Interactive CSV Visualization Tool")

# File uploader for CSV
file = st.file_uploader("EPI.csv", type=["csv"])

if file is not None:
    # Load the CSV file into a DataFrame
    dataframe = pd.read_csv(file)

    # Select a subset of rows and columns
    dataframe = dataframe.iloc[1:7, 1:7]  # Keep rows 1-6 and columns 2-7

    # Display the DataFrame
    st.write("### Data Overview")
    st.write(dataframe)

    # Allow user to select X and Y columns
    col_names = dataframe.columns.tolist()
    x_axis = st.selectbox("Choose X-axis column", col_names)
    y_axis = st.selectbox("Choose Y-axis column", col_names)

    # Allow user to choose graph type
    chart_type = st.selectbox(
        "Choose a chart type",
        ["Line Plot", "Scatter Plot", "Bar Chart", "Pie Chart"]
    )

    # Button to trigger plotting
    if st.button("Generate Chart"):
        plt.figure(figsize=(8, 5))
        fig, ax = plt.subplots()

        if chart_type == "Line Plot":
            ax.plot(dataframe[x_axis], dataframe[y_axis], marker='o', linestyle='-')
            ax.set_title(f"Line Plot: {y_axis} vs {x_axis}")

        elif chart_type == "Scatter Plot":
            ax.scatter(dataframe[x_axis], dataframe[y_axis], color='green')
            ax.set_title(f"Scatter Plot: {y_axis} vs {x_axis}")

        elif chart_type == "Bar Chart":
            ax.bar(dataframe[x_axis], dataframe[y_axis], color='blue')
            ax.set_title(f"Bar Chart: {y_axis} vs {x_axis}")

        elif chart_type == "Pie Chart":
            # Pie charts need fewer unique entries for clarity
            if dataframe[x_axis].nunique() <= 10:
                plt.pie(
                    dataframe[y_axis],
                    labels=dataframe[x_axis],
                    autopct='%1.1f%%',
                    startangle=90
                )
                plt.title(f"Pie Chart: {y_axis}")
            else:
                st.error("Too many categories in X-axis for a pie chart. Reduce to fewer unique values.")

        if chart_type != "Pie Chart":
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            st.pyplot(fig)
        else:
            st.pyplot(plt)

    st.write("Note: Ensure the selected columns are suitable for your chosen chart type.")
else:
    st.info("Upload a CSV file to begin.")
