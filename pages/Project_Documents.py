import streamlit as st
import os;


st.markdown("""
    <h1 id="Upload-h1" style="font-size: 2.5rem;color: #1d547b;text-align: left;">Project – <span id="RFP-span-id" style="background-color:#1d547b; padding:0 10px; color:white; border-radius:10px">Documents</span></h1>
            """,unsafe_allow_html=True)

st.markdown("""
            <p style="text-align:left" id="subtext">Browse & Download Design Documents.</p>
            """, unsafe_allow_html=True)


st.markdown("""<style>
            .stDownloadButton{
            float:right;}  
            .st-emotion-cache-ocsh0s {   
            background-color: #1d547b;
            color: white;
            width: 20vw;
            text-align:left;
            justify-content:left;
            }
            </style>""",unsafe_allow_html=True)

ba_file_path = os.path.join(os.path.dirname(__file__), "..", "User_Stories.txt")
with open(ba_file_path, "r", encoding="utf-8") as file:
    ba_content = file.read()

design_file_path = os.path.join(os.path.dirname(__file__), "..", "System_Design.txt")
with open(design_file_path, "r", encoding="utf-8") as file:
    design_content = file.read()

code_file_path = os.path.join(os.path.dirname(__file__), "..", "Implementation_Code.txt")
with open(code_file_path, "r", encoding="utf-8") as file:
    code_content = file.read()

test_file_path = os.path.join(os.path.dirname(__file__), "..", "Test_Cases.txt")
with open(test_file_path, "r", encoding="utf-8") as file:
    test_content = file.read()


with st.expander("User Stories", expanded=False):
    st.markdown(ba_content, unsafe_allow_html=True)




st.download_button(
            label="📄 Download User Stories",
            data=ba_content,
            file_name="User Stories.txt",
            mime="text/plain"
        )

with st.expander("Design Document", expanded=False):
    st.markdown(design_content, unsafe_allow_html=True)

st.download_button(
            label="📄 Download Design Document",
            data=design_content,
            file_name="Design Document.txt",
            mime="text/plain"
        )

with st.expander("Codebase", expanded=False):
    st.markdown(code_content, unsafe_allow_html=True)

st.download_button(
            label="📄 Download Code",
            data=code_content,
            file_name="Code.txt",
            mime="text/plain"
        )

with st.expander("Test Cases", expanded=False):
    st.markdown(test_content, unsafe_allow_html=True)

st.download_button(
            label="📄 Download Test Cases",
            data=test_content,
            file_name="Test_Cases.txt",
            mime="text/plain"
        )