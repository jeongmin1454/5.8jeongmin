import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df_a = pd.read_json(r'C:\Users\KDT19\Desktop\KDT-14\과제\5.8박정민\heart_failure_a.json')
df_b = pd.read_json(r'C:\Users\KDT19\Desktop\KDT-14\과제\5.8박정민\heart_failure_b.json')
df = pd.merge(df_a, df_b, on='person_id', how='inner')

st.title('박출계수 / 나이')



g = sns.jointplot(data=df, x='ejection_fraction', y='age', hue='DEATH_EVENT')

st.pyplot(g.fig)