from langchain.document_loaders import PyPDFLoader
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from streamlit_chat import message
from langchain.prompts import ChatPromptTemplate,HumanMessagePromptTemplate,SystemMessagePromptTemplate

import os



import streamlit as st
import time

# os.environ["OPENAI_API_KEY"] = "" # Update with your API key
os.environ["OPENAI_API_KEY"]

messages = []

def input_fields():
        
    st.session_state.source_docs = st.file_uploader(label="LLM Knowledgebase Upload", type="pdf", accept_multiple_files=True)
    
    if st.session_state.source_docs:
        st.success("Knowledge base file(s) successfully uploaded!")

def process_documents():
    if st.session_state.source_docs:
        file_list = []
        documents=[]
        loader_pdf_list=[]
        
        for source_doc in st.session_state.source_docs:
            file_list.append("input_"+source_doc.name)
            with open("input_"+source_doc.name, mode='wb') as w:
                w.write(source_doc.getvalue())
    
        for source_doc in file_list:
            loader_pdf = PyPDFLoader(source_doc)
            loader_pdf_list.append(loader_pdf)
            documents.extend(loader_pdf.load())
            st.session_state.retriever_doc = documents
    else:
        # st.warning(f"Please upload the documents")
        pass
        
def conversational_retrieval_chain(retriever):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    # texts=text_splitter.split_documents(documents)
    texts=text_splitter.split_documents(retriever)
    embeddings=OpenAIEmbeddings()
    db=Chroma.from_documents(texts, embeddings)
    retriever=db.as_retriever(search_type="similarity", search_kwargs={"k":3})
    qa = ConversationalRetrievalChain.from_llm(llm=ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0),
         retriever=retriever,
         return_source_documents=True)
    # qa = ConversationalRetrievalChain.from_llm(OpenAI(), retriever, return_source_documents=True)
    st.session_state.qachain = qa
    # return qa   
    
def query_llm(user_input):
    vAR_qa = st.session_state.qachain
    # qa = conversational_retrieval_chain(retriever)
    # query="Can I add beneficiary to my retirement plan?"
    query = user_input
    result_queries=vAR_qa({"question":query, "chat_history":st.session_state.messages})
    # print(result_queries["answer"])
    st.session_state.messages.append((query, result_queries["answer"]))
    # return result_queries["answer"]
    return result_queries["answer"]+"\t CITATION : "+str(result_queries["source_documents"][0].metadata)
    
def QAwithLangchain():
    start = time.time()
    start_time1 = time.time()
    input_fields()
    print('input file read - ',time.time()-start_time1)
    submit_button = False
    
    
    

    

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if 'qachain' not in st.session_state:
        st.session_state.qachain = None
    if 'retriever' not in st.session_state:
        st.session_state.retriever = None
        
    if 'source_docs' not in st.session_state:
        st.session_state.source_docs = None
    
    start_time2 = time.time()
    if not st.session_state.retriever:
        with st.spinner("Processing files!"):
            process_documents()
    
    print('input file process - ',time.time()-start_time2)
    
    if 'generated' not in st.session_state:
        if st.session_state.source_docs:
            # st.session_state['generated'] = ["We provide customized information to our registered users on our website (www.edd.ca.gov)?"]
            st.session_state['generated'] = ["Ask your question here"]


    if 'past' not in st.session_state:
        if st.session_state.source_docs:
            st.session_state['past'] = ["We're delighted to have you in our calPERS Retirement System Live Agent Chat room!"]
    
    container1 = st.container()
    container2 = st.container()
    
    
    start_time3 = time.time()
    with container2:
        # for message in st.session_state.messages:
        #     st.chat_message('human').write(message[0])
        #     st.chat_message('ai').write(message[1])    
        # #
        # if query := st.chat_input():
        #     st.chat_message("human").write(query)
        #     response = query_llm(st.session_state.retriever, query)
        #     st.chat_message("ai").write(response)
        if st.session_state.source_docs:
            with st.form(key='my_form ', clear_on_submit=True):
                if st.session_state.retriever_doc:
                    user_input = st.text_input("Prompt:", placeholder="What information are you looking for?", key='user_input')
                    if st.session_state.qachain is None:
                        conversational_retrieval_chain(st.session_state.retriever_doc)
                    response = query_llm(user_input)
                    #qa_chain

                    # Add custom CSS for the button
                    st.write(
                        """
                        <style>
                        .stButton button {
                            background-color: #007bff; /* Replace with your desired background color */
                            color: #fff; /* Text color */
                            border: none; /* Remove the default button border */
                            padding: 10px 20px; /* Adjust padding as needed */
                            border-radius: 5px; /* Add rounded corners */
                            cursor: pointer;
                        }
                        </style>
                        """,
                        unsafe_allow_html=True
                    )
                    submit_button = st.form_submit_button(label='Interact with LLM')
                    
                    if submit_button and user_input:
                        
                        st.session_state['past'].append(user_input)
                        st.session_state['generated'].append(str(response))
    print('query llm response - ',time.time()-start_time3)
    if 'generated' in st.session_state:         
        if st.session_state['generated']:
            with container1:
                for i in range(len(st.session_state['generated'])):
                    message(st.session_state["past"][i],is_user=True, key=str(i) + '_user ', avatar_style="big-smile")
                    message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")
                # with st.chat_message("user"):
                    #     st.write(st.session_state["past"][i])
                    # with st.chat_message("assistant"):
                    #     st.write(st.session_state["generated"][i])
                    
    print('overall time - ',time.time()-start)      
    
    
