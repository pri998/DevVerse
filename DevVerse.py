import streamlit as st
import PyPDF2
from Extraction import process_pdf_text
import time
from crew_businessAgent import run_business_analyst
from crew_designAgent import run_design_agent

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

                # with open("extracted_reqmts.txt", "w", encoding="utf-8") as f:
                #     for req in requirements:
                #         f.write(req + "\n")
                # with st.expander("Extracted Requirements", expanded=False):
                #     if requirements:
                #         for i, req in enumerate(requirements, 1):
                #             st.markdown(f"**{i}.** {req}")
                #     else:
                #         st.warning("No clear requirements found.")
                
            st.markdown("---")

            #Business Analyst Agent
            st.subheader("Business Analyst Agent")
            with st.spinner("Generating Business Analyst Output..."):
                start_time = time.time()
                ba_text = run_business_analyst()
                end_time = time.time()
                generation_time = end_time - start_time
            
                st.markdown(f"Generation time: {generation_time:.2f} seconds.  <span style='color:green;'> Generated Output ✅</span>", unsafe_allow_html=True)
                ba_output = f'<div style="border: 3px solid #b4d6e3;text-align:left; padding: 20px; border-radius: 5px; color: black; background-color: white; width: 100%;">{ba_text}</div>'

            with st.expander("User Stories", expanded=False):
                st.subheader("Business Analyst Agent Output:")
                st.markdown(ba_output,unsafe_allow_html=True)


            #Design Agent
            st.subheader("Design Agent")
            with st.spinner("Generating Design Agent Output..."):
                start_time = time.time()
                # result = crew_d.run_design_agent()
                design_text = run_design_agent()
                end_time = time.time()
                generation_time = end_time - start_time
            
                st.markdown(f"Generation time: {generation_time:.2f} seconds.  <span style='color:green;'> Generated Output ✅</span>", unsafe_allow_html=True)
                da_output = f'<div style="border: 3px solid #b4d6e3; padding: 10px; border-radius: 5px; color: black; background-color: white; width: 100%;">{design_text}</div>'

            with st.expander("System Design and Architecture", expanded=False):
                st.subheader("Design Agent Output:")
                st.markdown(da_output, unsafe_allow_html=True)

            #Developer Agent
            st.subheader("Developer Agent")
            with st.spinner("Generating Developer Agent Output..."):
                start_time = time.time()
                # result = crew_dev.run_developer_agent()
                code = run_developer_agent()
                end_time = time.time()
                generation_time = end_time - start_time       
                st.markdown(f"Generation time: {generation_time:.2f} seconds.  <span style='color:green;'> Generated Output ✅</span>", unsafe_allow_html=True)

            with st.expander("Production-ready Codebase", expanded=False):
                st.subheader("Developer Agent Output:")
                st.code(code)
