import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df_a = pd.read_json('\heart_failure_a.json')
df_b = pd.read_json('\heart_failure_b.json')
df = pd.merge(df_a, df_b, on='person_id', how='inner')

st.title('심박출 슬라이더')

min_ejection = int(df['ejection_fraction'].min())
max_ejection = int(df['ejection_fraction'].max())

ejection_range = st.slider(
    '심박출(ejection_fraction) 범위를 선택하세요:',
    min_value=min_ejection,
    max_value=max_ejection,
    value=(min_ejection, max_ejection) 
)


filtered_df = df[
    (df['ejection_fraction'] >= ejection_range[0]) & 
    (df['ejection_fraction'] <= ejection_range[1])
]


if filtered_df.empty:
    st.warning("선택된 심박출 범위에 해당하는 데이터가 없습니다.")
else:

    fig = plt.figure(figsize=(10, 8))
    sns.histplot(data=filtered_df, x='time', bins=20, hue='DEATH_EVENT', kde=True) 
    plt.title(f' {ejection_range[0]} - {ejection_range[1]})')
    plt.xlabel('time')
    plt.ylabel('Count')

    st.pyplot(fig)
