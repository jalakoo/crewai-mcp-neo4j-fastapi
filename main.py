from fastapi import FastAPI, Query
from crew_manager import run
import uvicorn
import os

app = FastAPI()

@app.get("/crewai")
async def prompt_crew_endpoint(prompt: str = Query(..., 
    description="The prompt / command to process",
    example="How many records are there?")):

    print(f'/crewai endpoint: Input prompt: {prompt}')
    return run(prompt)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 4000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)