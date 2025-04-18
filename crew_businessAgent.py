# #crew_b.py

# from crewai import Crew, Process
# from task import business_analyst_task
# from agents import business_analyst

# business_requirements = input("Enter business requirements: ")
# def run_business_analyst(business_requirements):
# # def run_business_analyst():

#     # Run Business Analyst Agent
#     crew_ba = Crew(
#         agents=[business_analyst],
#         tasks=[business_analyst_task],
#         process=Process.sequential
#     )

#     ba_output = crew_ba.kickoff(inputs={'topic': business_requirements})
#     ba_text = ba_output.result if hasattr(ba_output, 'result') else str(ba_output)
    

#     # Save Business Analyst Output to a File
#     with open("User_Stories.txt", "w", encoding="utf-8") as file:
#         file.write(ba_text)


#     with open("User_Stories.txt", "r", encoding="utf-8") as file:
#         return file.read() 
    

#     print("\n===== Business Analyst Output =====\n")
#     print(ba_text)


# # ONLY FOR BUILDING AI AGENTS, MUST BE COMMENTED FOR BUILDING UI
# if __name__ == "__main__":
#     run_business_analyst(business_requirements)


# import streamlit as st
from crewai import Crew, Process
from task import business_analyst_task
from agents import business_analyst
from rag import retrieve_and_generate
from datetime import datetime
# import os
from project_status import project_status
# import os

# requirements = st.session_state.get("requirements", "No RFP has been uploaded yet.")
# business_requirements = input("Enter business requirements: ")

# os.environ["LANGCHAIN_TRACING_V2"] = "false"
# os.environ["LANGCHAIN_PROJECT"] = ""


def run_business_analyst():
# def run_business_analyst():

    # Run Business Analyst Agent

    try:
        with open("extracted_reqmts.txt", "r", encoding="utf-8") as file:
            business_requirements = file.read()
    except FileNotFoundError:
        return "❌ Error: 'extracted_reqmts.txt' not found. Please extract requirements first."


    crew_ba = Crew(
        agents=[business_analyst],
        tasks=[business_analyst_task],
        process=Process.sequential
    )
    prompt=retrieve_and_generate(business_requirements)
    ba_output = crew_ba.kickoff(inputs={'topic': business_requirements+prompt})
    print(ba_output)
    ba_text = ba_output.result if hasattr(ba_output, 'result') else str(ba_output)
    

    # Save Business Analyst Output to a File
    with open("User_Stories.txt", "w", encoding="utf-8") as file:
        file.write(ba_text)

    # user_story_count = ba_text.lower().count("Acceptance Criteria")  # Simple heuristic
    import re

    # user_story_count = len(re.findall(r'^\d+\.\s+\*\*As a', ba_text, re.MULTILINE))
    user_story_count = len(re.findall(r'Acceptance Criteria:', ba_text))



    # ✅ Update project status
    project_status["user_stories_generated"] = user_story_count
    project_status["last_update"] = datetime.now().strftime("%b %d, %Y %I:%M %p")
    project_status["notes"].append(f"{user_story_count} user stories generated on {project_status['last_update']}")


    return ba_text
    # with open("User_Stories.txt", "r", encoding="utf-8") as file:
    #     return file.read() 
    
    # print("\n===== Business Analyst Output =====\n")
    # print(ba_text)


# ONLY FOR BUILDING AI AGENTS, MUST BE COMMENTED FOR BUILDING UI
# if __name__ == "__main__":
#     run_business_analyst(business_requirements)