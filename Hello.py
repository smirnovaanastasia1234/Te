import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer
import numpy as np
import pandas as pd
from transformers import pipeline
from PIL import  Image
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import plotly.express as px
import nltk 
  
def intro():
    import streamlit as st
    # Title of the application 
    st.write("# Добро пожаловать! 👋")
    st.sidebar.success("Выбрать раздел")

    st.markdown(' # Анализ тональности чатов Телеграм\n', )
    st.info("Группа 32: Смирнова А., Кожедуб Н., Багаудинов Э., Петраков В.")

    display = Image.open('images/display.jpg')
    display = np.array(display)
    st.image(display)
   

def mapping_demo():
    import streamlit as st
    from streamlit_extras.dataframe_explorer import dataframe_explorer
    import pandas as pd
    from transformers import pipeline
    import matplotlib.pyplot as plt 
    import seaborn as sns; sns.set()
    import plotly.express as px
    import time

    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    @st.cache 
    @st.experimental_memo
    def read_data(uploaded_file):
        return pd.read_csv(uploaded_file)
    datafile = st.file_uploader("Загрузите файл csv", ["csv"])
   
    if datafile is None:
        st.info("""Загрузите набор данных (.csv), чтобы приступить к работе.""")
        st.stop() 
    #Индикатор выполнения
    progress_bar = st.progress(0)
    progress_text = st.empty()
    for i in range(101):
        time.sleep(0.1)
        progress_bar.progress(i)
        progress_text.text(f"Progress: {i}%")
   
    data = read_data(datafile).copy()
    
    model=pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
                      
    result = st.button('Распознать')
    st.balloons()
    
    selected_id = st.selectbox("Select Sex", df_model['user_id'].unique())
    st.write(f"Выбрать пользователя: {selected_id!r}")   
    
    df_model = data.copy()
    
    if result:
        lst = []
        for i in df_model["text"]:
            lst.append(model(str(i))[0]["label"])
            df_model["Sentinent"]=pd.DataFrame(lst)
        st.write(df_model)
        st.balloons()
               

        st.subheader("Количество видов сообщений")

        chat_df = pd.DataFrame(df_model["Sentinent"].dropna().value_counts()).reset_index()
        chat_df = chat_df.sort_values(by="index")
        chat_df.columns = ["Sentinent", "Count"]
        fig = px.bar(
        chat_df,
        x="Sentinent",
        y="Count",
        title="Количество видов сообщений",
        color_discrete_sequence=["#9EE6CF"],)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        
        st.subheader("Самые позитивные user_id")
        df_P = df_model[df_model["Sentinent"]=="POSITIVE"]
        df_p =df_P.user_id.value_counts().sort_index()
        df_p.plot.bar(edgecolor='k', alpha=0.9, stacked = True, cmap="viridis")
# Create a word cloud function 
def wordcloud():
   # Standard Libraries
   import streamlit as st
   import os 
   import re 
   import string 
   import numpy as np
   from collections import Counter
   # Text Processing Library 
   from nltk.corpus import stopwords
   import pandas as pd
   import pymorphy2
   from nltk.tokenize import word_tokenize 
  
   # Data Visualisation 
   import matplotlib.pyplot as plt 
   from wordcloud import WordCloud 
   from PIL import Image
   
   st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
   st.header("Generate Word Cloud")
   st.subheader("Generate a word cloud from text containing the most popular words in the text.")

   

page_names_to_funcs = {
    "Главная 👋": intro,
    "Загрузка истории чатов 🔭": mapping_demo,
    "create_wordcloud ":wordcloud
   }
name = st.sidebar.selectbox("Выбрать раздел", page_names_to_funcs.keys())
page_names_to_funcs[name]()