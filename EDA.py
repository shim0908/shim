import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def  plotting_demo():
    
    #uploaded_file = st.file_uploader("Choose a file")

    #money=pd.read_csv(uploaded_file)
    money = pd.read_csv("money_data7.csv")

    option = st.selectbox(
        '년도',
        ('2020', '2021', '2022'))

    option2 = int(option)

    st.write('You selected:', option)

    money = money[:] [money['A_YEAR']== option2]
    st.money(200,100)
    
    global  aa
    
    aa = money

    fig, ax = plt.subplots(2,2, figsize=(12,8))

    plt.subplot(221)
    plt.plot(  list( money['A_MONTH'] ), list( money['A_RATE'] ), color='lightcoral' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('America rate')


    plt.subplot(222)
    plt.plot(  list( money['A_MONTH'] ), list( money['K_RATE'] ), color='cornflowerblue' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('Korea rate')

    plt.subplot(223)
    plt.plot(  list( money['A_MONTH'] ), list( money['KOSPI'] ), color='palegreen' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('Kospi Rate')

    plt.subplot(224)
    plt.plot(  list( money['A_MONTH'] ), list( money['HOUSE_PRICE'] ), color='gold' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('House Price')

    st.pyplot(fig)
    #st.dataframe(money)
       
def bar_chart():

    url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo&year="

    years = ['2015', '2016','2017', '2018', '2019', '2020', '2021', '2022' ]

    df = pd.DataFrame([]) 

    for    i    in     years: 
        df1 = pd.read_html( url + i  )[0]
        df1['년도'] =  i 
        df = pd.concat([df, df1], axis=0)
        
    baseball = df    

    baseball.팀.replace({'두산':'DS','삼성':'SS','키움':'KU','한화':'HH','롯데':'LT','넥센':'NX', 'kt':'KT'}, inplace=True)
    
    option = st.selectbox(
        '년도',
        ('2015', '2016','2017', '2018', '2019', '2020', '2021', '2022'))

    option2 = option

    st.write('You selected:', option)

    df7  =  baseball[:] [ baseball.년도==option2 ]
    x = df7.팀
    y = df7.승률
    
    global bb
    bb = baseball
    
    fig, ax = plt.subplots(figsize=(12,8))

    colors = ['C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17' ,'C18', 'C19', 'C20' ]
    plt.bar(  x,  y,  color= colors ) 

    for   num ,   v    in   enumerate( y ):
        plt.text (  num -0.4  ,   v + 0.01 ,  v   )

    plt.title( "year korea baseball winrate data", position=(0.5,1.1))
    st.pyplot(fig)
    #st.dataframe(df7)        


st.set_page_config(layout="centered")     
st.title("SHIM's Analystic🧐")
from PIL import Image
image = Image.open('img3.jpg')
st.image(image)


with st.form(key ='Form1'):
    with st.sidebar:
        
        select_language =  st.sidebar.radio('Chart & Data', ('💲📈📉🏠', '⚾🏆', '🤷‍♂️'))
        

        
if select_language =='💲📈📉🏠':  
    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
   
    with tab1:
        tab1.subheader("Chart")
        plotting_demo()
        
    with tab2:
        tab2.subheader("Data")
        st.dataframe(aa)
  

        
if select_language =='⚾🏆':
    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
   
    with tab1:
        tab1.subheader("Chart")
        bar_chart()
        
    with tab2:
        tab2.subheader("Data")
        st.dataframe(bb)
