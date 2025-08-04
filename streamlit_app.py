import streamlit as st
import pandas as pd
import numpy as np

st.title("제목입니다")
st.header("헤더입니다")
st.subheader("서브헤더입니다")
st.write("일반 텍스트입니다")
st.markdown("**굵은 글씨**와 *기울임*")


df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
st.dataframe(df)  # 인터랙티브한 표

st.line_chart(df)  # 선 그래프
st.bar_chart(df)   # 막대 그래프


