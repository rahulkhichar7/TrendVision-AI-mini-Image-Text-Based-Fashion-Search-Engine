import streamlit as st
import pandas as pd
import os

st.title("Rahul's AI Powered Search Engine \n ## Trend Vision AI: AI powered Image & Text-Based Fashion Search Engine")

# slide bar
search_type = st.sidebar.radio("Search by: ",["Text", "Image", "Hybrid","See ALL Available Products"])
labels = pd.read_csv("extracted/myntradataset/styles.csv")

if search_type=="Text":
    st.write("showing result for Text Search")
    input_text = st.text_input("search here...")
    
elif search_type == "Image":
    st.write("Showing results for Image Search")
    input_image = st.file_uploader("Upload Image here...")
    
elif search_type == "See ALL Available Products":
    n =1
    for i in os.listdir("extracted/myntradataset/images"):
        
        st.image("extracted/myntradataset/images/"+i,caption=labels.loc[labels.id==int(i.split(".")[0])].values[0][9],width=100)
        n+=1
        if n>10:
            break
    
else:
    st.write("website under progess. This feature will be available soon.")
    