import streamlit as st
import PyPDF2
from Extraction import process_pdf_text

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styleDevVerse.css")

st.markdown("""
    <h1 id="Upload-h1" style="font-size: 2.5rem;color: #1d547b;text-align: center;">Kickstart Your Software Journey – <span id="RFP-span-id">Submit your RFP</span></h1>
            """,unsafe_allow_html=True)
st.markdown("""
            <p style="text-align:center" id="subtext">Easily upload your RFP (Request for Proposal) in PDF format. Our AI-powered dev pods will analyze your requirements and jump into action. Let’s build something amazing together.</p>
            """, unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["pdf"])

if uploaded_file:
    # Extract text from PDF file object
    pdf_text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        pdf_text += page.extract_text() + "\n"

    st.success("PDF uploaded and text extracted successfully!")


    if st.button("Initialize Project"):
            
            with st.spinner("Analyzing..."):
                # Step 1: Extract requirements
                requirements, tfidf_vectors = process_pdf_text(pdf_text)
                st.session_state.requirements = "\n".join(requirements)

                with open("extracted_reqmts.txt", "w", encoding="utf-8") as f:
                    for req in requirements:
                        f.write(req + "\n")
                with st.expander("Extracted Requirements", expanded=False):
                    if requirements:
                        for i, req in enumerate(requirements, 1):
                            st.markdown(f"**{i}.** {req}")
                    else:
                        st.warning("No clear requirements found.")