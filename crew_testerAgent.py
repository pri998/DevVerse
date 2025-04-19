from crewai import Crew, Process
from task import tester_task
from agents import tester_agent
from rag import retrieve_and_generate
from datetime import datetime
# import os
from project_status import project_status

def run_tester_agent():
    # Read Design Agent Output from File
    with open("Implementation_Code.txt", "r", encoding="utf-8") as file:
        code = file.read()
    return work(code)

# def run_developer_agent2(user_input):
#     return work(user_input)

def work(text):
    # Run Developer Agent
    crew_test = Crew(
        agents=[tester_agent],
        tasks=[tester_task],
        process=Process.sequential
    )

    prompt=retrieve_and_generate(text)
    tester_output = crew_test.kickoff(inputs={'topic': text+prompt})
    tester_text = tester_output.result if hasattr(tester_output, 'result') else str(tester_output)

    # Save Developer Output to a File
    with open("Test_Cases.txt", "w", encoding="utf-8") as file:
        file.write(tester_text)

    project_status["test_cases_generated"] = True
    project_status["last_update"] = datetime.now().strftime("%b %d, %Y %I:%M %p")
    project_status["notes"].append(f"Test Cases has been generated on {project_status['last_update']}")
    

    return tester_text

    # with open("Test_Cases.txt", "r", encoding="utf-8") as file:
    #     return file.read() 
    
# if __name__ == "__main__":
#     run_tester_agent()
