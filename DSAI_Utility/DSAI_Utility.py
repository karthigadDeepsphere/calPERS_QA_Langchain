
import streamlit as st
from PIL import Image


def CSS_Property(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def All_Initialization():
    col1,col2 = st.columns([5,5])
    with col1:
        image = Image.open('DSAI_Utility/Logo_final.png')
        st.image(image)
    with col2:
        image = Image.open('DSAI_Utility/calPers_logo.png')
        st.image(image)
    # st.markdown("<h1 style='text-align: center; color: #454545; font-size:25px;'>Generative AI empowers policy analysis for Employment Development</h1><h2 style='text-align: center; color: blue; font-size:20px;position: relative; top:-22px;'>With LLM, policy Q&A responses are easier to generate with citations</h2>", unsafe_allow_html=True)
    # st.markdown("""
    # <hr style="width:100%;height:3px;background-color:gray;border-width:10;position:relative;bottom:16px;">
    # """, unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #454545; font-size:25px;'>Generative AI empowers policy analysis for Retirement System</h2><h2 style='text-align: center; color: blue; font-size:20px;position: relative; top:-30px;'>With LLM, policy Q&A responses are easier to generate</h2>", unsafe_allow_html=True)
    # st.markdown("<h1 style='text-align: center; color: #454545; font-size:20px; top: '>Generative AI empowers policy analysis for Employment Developmen</h1>", unsafe_allow_html=True)
    st.markdown("""
    <hr style="width:100%;height:3px;background-color:gray;border-width:10;position:relative; bottom:30px;">
    """, unsafe_allow_html=True)
    st.sidebar.markdown("<h2 style='text-align: center; color: white; font-size:20px;'>Solution Scope</h2>", unsafe_allow_html=True)
    
    choice2 =  st.sidebar.selectbox(" ",('Home','About Us'))
    choice1 =  st.sidebar.selectbox(" ",('Select Application','Policy Analysis Q&A')) #,'Policy Analysis - Dialogflow','Policy Analysis - Evaluation'
    choice3 =  st.sidebar.selectbox(" ",('Libraries in Scope','OpenAI','Streamlit'))
    choice4 =  st.sidebar.selectbox(" ",('Models Used','ChatGPT', 'GPT3','GPT3 - Davinci','Llama','Titan'))
    menu = ["Google Cloud Services in Scope","Cloud Storage", "Cloud Run", "Cloud Function", "Secret Manager","AWS-OpenSearch(Serverless VectorStore)"]
    choice = st.sidebar.selectbox(" ",menu)
    st.sidebar.write('')
    st.sidebar.write('')
    href = """<form action="#">
    <input style='width: 100%;
        border-radius: 5px;
        padding: 7px;
        background-color: #32CD32;
        border: none;' type="submit" value="Clear/Reset" />
</form>"""
    st.sidebar.markdown(href, unsafe_allow_html=True)
    st.sidebar.write('')
    st.sidebar.write('')
    st.sidebar.markdown("<p style='text-align: center; color: White; font-size:20px;'>Build & Deployed on<span style='font-weight: bold'></span></p>", unsafe_allow_html=True)
    st.sidebar.write('')
    
    with st.sidebar:
        col1,col2 = st.columns([5,5])
        with col1:
            st.image('DSAI_Utility/Google-Cloud-Platform-GCP-logo.png')
        with col2:
            st.image('DSAI_Utility/aws_logo.png')
    
    # vAR_clear_button = st.sidebar.button('Clear/Reset')
    # if vAR_clear_button:
    #     st.experimental_rerun()
    
    return choice1
