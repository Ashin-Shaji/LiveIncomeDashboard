import streamlit as st
import pandas as p
import numpy as n
import time
import plotly.express as px
st.set_page_config(page_title='Live Income Dashboard',
page_icon='💸',layout='wide')
st.title('Live Income Data Monitoring App')
df=p.read_csv('income.csv')
#filters
jobfilter=st.selectbox('Choose a job',df['occupation'].unique(),index=1)
st.write(jobfilter)
placeholder=st.empty()
df=df[df['occupation']==jobfilter]
# st.write(df)
while True:
    df['new_age']=df['age']*n.random.choice(range(1,5))
    df['whpw_new']=df['hours-per-week']*n.random.choice(range(1,5))#whpw-working hours per week
    #creating kpis
    avg_age=n.mean(df['new_age'])#average
    #we need the total count of 'Married-civ-spouse',and to know the change add random.choice(range(1,30))
    count_marri=int(df[df['marital-status']=='Married-civ-spouse']
    ['marital-status'].count()+n.random.choice(range(1,30)))
    hpw=n.mean(df['whpw_new'])
    with placeholder.container():
        #create 3 columns
        kpi1,kpi2,kpi3=st.columns(3)
        #filling columns with required values,delta-to view the type of change(up or down)
        kpi1.metric(label='Age',value=round(avg_age),delta=round(avg_age)-10)
        kpi2.metric(label='Married Count',value=int(round(count_marri)),delta=10+count_marri)#count_marri is float,so int()
        kpi3.metric(label='Working hours/week',value=round(hpw),delta=round(count_marri/hpw)/8)
        #create two columns for chart
        fig1,fig2=st.columns(2)
        with fig1:
            st.markdown('### Age vs Marital Status')
            fig1=px.density_heatmap(data_frame=df,y='new_age',x='marital-status').update_layout(xaxis_title='Married',yaxis_title=('Age'))
            st.write(fig1)
        with fig2:
            st.markdown('### Age count')
            fig2=px.histogram(data_frame=df,x='new_age').update_layout(xaxis_title='Age')
            st.write(fig2)
        st.markdown('### Data view')
        st.dataframe(df)
        time.sleep(1)














