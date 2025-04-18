from crewai import Task
from agents import business_analyst, design_agent,developer_agent,tester_agent

# Business analyst task
business_analyst_task = Task(
    description=(
        "Given a high-level business requirement, create a detailed list of user stories in the format: "
        "'As a [role], I want to [action], so that [benefit]'. "
        "Ensure completeness, clarity, and relevance, and include well-defined acceptance criteria. "
        "*Do NOT include system design details or technical aspects.*"
    ),
    agent=business_analyst,
    expected_output="A structured list of user stories with clear acceptance criteria.",
)

# Design agent task
design_task = Task(
    description=(
        "Create a detailed software architecture and system design **based strictly on the user stories** from the Business Analyst for {topic}. "
        "Ensure the design includes system components, database choices, data flow, and UI wireframes. "
        "**Avoid repeating business requirements, user stories, security considerations, or future enhancements.**"
         
    ),
    inputs=["topic"],  # Explicit input for topic
    agent=design_agent, 
    expected_output="A structured design document including system architecture, tech stack, and UI wireframes, avoiding duplicates",
)


developer_task = Task(
     description=(       
        "Develop a fully functional, scalable, and well-structured codebase for {topic} based on the business requirement design document. "
        "Ensure best practices in software development, modularity, and efficiency. "
        "Write production-ready code that adheres to industry standards, including security, performance, and maintainability. "
        "Use appropriate design patterns and follow the specified tech stack. "
        "Document the code with meaningful comments explaining key implementation decisions, logic flow, and API endpoints (if applicable). "
        "Ensure the implementation is testable, extendable, and ready for deployment."


    ),
    inputs=["topic"],  # Explicit input for topic
    agent=developer_agent,
        expected_output=(
        "A fully implemented, structured, and well-commented codebase for the specified project, "
        "ready for testing, deployment, and future enhancements."
    ),
)
