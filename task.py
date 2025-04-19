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
tester_task = Task(
    description=(
        "You are a senior QA engineer at a leading software company. Based on the provided production-grade codebase, "
        "develop a complete suite of automated tests to validate the system’s functionality, performance, and reliability for {topic}. "
        "Follow best practices in software testing, such as test-driven development (TDD), black-box and white-box testing, and boundary value analysis. "
        "Create tests that cover API endpoints, database operations, business logic, and user interactions. "
        "Include both positive and negative test cases, edge cases, and integration tests. "
        "Ensure the test suite is easy to maintain, modular, and runnable via test runners such as Jest, Mocha (for Node.js), and React Testing Library. "
        "Mock dependencies and isolate units of code as appropriate. "
        "Clearly document the purpose of each test case and its expected behavior."
    ),
    inputs=["topic"],
    agent=tester_agent,
    expected_output=(
        "A complete, structured, and production-grade test suite for the provided codebase. "
        "Include backend API tests (e.g., using Jest or Mocha with Supertest), frontend component tests (e.g., React Testing Library or Jest), and database validation logic. "
        "Ensure high test coverage, clear assertions, proper mocking, and independence between tests. "
        "Each test should be self-explanatory and follow best practices for unit, integration, and end-to-end testing. "
        "Output should be ready for CI/CD pipelines and future maintainability."
    ),
)
