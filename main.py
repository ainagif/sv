import streamlit as st

st.set_page_config(
    page_title="Genetic Algorithm"
)

st.header("Genetic Algorithm", divider="gray")

import streamlit as st
import pandas as pd
import plotly.express as px

# Set the URL for the CSV file
csv_url = 'https://raw.githubusercontent.com/ainagif/aina44/refs/heads/main/arts_faculty_data.csv'

# --- Data Loading ---
st.header("Arts Faculty Data Analysis")

try:
    # Load the data into a Pandas DataFrame
    arts_df = pd.read_csv(csv_url)
    st.success("Data loaded successfully!")


    # Display the head of the DataFrame in Streamlit
    st.subheader("Data Preview (First 5 Rows)")
    st.dataframe(arts_df.head())

    # --- Plotly Pie Chart Generation ---
    st.subheader("Distribution of Gender in Arts Faculty (Plotly)")

    # Calculate the value counts for the 'Gender' column
    gender_counts = arts_df['Gender'].value_counts().reset_index()
    # Rename columns for clarity in Plotly
    gender_counts.columns = ['Gender', 'Count']

    # Create the Plotly Pie Chart
    # plotly.express is often the simplest way to create common charts
    fig = px.pie(
        gender_counts,
        values='Count',
        names='Gender',
        title='Distribution of Gender in Arts Faculty',
        hole=0.3, # Optional: makes it a donut chart
        color_discrete_sequence=px.colors.qualitative.Set1 # Optional: sets a color scheme
    )

    # Optional: Update layout for better appearance
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"An error occurred while loading or processing data: {e}")
