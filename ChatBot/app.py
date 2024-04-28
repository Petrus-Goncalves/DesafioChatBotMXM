# Módulos relacionados a modelos de linguagens da plataforma HuggingFace
# from langchain.embeddings import HuggingFaceInstructEmbeddings
# from langchain.llms import HuggingFaceHub

import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template

def extrair_texto_pdf(pdf_docs):
    texto = ""
    for pdf in pdf_docs:
        leitor_pdf = PdfReader(pdf)
        for pagina in leitor_pdf.pages:
            texto += pagina.extract_text()
    return texto


def extrair_chunks_texto(texto):
    separador_texto = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = separador_texto.split_text(texto)
    return chunks


def criacao_vetores(chunks_texto):
    # Caso queira a utilização de outro modelo de linguagem, utiliza a atribuição da variável abaixo ao invés da atribuição atual
    # embeddings = HuggingFaceInstructEmbeddings(model_name="philschmid/bart-large-cnn-samsum")

    embeddings = OpenAIEmbeddings()
    deposito_vetores = FAISS.from_texts(texts=chunks_texto, embedding=embeddings)
    return deposito_vetores


def criacao_cadeia_conversacao(deposito_vetores):
    # Caso queira a utilização de outro modelo de linguagem, utiliza a atribuição da variável abaixo ao invés da atribuição atual
    # modelo_de_linguagem = HuggingFaceHub(repo_id="tincans-ai/gazelle-v0.2", model_kwargs={"temperature":1.0, "max_length":512})

    modelo_de_linguagem = ChatOpenAI()
    
    memoria = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    historico_conversacao = ConversationalRetrievalChain.from_llm(
        llm = modelo_de_linguagem,
        retriever = deposito_vetores.as_retriever(),
        memory = memoria
    )
    return historico_conversacao


def permanencia_pergunta_usuario(pergunta_usuario):
    resposta = st.session_state.conversation({'question': pergunta_usuario})
    st.session_state.chat_history = resposta['chat_history']

    for i, menssagem in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", menssagem.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", menssagem.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="ChatBot MXM",
                       page_icon=":robot_face:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Bem vindo ao ChatBot MXM :robot_face:")
    pergunta_usuario = st.text_input("Faça uma pergunta:   ")
    if pergunta_usuario:
        permanencia_pergunta_usuario(pergunta_usuario)

    with st.sidebar:
        st.subheader("Seus documentos")
        pdf_docs = st.file_uploader(
            " Clique em 'Browse files' e selecione seus PDF's.  Depois, clique em 'Carregar'", accept_multiple_files=True)
        if st.button("Carregar"):
            with st.spinner("Carregando"):
                # Extração do PDF para uma única string 
                texto_bruto = extrair_texto_pdf(pdf_docs)

                # Quebra dessa stringem pequenos blocos chamados "chunks"
                chunks_do_texto = extrair_chunks_texto(texto_bruto)

                # Criação de uma base de vetores dos blocos (chunks)
                deposito_vetores = criacao_vetores(chunks_do_texto)

                # Criação de uma cadeia de conversação usuário-chatbot
                st.session_state.conversation = criacao_cadeia_conversacao(
                    deposito_vetores)


if __name__ == '__main__':
    main()
