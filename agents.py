from crewai import Agent
from crewai import LLM
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


os.environ['GEMINI_API_KEY'] = ""

gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    verbose=True,
    temperature=0.3
)


business_analyst=Agent(
    role="Business Analyst",
    goal="Analyze high-level business requirements and generate *ONLY* user stories in {topic}. Do *NOT* include system design, architecture, technology stack, or database details.",
    backstory="A skilled business analyst with experience in Agile methodologies and user-centric design. "
              "Your expertise lies in translating abstract requirements into actionable user stories.",
    verbose=True,
    memory=True,
    tools=[],
    llm=gemini_llm,
    allow_delegation=True

)

