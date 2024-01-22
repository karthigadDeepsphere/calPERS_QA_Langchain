import streamlit as vAR_st
vAR_st.set_page_config(page_title="Policy Analysis", layout="wide")

from DSAI_Utility.DSAI_Utility import All_Initialization,CSS_Property
# from DSAI_Assistant_API import RAGWithAssistant
import traceback
# from DSAI_source_code.DSAI_Langchain import RAGWithLangchain 
from DSAI_source_code.DSAI_QALangchain import QAwithLangchain
# from DSAI_source_code.DSAI_Langchain_Eval import RAGWithLangchainEval
# from DSAI_source_code.DSAI_GCP_GenApp import dialogflow
# from DSAI_Assistant_API import RAGWithAssistant
# from DSAI_LlamaIndex import RAGWithLlama



if __name__=='__main__':
    vAR_hide_footer = """<style>
            footer {visibility: hidden;}
            </style>
            """
    vAR_st.markdown(vAR_hide_footer, unsafe_allow_html=True)
    # try:
    # Applying CSS properties for web page
    CSS_Property("DSAI_Utility/DSAI_style.css")
    # Initializing Basic Componentes of Web Page
    choice = All_Initialization()
    
    if choice=="Policy Analysis Q&A":
    
        # RAGWithLangchain()
        QAwithLangchain()
        # RAGWithLlama()
        # RAGWithAssistant()
        
    # if choice=="Policy Analysis - Dialogflow":
    #     dialogflow()
        
    # if choice=="Policy Analysis - Evaluation":
    #     RAGWithLangchainEval()


    # except BaseException as exception:
    #     print('Error in main function - ', exception)
    #     exception = 'Something went wrong - '+str(exception)
    #     traceback.print_exc()
    #     vAR_st.error(exception)