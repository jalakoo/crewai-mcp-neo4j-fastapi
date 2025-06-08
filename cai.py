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

            # Google Ads Campaign Analyst
            ads_analyst = Agent(
                role="Google Ads Campaign Analyst",
                goal="Analyze Google Ads campaign performance data to identify optimization opportunities and provide actionable recommendations for improving ROI, CTR, and conversion rates.",
                backstory="""You are a seasoned digital marketing analyst specializing in Google Ads optimization for trade businesses. 
                You have extensive experience analyzing campaign performance metrics, keyword effectiveness, audience targeting, 
                and conversion funnels. You excel at identifying underperforming campaigns, discovering high-value keywords, 
                and recommending budget reallocation strategies that maximize return on ad spend (ROAS) for tradespeople and contractors.""",
                tools=tools,
                reasoning=True,
                verbose=True,
                step_callback=log_step_callback,
                # llm=llm, # Optional - Remove if using OpenAI
            )
            
            # Website Optimization Specialist
            web_optimizer = Agent(
                role="Website Optimization Specialist", 
                goal="Analyze website performance data and user behavior to provide actionable recommendations for improving conversion rates, user experience, and lead generation.",
                backstory="""You are a conversion rate optimization expert specializing in trade business websites. 
                You understand how tradespeople's potential customers behave online, what drives them to request quotes, 
                and how to optimize landing pages, contact forms, and user journeys. You analyze traffic patterns, 
                bounce rates, conversion funnels, and user engagement to provide specific, implementable recommendations 
                that turn website visitors into qualified leads.""",
                tools=tools,
                reasoning=True,
                verbose=True,
                step_callback=log_step_callback,
                # llm=llm, # Optional - Remove if using OpenAI
            )
            
            # Determine which agent should handle the query based on content
            query_lower = query.lower()
            
            if any(keyword in query_lower for keyword in ['ads', 'campaign', 'google ads', 'ppc', 'cpc', 'roas', 'ad spend', 'keywords', 'bidding']):
                primary_agent = ads_analyst
                task_focus = "Google Ads campaign optimization"
            elif any(keyword in query_lower for keyword in ['website', 'conversion', 'landing page', 'traffic', 'bounce rate', 'user experience', 'seo']):
                primary_agent = web_optimizer  
                task_focus = "website optimization"
            else:
                # Default to ads analyst for general marketing queries
                primary_agent = ads_analyst
                task_focus = "digital marketing analytics"
            
            # Marketing Analytics Task
            marketing_analysis_task = Task(
                description=f"""Analyze the following marketing query for TradieMate: {{query}}
                
                Focus on {task_focus} and use the available Neo4j tools to:
                
                1. **Data Discovery**: Examine the database schema to understand available marketing data
                2. **Query Construction**: Build targeted Cypher queries to extract relevant campaign/website performance data
                3. **Performance Analysis**: Analyze metrics such as:
                   - Campaign performance (CTR, CPC, conversion rates, ROAS)
                   - Website analytics (traffic sources, user behavior, conversion funnels)
                   - Keyword effectiveness and search trends
                   - Audience segments and targeting performance
                4. **Insight Generation**: Identify patterns, trends, and optimization opportunities
                5. **Actionable Recommendations**: Provide specific, implementable strategies
                
                Consider the unique needs of trade businesses and their customers when analyzing the data.""",
                expected_output="""A comprehensive marketing analysis report that includes:
                
                **Executive Summary**
                - Key findings and primary recommendations for: {{query}}
                
                **Performance Metrics**
                - Current performance data with supporting evidence from Neo4j
                - Benchmark comparisons and trend analysis
                
                **Optimization Opportunities**
                - Specific areas for improvement with quantified potential impact
                - Budget reallocation recommendations
                - Targeting and messaging improvements
                
                **Action Plan**
                - Prioritized list of actionable recommendations
                - Implementation timeline and expected outcomes
                - Success metrics to track progress
                
                **Supporting Data**
                - Relevant Cypher queries used
                - Data visualizations or insights discovered
                - Methodology explanation""",
                agent=primary_agent,
                callback=log_task_callback,
            )
            
            # Create marketing analytics crew
            marketing_crew = Crew(
                agents=[ads_analyst, web_optimizer],
                tasks=[marketing_analysis_task],
                verbose=True,
                planning=True,  # Enable planning for better coordination
            )
        
            result = marketing_crew.kickoff(inputs={"query": query})
            return {"result": result, "status": "success"}
            
    except Exception as e:
        print(f"Error in run_crew_query: {str(e)}")
        return {"error": str(e), "status": "error"}

# For running as a script
# ie poetry run python cai.py
if __name__ == "__main__":
    result = run_crew_query("What are the top performing Google Ads campaigns and how can we optimize budget allocation to improve ROAS?")
    print(f"""
        Marketing Analysis completed!
        result: {result}
    """)