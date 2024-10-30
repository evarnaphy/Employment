import pandas as pd
import streamlit as st
import plotly.express as px 
import plotly.graph_objects as go

@st.cache_data
def load_data(url):
    df=pd.read_csv(url)
    return df

df=pd.read_csv("C:/Users/User/Desktop/employment/dataset.csv")
df=df.dropna()
df.head()
year_min = df['year'].min()
year_max = df['year'].max()

selected_year = st.slider('Year:', year_min, year_max, (year_min, year_max))

filtered_df = df[(df['year'] >= selected_year[0]) & (df['year'] <= selected_year[1])]

st.title("Kenya Employment Data Visualization")
    
fig= px.pie(df, values='total_employed_population', names='sex',
                  title="Gender distribution by employment",)
st.plotly_chart(fig, use_container_width=True)

st.write("Population over time")
st.line_chart(
         df, 
         x='year', 
         y='population',

)

st.bar_chart(
    df,
    x="year",
    y="ILO_unemployed_rate",
)

st.write("Unemployment rates")
    
st.bar_chart(
    df,
    x="Agriculture",
    y="ILO_unemployed_rate",
)
    
fig= px.pie(df, values='total_employed_population', names='Agriculture',
                  title="Employment distribution across Agriculture",)
st.plotly_chart(fig, use_container_width=True)
    

st.write("Comparison of inactive population types")
fig4 = go.Figure(data=[go.Bar(x=['Less than basic_unemployment', 'Basic_unemployment', 'Intermediate_unemployment', 'Advanced_unemployment'], y=df['Less than basic_unemployment']+df['Basic_unemployment']+df['Intermediate_unemployment']+df['Advanced_unemployment'])])
fig4.update_layout(title='Comparison of Inactive Population Types', xaxis_title='Inactive Population Type', yaxis_title='Number of People')
st.plotly_chart(fig4)


