#!/bin/bash

# CrewAI Neo4j FastAPI Server Startup Script

echo "Starting CrewAI Neo4j FastAPI Server..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "Error: .env file not found. Please copy sample.env to .env and configure your environment variables."
    exit 1
fi

# Load environment variables
source .env

# Check required environment variables
if [ -z "$OPENAI_API_KEY" ]; then
    echo "Error: OPENAI_API_KEY not set in .env file"
    exit 1
fi

if [ -z "$NEO4J_URI" ]; then
    echo "Error: NEO4J_URI not set in .env file"
    exit 1
fi

if [ -z "$NEO4J_USERNAME" ]; then
    echo "Error: NEO4J_USERNAME not set in .env file"
    exit 1
fi

if [ -z "$NEO4J_PASSWORD" ]; then
    echo "Error: NEO4J_PASSWORD not set in .env file"
    exit 1
fi

# Set default port if not specified
if [ -z "$PORT" ]; then
    export PORT=12000
fi

echo "Environment variables loaded successfully"
echo "Starting server on port $PORT..."

# Install dependencies if needed
if [ ! -d ".venv" ]; then
    echo "Installing dependencies..."
    poetry install --no-root
fi

# Start the server
poetry run python main.py