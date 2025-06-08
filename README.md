# CrewAI Neo4j FastAPI Server

A production-ready FastAPI server that uses CrewAI and Neo4j MCP (Model Context Protocol) to process natural language queries about data within a Neo4j graph database.

## Features

- 🤖 **CrewAI Integration**: Intelligent AI agents for data analysis
- 🗄️ **Neo4j MCP Support**: Direct integration with Neo4j via Model Context Protocol
- 🚀 **FastAPI**: Modern, fast web framework with automatic API documentation
- 🐳 **Docker Support**: Complete containerization with Docker Compose
- 🔧 **Environment Configuration**: Flexible configuration via environment variables
- 🌐 **CORS Support**: Ready for web application integration
- 📊 **Health Checks**: Built-in health monitoring endpoints

## Requirements

- [Poetry](https://python-poetry.org) for dependency management
- [OpenAI API Key](https://platform.openai.com/api-keys) for LLM inference
- Running [Neo4j](https://neo4j.com) database (local or cloud)
- Python 3.11.11

## Quick Start

### Option 1: Automated Setup

```bash
# Clone and setup
git clone https://github.com/TradieMate/crewai-mcp-neo4j-fastapi.git
cd crewai-mcp-neo4j-fastapi
./setup.sh
```

### Option 2: Manual Setup

1. **Install dependencies:**
   ```bash
   poetry install
   ```

2. **Configure environment:**
   ```bash
   cp sample.env .env
   # Edit .env with your actual values
   ```

3. **Start the server:**
   ```bash
   poetry run uvicorn main:app --host 0.0.0.0 --port 12000 --reload
   ```

### Option 3: Docker Compose (Recommended)

```bash
# Start both the API server and Neo4j database
docker-compose up
```

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```bash
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Neo4j Database Configuration
NEO4J_URI=neo4j://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_neo4j_password_here

# Server Configuration
PORT=12000
HOST=0.0.0.0

# Environment
ENVIRONMENT=development

# CORS Configuration (for web access)
ALLOWED_ORIGINS=*
```

### Neo4j Setup

#### Local Neo4j
```bash
# Using Docker
docker run \
    --name neo4j \
    -p7474:7474 -p7687:7687 \
    -d \
    -v $HOME/neo4j/data:/data \
    -v $HOME/neo4j/logs:/logs \
    -v $HOME/neo4j/import:/var/lib/neo4j/import \
    -v $HOME/neo4j/plugins:/plugins \
    --env NEO4J_AUTH=neo4j/password \
    neo4j:latest
```

#### Neo4j Aura (Cloud)
1. Create a free account at [Neo4j Aura](https://neo4j.com/cloud/aura/)
2. Create a new database instance
3. Use the provided connection details in your `.env` file

## API Endpoints

### Base URL
- **Local**: `http://localhost:12000`
- **Production**: Your deployed URL

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint with basic information |
| GET | `/health` | Health check endpoint |
| POST | `/crewai` | Process natural language queries |
| GET | `/docs` | Interactive API documentation |

### Example Usage

#### Query the Database
```bash
curl -X POST "http://localhost:12000/crewai" \
     -H "Content-Type: application/json" \
     -d '{"query": "What are the most connected nodes in the graph?"}'
```

#### Health Check
```bash
curl http://localhost:12000/health
```

## Development

### Running Tests
```bash
poetry run pytest
```

### Code Formatting
```bash
poetry run black .
poetry run isort .
```

### Type Checking
```bash
poetry run mypy .
```

## Deployment

### Docker Production Build
```bash
docker build -t crewai-neo4j-api .
docker run -p 12000:12000 --env-file .env crewai-neo4j-api
```

### Cloud Deployment
The application is ready for deployment on:
- AWS ECS/Fargate
- Google Cloud Run
- Azure Container Instances
- Heroku
- Railway
- Render

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   FastAPI       │    │   CrewAI        │    │   Neo4j MCP     │
│   Web Server    │───▶│   AI Agents     │───▶│   Tools         │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                                                       ▼
                                              ┌─────────────────┐
                                              │   Neo4j         │
                                              │   Database      │
                                              └─────────────────┘
```

## Troubleshooting

### Common Issues

1. **MCP Neo4j Tool Not Found**
   ```bash
   # Install uvx and the MCP tool
   poetry run pip install uv
   uvx install mcp-neo4j-cypher
   ```

2. **Neo4j Connection Issues**
   - Verify Neo4j is running: `docker ps` or check Neo4j Desktop
   - Check connection details in `.env` file
   - Ensure firewall allows connections on port 7687

3. **OpenAI API Issues**
   - Verify API key is correct and has credits
   - Check API key permissions

### Logs
```bash
# View application logs
docker-compose logs app

# View Neo4j logs
docker-compose logs neo4j
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- Create an issue on GitHub
- Check the [CrewAI documentation](https://docs.crewai.com/)
- Review [Neo4j MCP documentation](https://github.com/neo4j/mcp-neo4j)
