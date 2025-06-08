#!/bin/bash

# Build script for unified CrewAI FastAPI + Neo4j GDS Docker setup

set -e

echo "🏗️  Building CrewAI FastAPI with Neo4j Graph Data Science support..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Check if git submodules are initialized
if [ ! -f "graph-data-science/gradlew" ]; then
    echo "📦 Initializing Git submodules..."
    git submodule update --init --recursive
fi

# Build the unified Docker image
echo "🔨 Building unified Docker image..."
docker build -f Dockerfile.unified -t crewai-neo4j-gds:latest .

echo "✅ Build completed successfully!"
echo ""
echo "🚀 To run the application:"
echo "   Option 1 (Standalone): docker run -p 12000:12000 crewai-neo4j-gds:latest"
echo "   Option 2 (With Neo4j): docker-compose -f docker-compose.unified.yml up"
echo ""
echo "📚 Available endpoints:"
echo "   - FastAPI App: http://localhost:12000"
echo "   - API Docs: http://localhost:12000/docs"
echo "   - Health Check: http://localhost:12000/health"
echo "   - Neo4j Browser: http://localhost:7474 (if using docker-compose)"
echo ""
echo "📈 Graph Data Science plugin is included and ready to use!"
echo "📖 See GRAPH_DATA_SCIENCE.md for usage examples."