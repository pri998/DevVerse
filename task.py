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
