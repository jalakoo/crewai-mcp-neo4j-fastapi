# OPTIONAL -------------------------------
# Using ollama - by default OpenAI is used
# Remove / comment this block if using OpenAI
# from crewai import LLM
# from langchain_community.chat_models import ChatOpenAI

# llm = ChatOpenAI(
#     model="ollama/qwen3:latest",
#     base_url="http://localhost:11434",
#     streaming=True
# )
# ----------------------------------------

from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create a StdioServerParameters object
server_params=[
    StdioServerParameters(
        command="uvx", 
        args=["mcp-neo4j-cypher"],
        env=os.environ,
    )
]

# Optionally logging callbacks from Agents & Tasks
def log_step_callback(output):
    print(f"""
        Step completed!
        details: {output.__dict__}
    """)

def log_task_callback(output):
    print(f"""
        Task completed!
        details: {output.__dict__}
    """)

# Create and run Crew
def run_crew_query(query: str):
    """
    Process a query using CrewAI with Neo4j MCP tools
    
    Args:
        query (str): Natural language query about the Neo4j database
        
    Returns:
        dict: Result containing the processed answer
    """
    try:
        # Validate environment variables
        required_env_vars = ["OPENAI_API_KEY", "NEO4J_URI", "NEO4J_USERNAME", "NEO4J_PASSWORD"]
        missing_vars = [var for var in required_env_vars if not os.getenv(var)]
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

        with MCPServerAdapter(server_params) as tools:
        
            print(f"Available tools from Stdio MCP server: {[tool.name for tool in tools]}")

            analyst_agent = Agent(
                role="Neo4j Data Analyst",
                goal="Analyze and query Neo4j graph database to provide comprehensive answers to user questions.",
                backstory="""You are an expert data analyst specializing in graph databases and Neo4j. 
                You have deep knowledge of Cypher query language and can interpret complex graph relationships 
                to provide meaningful insights from the data.""",
                tools=tools,
                reasoning=True, # Enable reasoning for better analysis
                verbose=True, # Enable verbose for debugging
                step_callback=log_step_callback, # Optional
                # llm=llm, # Optional - Remove if using OpenAI
            )
            
            # Passing query directly into task
            processing_task = Task(
                description="""Analyze the following query about the Neo4j graph database: {query}
                
                Use the available Neo4j tools to:
                1. Understand what data the user is asking about
                2. Construct appropriate Cypher queries to retrieve the relevant information
                3. Analyze the results and provide insights
                4. Present a clear, comprehensive answer to the user's question
                
                Be thorough in your analysis and provide context for your findings.""",
                expected_output="""A comprehensive, well-structured answer that includes:
                - Direct answer to the query: {query}
                - Supporting data and evidence from the Neo4j database
                - Any relevant insights or patterns discovered
                - Clear explanation of the methodology used""",
                agent=analyst_agent,
                callback=log_task_callback, # Optional
            )
            
            data_crew = Crew(
                agents=[analyst_agent],
                tasks=[processing_task],
                verbose=True
            )
        
            result = data_crew.kickoff(inputs={"query": query})
            return {"result": result, "status": "success"}
            
    except Exception as e:
        print(f"Error in run_crew_query: {str(e)}")
        return {"error": str(e), "status": "error"}

# For running as a script
# ie poetry run python cai.py
if __name__ == "__main__":
    result = run_crew_query("Which staff member manages the delivery service delivering the most orders?")
    print(f"""
        Query completed!
        result: {result}
    """)