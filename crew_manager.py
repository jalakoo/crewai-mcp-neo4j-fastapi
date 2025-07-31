# OPTIONAL -------------------------------
# Using ollama - by default OpenAI is used
# Remove / comment this block if using OpenAI
# from crewai import LLM
# from langchain_community.chat_models import ChatOpenAI

# llm = ChatOpenAI(
#     model="ollama/mixtral:latest",
#     base_url="http://localhost:11434",
#     streaming=True
# )
# ----------------------------------------

from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
from dotenv import load_dotenv
import os

load_dotenv()

# Create a StdioServerParameters object
server_params = [
    StdioServerParameters(
        command="uvx",
        args=["mcp-neo4j-cypher"],
        env=os.environ,
    )
]


# Optionally logging callbacks from Agents & Tasks
def log_step_callback(output):
    print(
        f"""
        Step completed!
        details: {output.__dict__}
    """
    )


def log_task_callback(output):
    print(
        f"""
        Task completed!
        details: {output.__dict__}
    """
    )

def mcp_crew(tools):

    print(f"Available tools from MCP server(s): {[tool.name for tool in tools]}")

    analyst_agent = Agent(
        role="MCP Tool User",
        goal="Utilize tools from MCP servers.",
        backstory="I can connect to MCP servers and use their tools.",
        tools=tools,
        max_iterations=3,
        reasoning=False,  # Optional
        verbose=False,  # Optional
        step_callback=log_step_callback,  # Optional
        # llm=llm, # Optional - Remove if using OpenAI
    )

    # Passing query directly into task
    processing_task = Task(
        description="""Process the following prompt about the Neo4j graph database: {prompt}""",
        expected_output="A brief report on the outcome of the command: {prompt}",
        agent=analyst_agent,
        callback=log_task_callback,  # Optional
    )

    return Crew(agents=[analyst_agent], tasks=[processing_task], verbose=False)

# Convenience for fastAPI call
def run(prompt: str):
    with MCPServerAdapter(server_params) as tools:
        crew = mcp_crew(tools)
        result = crew.kickoff(inputs={"prompt": prompt})
    return {"result": result}


# For running as a script
if __name__ == "__main__":

    write_command = "Create a database record for a company named 'Acme Inc'"
    read_command = "Describe the data from the database"
    result = run(write_command)

    print(
        f"""
        Query completed!
        result: {result}
    """
    )
