import streamlit as st
import random
st.title("나의 첫번째 앱")

st.text('\n\n')

st.write('안녕하세요, 저는 --- 입니다')
st.write('저의 이메일 주소는 undefined@null.com')

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write(random.randint(1, 1000))
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
