
from crewai import Crew, Process
from task import developer_task
from agents import developer_agent
from datetime import datetime
from project_status import project_status

def run_developer_agent():
    # Read Design Agent Output from File
    with open("System_Design.txt", "r", encoding="utf-8") as file:
        design_text = file.read()
    return work(design_text)

def work(text):
    # Run Developer Agent
    crew_dev = Crew(
        agents=[developer_agent],
        tasks=[developer_task],
        process=Process.sequential
    )


    dev_output = crew_dev.kickoff(inputs={'topic': text})
    dev_text = dev_output.result if hasattr(dev_output, 'result') else str(dev_output)

    # Save Developer Output to a File
    with open("Implementation_Code.txt", "w", encoding="utf-8") as file:
        file.write(dev_text)
    
    project_status["code_generated"] = True
    project_status["last_update"] = datetime.now().strftime("%b %d, %Y %I:%M %p")
    project_status["notes"].append(f"Codebase has been generated on {project_status['last_update']}")
    
    
    return dev_text