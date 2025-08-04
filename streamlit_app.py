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


name = st.text_input("이름을 입력하세요")
age = st.slider("나이", 0, 100, 25)
agree = st.checkbox("동의하십니까?")

if st.button("클릭하세요"):
    st.success(f"{name}님, 반갑습니다!")


uploaded = st.file_uploader("CSV 파일을 업로드하세요", type="csv")
if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.write(df)
