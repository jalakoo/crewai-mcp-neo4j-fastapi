# Deployment Guide

## Application Status: ✅ READY FOR LAUNCH

The CrewAI Neo4j FastAPI application has been successfully configured and is ready for production deployment.

## Current Configuration

### Environment Variables
All required environment variables are properly configured in `.env`:

- ✅ `OPENAI_API_KEY` - OpenAI API key for LLM inference
- ✅ `NEO4J_URI` - Neo4j database connection URI
- ✅ `NEO4J_USERNAME` - Neo4j database username
- ✅ `NEO4J_PASSWORD` - Neo4j database password
- ✅ `PORT` - Server port (set to 12000 for runtime environment)

### Dependencies
- ✅ All Python dependencies installed via Poetry
- ✅ Python version compatibility fixed (>=3.11,<3.13)
- ✅ FastAPI with CORS middleware enabled
- ✅ CrewAI and MCP tools properly configured

### Server Configuration
- ✅ FastAPI server configured to listen on 0.0.0.0:12000
- ✅ CORS enabled for cross-origin requests
- ✅ Health check endpoint available at `/health`
- ✅ Interactive API documentation at `/docs`
- ✅ Root endpoint with service information at `/`

## Access URLs

### Primary Application URL
- **External URL**: https://work-1-goqklxbklssuggrt.prod-runtime.all-hands.dev
- **Local URL**: http://localhost:12000

### Available Endpoints
- **Root**: `/` - Service information and status
- **Health Check**: `/health` - Application health status
- **API Documentation**: `/docs` - Interactive Swagger UI
- **Query Endpoint**: `/crewai` - Main CrewAI query processing endpoint

## Quick Start

### Option 1: Using the startup script
```bash
./start.sh
```

### Option 2: Manual startup
```bash
# Load environment variables
source .env

# Start the server
poetry run python main.py
```

### Option 3: Using Poetry directly
```bash
poetry run uvicorn main:app --host 0.0.0.0 --port 12000 --reload
```

## Testing the Application

### 1. Health Check
```bash
curl https://work-1-goqklxbklssuggrt.prod-runtime.all-hands.dev/health
```
Expected response:
```json
{"status":"healthy","service":"crewai-neo4j-fastapi"}
```

### 2. Service Information
```bash
curl https://work-1-goqklxbklssuggrt.prod-runtime.all-hands.dev/
```

### 3. API Documentation
Visit: https://work-1-goqklxbklssuggrt.prod-runtime.all-hands.dev/docs

### 4. Test Query (Example)
```bash
curl -X POST "https://work-1-goqklxbklssuggrt.prod-runtime.all-hands.dev/crewai" \
     -H "Content-Type: application/json" \
     -d '{"query": "What data is available in the Neo4j database?"}'
```

## Architecture

### Components
1. **FastAPI Server** - Web API framework with automatic documentation
2. **CrewAI** - AI agent framework for processing queries
3. **Neo4j MCP** - Model Context Protocol for Neo4j database interaction
4. **OpenAI Integration** - LLM for natural language processing

### Data Flow
1. Client sends query to `/crewai` endpoint
2. FastAPI receives and validates the request
3. CrewAI agent processes the query using Neo4j MCP tools
4. MCP tools interact with Neo4j database
5. Results are processed and returned to client

## Security Considerations

- ✅ Environment variables properly isolated in `.env` file
- ✅ CORS configured for cross-origin access
- ✅ API key authentication handled by OpenAI SDK
- ✅ Neo4j connection secured with credentials

## Monitoring

### Health Monitoring
- Use `/health` endpoint for application health checks
- Monitor server logs for errors and performance metrics
- Check Neo4j database connectivity

### Performance Monitoring
- Monitor response times for `/crewai` endpoint
- Track OpenAI API usage and costs
- Monitor Neo4j database performance

## Troubleshooting

### Common Issues

1. **Server won't start**
   - Check `.env` file exists and contains all required variables
   - Verify Poetry dependencies are installed: `poetry install --no-root`
   - Check port 12000 is available

2. **Environment variable errors**
   - Ensure `.env` file is properly formatted
   - Verify all required variables are set
   - Check for trailing spaces or special characters

3. **Neo4j connection issues**
   - Verify Neo4j database is running and accessible
   - Check NEO4J_URI, NEO4J_USERNAME, and NEO4J_PASSWORD
   - Test database connectivity independently

4. **OpenAI API errors**
   - Verify OPENAI_API_KEY is valid and has sufficient credits
   - Check API rate limits and usage

### Logs
Server logs are available in `server.log` when running in background mode.

## Production Deployment Notes

1. **Environment Variables**: Ensure production environment variables are properly set
2. **Database**: Verify Neo4j database is production-ready with proper backups
3. **API Keys**: Use production OpenAI API keys with appropriate rate limits
4. **Monitoring**: Set up proper logging and monitoring for production use
5. **Security**: Consider additional security measures for production deployment

## Status: ✅ READY FOR LAUNCH

The application is fully configured and tested. All components are working correctly:
- ✅ Server running on correct port (12000)
- ✅ External access confirmed
- ✅ All endpoints responding correctly
- ✅ Environment variables properly loaded
- ✅ Dependencies installed and working
- ✅ CORS and security configured
- ✅ Documentation accessible

The application is ready for production use.