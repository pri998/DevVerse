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


design_agent = Agent(
    role="Software Designer",
    
     goal="Create a high-level software architecture and design based on user stories from the Business Analyst in {topic}. "
         "*Avoid repeating user stories, security considerations, or future enhancements.*",
    backstory="A highly experienced software architect specializing in designing scalable, efficient, and maintainable software systems. "
              "You define system components, data flow, and architecture without overlapping business analysis.",
    verbose=True,
    memory=True,
    tools=[],
    llm=gemini_llm,
    allow_delegation=True
)

developer_agent = Agent(
   role="Software Developer",
    goal=(
        '''  "Generate production-ready code based on the system design for {topic}. "
        "Implement all specified features and functionality while ensuring modularity, scalability, and performance. "
        "Follow the best practices in software development, and use appropriate design patterns. "
        "Ensure the code is well-commented, testable, and ready for deployment in real-world applications."
        "Generate ONLY code and nothing else" '''

        "You are a senior software engineer at a top-tier tech company. Given the following system design specification, generate complete, clean, and well-structured development code for {topic}."
        "The response must include only the code in the format typically used in the development/documentation phase of the software development life cycle (SDLC) in major tech companies."
        "Do not include explanations, comments outside the code, or disclaimers. Just return the fully structured code as it would appear in a professional codebase."
    ),
    backstory=(
        "An experienced software developer proficient in various programming languages and frameworks. "
        "You are skilled at translating system designs into clean, efficient, and maintainable code for web applications, mobile apps, APIs, and more. "
        "You focus on creating reliable solutions with a clear, readable code structure and high attention to detail."
    ),
    verbose=True,
    memory=True,
    tools=[],
    llm=gemini_llm,
    allow_delegation=True
)

