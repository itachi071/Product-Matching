import pandas as pd
import streamlit as st
import pickle

price_dict = pickle.load(open('prices.pkl', 'rb'))
price=pd.DataFrame(price_dict)
def form(product_name):
    arp=price[price['product_name']==product_name].to_numpy()[0][1]
    adp=price[price['product_name']==product_name].to_numpy()[0][2]
    frp=price[price['product_name']==product_name].to_numpy()[0][4]
    fdp=price[price['product_name']==product_name].to_numpy()[0][5]
    return arp,adp,frp,fdp

st.title('Product Price on Amazon and Filpkart')
product=st.text_input('Product Name')
if st.button('Submit'):
    name=['Amazon_retail_Price','Amazon_discounted_Price','Flipkart_retail_Price','Flipkart_discounted_Price']
    p=form(product)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.text(name[0])
        st.text(p[0])
    with col1:
        st.text(name[1])
        st.text(p[1])
    with col1:
        st.text(name[2])
        st.text(p[2])
    with col1:
        st.text(name[3])
        st.text(p[3])






