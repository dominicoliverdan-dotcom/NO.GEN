import streamlit as st
import random

st.write("NUMBER GENERATOR")
st.write("input range")
S = st.number_input("smallest:" , value=1, step=1)
L = (st.number_input("largest:" , value=10, step=1))
number = random.randint(S, L)

if st.button("generate"):
    if S > L :
        st.error("smallest must be less than largest")
    else :
        number = random.randint (S,L)
        st.success(number)

