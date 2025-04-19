- Pitch Video link : https://drive.google.com/file/d/1T6nSzjjwp1AXK-OlgaaHHsEqrQY-cINm/view?usp=sharing  
- Demo Video link : https://drive.google.com/file/d/1sg43tgS1IGhGwoqCU2AFYUOTfeLGhXda/view?usp=sharing  

- **DevVerse: AI-Powered Virtual Development Pod**  
  "Bringing intelligence to requirements — and speed to solutions."
  
  **DevVerse** is an AI-powered assistant that automates the transformation of plain English RFPs (Request for Proposals) into structured, implementation-ready development assets — all through an intelligent pipeline of role-based autonomous agents and Retrieval-Augmented Generation (RAG).


- What is DevVerse?  
  DevVerse mimics a real-world project team using intelligent agents like:  
  🔹Business Analyst Agent – Extracts user stories  
  🔹Design Agent – Generates UI/UX components & architecture  
  🔹Developer Agent – Produces backend code & database structure  
  🔹Tester Agent – Builds test cases based on user stories and code  
  These agents collaborate to convert an RFP into project artifacts — automatically, intelligently, and instantly.  

- Problem We Solve:-  
  RFPs are often written in unstructured, plain English.  
  Converting them into usable formats (user stories, UI layouts, test cases, etc.) takes time, manual effort, and domain expertise.  
  Scaling this process across domains like finance, e-commerce, or healthcare becomes inefficient.  

- Our Solution:-  
  DevVerse automates this workflow using a smart, modular pipeline:  
  🔹Embedding : Creation	RFP is encoded into semantic vectors  
  🔹Vector Search (ChromaDB) : Retrieves domain-relevant templates  
  🔹Agent Collaboration : Agents extract and generate structured outputs  
  🔹LLM Response : Final context goes to LLM (Gemini-1.5-flash) to generate artifacts  

- Tech Stack:-  
  Frontend : Streamlit  
  Backend : Python, CrewAI  
  LLM : API	Gemini-1.5-flash  
  Vector DB : ChromaDB  
  Embeddings : Sentence Transformers  
  Agent Framework : CrewAI, Prompt Chaining  

- Agents in Action:-  
  Each agent plays a defined role in the pipeline:  
  🔹Business Analyst Agent : Extracts domain keywords and requirements; Generates user stories based on RFP understanding  
  🔹Design Agent : Selects UI layouts from template pool; Builds hierarchy and architecture diagrams  
  🔹Developer Agent : Suggests database schema and backend module layout (Extendable to generate code skeletons)  
  🔹Tester Agent : Derives test cases from user stories and functions; Suggests automation test structure  

- System Architecture Overview:-  
  [User Input: RFP]  
        ↓  
  [Vectorization: Sentence Embedding]  
        ↓  
  [ChromaDB Search]  
        ↓  
  [Relevant Format Retrieval]  
        ↓  
  [Agent Collaboration]  
        ↓  
  [Final Prompt Assembly]  
        ↓  
  [LLM Generation]  
        ↓  
  [User Stories | Design | Code | Test Cases]  

- Impact:-  
  🔹80%+ reduction in manual effort  
  🔹Rapid transition from RFP to assets  
  🔹Standardized documentation across projects  
  🔹Domain-agnostic: works for fintech, healthcare, e-commerce, etc.  

- Future Scope:-  
  Add agents like UI/UX Designer, Scrum Master, Security Expert  
  Generate backend code skeletons and API specs  
  Integrate with tools like JIRA, GitHub Projects, Figma  

- Team:-  
  Priya Kumari  
  Tideesha Saha  
  Prakriti Mukhopadhyay  
  Debarati Das  
