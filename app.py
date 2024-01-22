import streamlit as vAR_st
vAR_st.set_page_config(page_title="Policy Analysis", layout="wide")

from DSAI_Utility.DSAI_Utility import All_Initialization,CSS_Property
from DSAI_source_code.DSAI_QALangchain import QAwithLangchain


if __name__=='__main__':
    vAR_hide_footer = """<style>
            footer {visibility: hidden;}
            </style>
            """
    vAR_st.markdown(vAR_hide_footer, unsafe_allow_html=True)
    # Applying CSS properties for web page
    CSS_Property("DSAI_Utility/DSAI_style.css")
    # Initializing Basic Componentes of Web Page
    choice = All_Initialization()
    
    if choice=="Policy Analysis Q&A":

        # function to call QA langchain
        QAwithLangchain() 
        