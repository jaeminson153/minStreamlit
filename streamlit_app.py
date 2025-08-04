import streamlit as st
import pandas as pd
import numpy as np
from transformers import pipeline

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




# 감정 분석 파이프라인 불러오기
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

# Streamlit UI 구성
st.title("🤗 Hugging Face 감정 분석기")
st.write("텍스트를 입력하면 감정(긍정/부정)을 분석합니다.")

# 사용자 입력 받기
user_input = st.text_area("✍️ 분석할 문장을 입력하세요:", "I love Streamlit and Hugging Face!")

# 버튼 클릭 시 감정 분석 수행
if st.button("감정 분석 실행"):
    with st.spinner("분석 중..."):
        result = model(user_input)
        label = result[0]['label']
        score = result[0]['score']

        st.subheader("🔍 분석 결과")
        st.write(f"**감정 분류:** {label}")
        st.write(f"**확신도 (score):** {score:.2f}")


