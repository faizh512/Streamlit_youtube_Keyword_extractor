import streamlit as st
from bs4 import BeautifulSoup
import requests
st.markdown("<h1 style='text-align:center;'>Youtube Keyword Extractor</h1>", unsafe_allow_html=True)
st.markdown("---")
url=st.text_input("Enter the Url")
s_btn=st.button("Submit")
if s_btn:
    page=requests.get(url)
    if page.status_code!=200:
        print("page is not successfully Read")
    else:
        print("Page is successfully Read ")
        soup=BeautifulSoup(page.content,"lxml")
        meta_tag=soup.select("meta[name='keywords']")
        st.write(meta_tag[0]['content'])
        