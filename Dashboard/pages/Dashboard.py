import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

#Load the Titanic Dataset
df = sns.load_dataset('titanic')

#Set the title of the page
st.title('Titanic Data Analysis')

st.sidebar.header("Filter Options")

#gender filter
gender = st.sidebar.multiselect('Gender',
                                options=df['sex'].unique(),
                                default=df['sex'].unique())

#class filter
pclass = st.sidebar.multiselect('Class',
                                options=sorted(df['pclass'].unique()),
                                default=sorted(df['pclass'].unique()))   

#Age Filter
min_age, max_age = st.sidebar.slider('Age',
                                     min_value = int(df['age'].min()),
                                     max_value = int(df['age'].max()),
                                     value = (int(df['age'].min()), int(df['age'].max())))

#Filter the dataset based on the user selection
filtered_data = df[
    (df['sex'].isin(gender)) &
    (df['pclass'].isin(pclass)) &
    (df['age'] >= min_age) &
    (df['age'] <= max_age)
]

st.dataframe(filtered_data)

#Create a pie chart for gender distribution
st.subheader('Gender Distribution')
gender_count = filtered_data['sex'].value_counts()
fig = px.pie(names=gender_count.index, values=gender_count.values,
             title='Gender Distribution')
st.plotly_chart(fig)

#Create a histogram for age distribution
st.subheader('Age Distribution')
fig = px.histogram(filtered_data, x='age', nbins=20, title='Age Distribution',
                   labels={'age':'Age', 'count':'Count'})
st.plotly_chart(fig)

#Violin plot of age distribution by survival status
#Scatter plot of age vs fare
#Box plot of age distribution by passenger class
#bar chart of survival counts
