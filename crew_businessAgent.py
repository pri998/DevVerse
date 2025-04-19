from crewai import Crew, Process
from task import business_analyst_task
from agents import business_analyst
from rag import retrieve_and_generate
from datetime import datetime

from project_status import project_status


# requirements = st.session_state.get("requirements", "No RFP has been uploaded yet.")
# business_requirements = input("Enter business requirements: ")


def run_business_analyst():
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

    import re
    user_story_count = len(re.findall(r'Acceptance Criteria:', ba_text))
    
    # ✅ Update project status
    project_status["user_stories_generated"] = user_story_count
    project_status["last_update"] = datetime.now().strftime("%b %d, %Y %I:%M %p")
    project_status["notes"].append(f"{user_story_count} user stories generated on {project_status['last_update']}")


    return ba_text
