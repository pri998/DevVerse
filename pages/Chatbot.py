
from streamlit_chat import message
import streamlit as st
from datetime import datetime
from project_status import project_status
# from DEVDESK import requirements
import google.generativeai as genai
st.set_page_config(page_title="DevPod Chat", page_icon="💬")

# Gemini API key setup
genai.configure(api_key="AIzaSyDt1yuhcTKzBu8vfN-0oDSe2cRQpAh60UE")
# genai.configure(api_key="AIzaSyARU8QB5zBI5kC6mXStg4sDnfPGxLN7tXo")


st.markdown("""
    <h1 id="chatbot-h1"> <span id="Project-progress-span-id">Project Progress</span>- Chatbot</h1>
            """,unsafe_allow_html=True)
st.markdown("""
    <style>
            #Project-progress-span-id{
                    background-color: #1d547b;
                    color:white;
                    padding: 0 5px;
                    border-radius: 10px;
            }
            </style>
            """,unsafe_allow_html=True)

st.subheader("Ask anything about your software project's status!")

requirements = st.session_state.get("requirements", "No RFP has been uploaded yet.")


# Format project status
def format_project_status(status: dict) -> str:
    return (
        f"- Requirements Extracted: {status['requirements_extracted']}\n"
        f"- User Stories Generated: {status['user_stories_generated']}\n"
        f"- Design Document Generated: {'Yes' if status['design_document_generated'] else 'No'}\n"
        f"- Code Generated: {'Yes' if status['code_generated'] else 'No'}\n"
        f"- Test Cases Generated: {status['test_cases_generated']}\n"
        f"- Deployment Done: {'Yes' if status['deployment_done'] else 'No'}"
    )

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input box
user_input = st.chat_input("Ask about your project...")

if user_input:
    # Save user message
    st.session_state.chat_history.append(("You", user_input))

    # Build Gemini prompt
    prompt = f"""
    You are a helpful assistant that answers queries about a software project and it's progress.
    Here is the RFP for the project: {requirements}
    Analyse the RFP carefully and answer queries related to the project.

    For project status, give the status matching to the given format, not according to what is mentioned in the RFP file:
    Here is the current project status:
    {format_project_status(project_status)}

    User's question: "{user_input}"

    Answer considering the above project status.
    If no work is done, assume that the RFP has not yet been uploaded.
    """

    # Call Gemini API
    with st.spinner("Thinking..."):
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        response = model.generate_content(prompt)

    # Save bot response
    st.session_state.chat_history.append(("Bot", response.text))

# Display chat history
for speaker, msg in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(
            f"<p style='width:fit-content; background-color:#e6f5ff; border-radius: 10px; padding:8px 12px; margin: 10px 0; margin-left:auto; text-align:right;'>"
            f"<b>You:</b> {msg}</p>", unsafe_allow_html=True)
    else:
        st.markdown(
            f"<div style='width:fit-content; max-width:80%; border: 1.5px solid #1d547b; border-radius: 10px; padding:10px 12px; margin: 10px 0;'>"
            f"<b>Bot:</b> {msg}</div>", unsafe_allow_html=True)
