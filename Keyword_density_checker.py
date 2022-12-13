import streamlit as st
import re

#------------------------------------------------------title
st.markdown("<h1 style='text-align: center;'>Keyword Density Checkwer</h1>", unsafe_allow_html=True)
st.markdown("--------",unsafe_allow_html=True)
#----------------------------------------------------
text = st.text_area("PASTE HERE YOUR PARAGRAPH")
but = st.button("Check")
col_1, col_2, col_3 = st.columns(3)
word_dict = dict()
if but:
    #------------------------------------
    col_1.markdown(f"<h3> Keywords</h3>", unsafe_allow_html=True)
    col_2.markdown(f"<h3> Density</h3>", unsafe_allow_html=True)
    col_3.markdown(f"<h3> Percentage</h3>", unsafe_allow_html=True)
    sim_text = re.sub("[.?!&;:*@,]", "", text)
    words = sim_text.lower().split(" ")
    t_len = len(words)
    for word in words:
        if word in word_dict:
            word_dict[word]=word_dict[word]+1
        else:
            word_dict[word]=1
    print(word_dict)
    keys = list(word_dict.keys())
    values = list(word_dict.values())
    for i in range(len(keys)):
        col_1.markdown(f"<h5>{keys[i]}</h5>", unsafe_allow_html=True)
        col_2.markdown(f"<h5>{values[i]}</h5>", unsafe_allow_html=True)
        col_3.markdown(f"<h5>{round(values[i]/(t_len)*100)}</h5>", unsafe_allow_html=True)


        












