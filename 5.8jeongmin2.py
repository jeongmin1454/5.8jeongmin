import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df_a = pd.read_json('\heart_failure_a.json')
df_b = pd.read_json('\heart_failure_b.json')
df = pd.merge(df_a, df_b, on='person_id', how='inner')



st.title('흡연 여부 그래프')

smoking_option = st.radio(
    "흡연?",
    ('흡연 (1)', '비흡연 (0)')
)

if smoking_option == '흡연 (1)':
    filtered_df = df[df['smoking'] == 1]
else:
    filtered_df = df[df['smoking'] == 0]

if filtered_df.empty:
    st.warning("선택된 조건에 해당하는 데이터가 없습니다.")
else:
    fig, ax = plt.subplots(figsize=(10, 6)) # plt.figure 대신 권장되는 방식
    

    sns.violinplot(data=filtered_df, x='DEATH_EVENT', y='platelets', ax=ax)
    
    ax.set_title(f'사망 여부와 혈소판 수치 ({smoking_option})')
    ax.set_xlabel('사망 여부 (DEATH_EVENT)')
    ax.set_ylabel('혈소판 수치 (platelets)')


    st.pyplot(fig)
