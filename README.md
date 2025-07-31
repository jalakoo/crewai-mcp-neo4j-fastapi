# FastAPI server using CrewAI and Neo4j MCP

This is a simple FastAPI server that uses CrewAI and Neo4j MCP to process queries about the data within a Neo4j graph database.

## Requirements
- [Poetry](https://python-poetry.org) for virtual env and dependency management
- [OpenAI Key](https://platform.openai.com/api-keys) for LLM inference
- Running [Neo4j](https://neo4j.com) database


## Setup
1. Copy the sample.env file to .env and fill in the values.
2. Run `poetry install`


## Run the crew_manager as a script
```

poetry run python crew_manager.py

```

## Start FastAPI Server
```

poetry run uvicorn main:app --reload --port 4000

```

Interactive docs will be accessible at:
http://127.0.0.1:8000/docs
