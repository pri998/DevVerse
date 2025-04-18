from crewai import Crew, Process
from task import design_task
from agents import design_agent
from rag import retrieve_and_generate
from datetime import datetime
# import os
from project_status import project_status

def run_design_agent():
    # Read Business Analyst Output from File
    with open("User_Stories.txt", "r", encoding="utf-8") as file:
        ba_text = file.read()
    return work(ba_text)

# def run_design_agent2(user_input):
#     return work(user_input)


def work(text):
    # Run Design Agent
    crew_design = Crew(
        agents=[design_agent],
        tasks=[design_task],
        process=Process.sequential
    )
    prompt=retrieve_and_generate(text)
    design_output = crew_design.kickoff(inputs={'topic': text+prompt})
    design_text = design_output.result if hasattr(design_output, 'result') else str(design_output)
    with open("System_Design.txt", "w", encoding="utf-8") as file:
        file.write(design_text)

    project_status["design_document_generated"] = True
    project_status["last_update"] = datetime.now().strftime("%b %d, %Y %I:%M %p")
    project_status["notes"].append(f"System Design and Architecture has been generated on {project_status['last_update']}")
    
    
    return design_text
