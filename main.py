from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from cai import run_crew_query
import uvicorn
import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class QueryRequest(BaseModel):
    query: str

class HealthResponse(BaseModel):
    status: str
    message: str

# Initialize FastAPI app
app = FastAPI(
    title="CrewAI Neo4j FastAPI Server",
    description="A FastAPI server that uses CrewAI and Neo4j MCP to process queries about graph database data",
    version="1.0.0"
)

# Configure CORS
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint with basic information"""
    return {
        "message": "CrewAI Neo4j FastAPI Server",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        message="Server is running and ready to process queries"
    )

@app.post("/crewai", response_model=Dict[str, Any])
async def query_crew_endpoint(request: QueryRequest):
<<<<<<< HEAD
    """
    Process a natural language query about Neo4j graph database data using CrewAI
    
    Args:
        request: QueryRequest containing the natural language query
        
    Returns:
        Dict containing the processed result from CrewAI
    """
    try:
        print(f'/crewai endpoint: Input query: {request.query}')
=======
    """Process queries using CrewAI and Neo4j MCP"""
    print(f'/crewai endpoint: Input query: {request.query}')

    try:
>>>>>>> origin/feat/production-deployment-setup
        result = run_crew_query(request.query)
        return result
    except Exception as e:
        print(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 12000))
    host = os.getenv("HOST", "0.0.0.0")
    uvicorn.run("main:app", host=host, port=port, reload=True)