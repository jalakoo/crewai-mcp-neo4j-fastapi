from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from cai import run_crew_query
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class QueryRequest(BaseModel):
    query: str

app = FastAPI(
    title="CrewAI Neo4j FastAPI Server",
    description="A FastAPI server that uses CrewAI and Neo4j MCP to process queries about graph database data",
    version="0.1.0"
)

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    """Root endpoint providing basic API information"""
    return {
        "message": "CrewAI Neo4j FastAPI Server",
        "version": "0.1.0",
        "status": "running",
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "query": "/crewai"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "crewai-neo4j-fastapi"}

@app.post("/crewai")
async def query_crew_endpoint(request: QueryRequest):
    """Process queries using CrewAI and Neo4j MCP"""
    print(f'/crewai endpoint: Input query: {request.query}')

    try:
        result = run_crew_query(request.query)
        return result
    except Exception as e:
        print(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 4000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)