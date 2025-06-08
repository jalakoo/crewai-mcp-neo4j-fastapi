# 🚀 TradieMate Marketing Analytics - Unified Platform Guide

## Overview

The TradieMate Marketing Analytics platform combines a powerful CrewAI backend with a modern chat interface to provide AI-powered Google Ads and website optimization for trade businesses. This unified platform allows you to chat with specialized marketing agents through an intuitive web interface.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    TradieMate Platform                      │
├─────────────────────────────────────────────────────────────┤
│  Frontend (Next.js)          │  Backend (FastAPI + CrewAI) │
│  ├─ Chat Interface           │  ├─ Marketing Agents        │
│  ├─ TradieMate Branding      │  ├─ Google Ads Analyst      │
│  ├─ Real-time Messaging      │  ├─ Website Optimizer       │
│  └─ Supabase Integration     │  └─ Neo4j Graph Database    │
├─────────────────────────────────────────────────────────────┤
│                    Shared Services                          │
│  ├─ Neo4j Graph Database (Marketing Data)                  │
│  ├─ Supabase (User Data & Chat History)                    │
│  └─ Docker Orchestration                                   │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- OpenAI API Key
- 8GB+ RAM recommended
- Ports 3000, 7474, 7687, 12000, 12001, 54321-54323 available

### 1. One-Command Setup

```bash
# Clone and setup the platform
git clone https://github.com/TradieMate/crewai-mcp-neo4j-fastapi.git
cd crewai-mcp-neo4j-fastapi
./setup-full-stack.sh
```

### 2. Manual Setup

```bash
# 1. Create environment configuration
cp .env.example .env
cp frontend/.env.local.example frontend/.env.local

# 2. Update your OpenAI API key in .env
# OPENAI_API_KEY=your_actual_api_key_here

# 3. Start all services
docker-compose -f docker-compose.full-stack.yml up --build -d

# 4. Wait for services to start (30-60 seconds)
docker-compose -f docker-compose.full-stack.yml logs -f
```

## 🌐 Service Access

| Service | URL | Purpose |
|---------|-----|---------|
| **Chat Interface** | http://localhost:12001 | Main user interface for chatting with agents |
| **Backend API** | http://localhost:12000 | CrewAI FastAPI backend |
| **Neo4j Browser** | http://localhost:7474 | Graph database management |
| **Supabase Dashboard** | http://localhost:54323 | User data and chat history |

## 💬 Using the Chat Interface

### 1. Access the Platform
Navigate to http://localhost:12001 in your browser.

### 2. Select a Marketing Agent
Choose from specialized agents:
- **TradieMate Marketing Analytics**: General marketing analysis
- **Google Ads Campaign Analyst**: Google Ads optimization
- **Website Optimization Specialist**: Website performance analysis

### 3. Start Chatting
Ask questions like:
- "Analyze my Google Ads performance for plumbing services"
- "How can I improve my electrician website's conversion rate?"
- "What keywords should I target for HVAC services?"
- "Create a marketing strategy for my roofing business"

### 4. Get Detailed Reports
The agents provide:
- 📊 Performance metrics and analytics
- 💡 Actionable insights and recommendations
- 🎯 Specific optimization strategies
- 📈 ROI improvement suggestions

## 🔧 Configuration

### Environment Variables

#### Backend Configuration (.env)
```bash
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Database
NEO4J_URI=neo4j://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=tradiemate123

# API Settings
PORT=12000
HOST=0.0.0.0
ENVIRONMENT=production
LOG_LEVEL=INFO
```

#### Frontend Configuration (frontend/.env.local)
```bash
# Backend Connection
CREWAI_BACKEND_URL=http://localhost:12000

# Supabase (for user data)
NEXT_PUBLIC_SUPABASE_URL=http://localhost:54321
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key

# Branding
NEXT_PUBLIC_APP_NAME=TradieMate Marketing Analytics
NEXT_PUBLIC_APP_DESCRIPTION=AI-powered Google Ads and website optimization for trade businesses
```

## 🛠️ Development

### Local Development Setup

```bash
# Backend development
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 12000

# Frontend development
cd frontend
npm install
npm run dev
```

### Adding New Agents

1. **Create Agent in Backend** (`agents/`)
```python
# agents/new_agent.py
from crewai import Agent

new_agent = Agent(
    role="Specialized Role",
    goal="Specific goal for trade businesses",
    backstory="Agent background and expertise",
    tools=[relevant_tools]
)
```

2. **Add to Frontend Model List** (`frontend/lib/models/llm/crewai-llm-list.ts`)
```typescript
{
  modelId: "new-agent",
  modelName: "New Specialized Agent",
  provider: "crewai",
  // ... configuration
}
```

3. **Update API Route** (`frontend/app/api/chat/crewai/route.ts`)
Add handling for the new agent type.

## 📊 Data Flow

```
User Input → Frontend Chat → CrewAI API Route → FastAPI Backend → 
CrewAI Agents → Tools & Neo4j → Formatted Response → Frontend Display
```

### Chat Message Processing

1. **User sends message** in chat interface
2. **Frontend** captures message and sends to `/api/chat/crewai`
3. **API route** forwards to FastAPI backend at `/crewai`
4. **CrewAI agents** process the query using specialized tools
5. **Neo4j database** provides marketing data and insights
6. **Formatted response** returns through the chain
7. **Chat interface** displays rich markdown response

## 🔒 Security Features

- **API Key Management**: Secure environment variable handling
- **Rate Limiting**: Built-in request throttling
- **Input Validation**: Sanitized user inputs
- **CORS Protection**: Configured cross-origin policies
- **Health Monitoring**: Comprehensive health checks

## 📈 Monitoring & Logging

### Health Checks
```bash
# Check all services
curl http://localhost:12001/api/health  # Frontend
curl http://localhost:12000/health      # Backend
curl http://localhost:7474              # Neo4j
```

### Logs
```bash
# View all logs
docker-compose -f docker-compose.full-stack.yml logs -f

# View specific service logs
docker-compose -f docker-compose.full-stack.yml logs -f frontend
docker-compose -f docker-compose.full-stack.yml logs -f backend
docker-compose -f docker-compose.full-stack.yml logs -f neo4j
```

## 🚀 Production Deployment

### Cloud Deployment Options

#### 1. Docker Swarm
```bash
docker swarm init
docker stack deploy -c docker-compose.full-stack.yml tradie-platform
```

#### 2. Kubernetes
Use the provided Kubernetes manifests in `/k8s/` directory.

#### 3. Cloud Platforms
- **AWS**: ECS with Application Load Balancer
- **Google Cloud**: Cloud Run with Cloud SQL
- **Azure**: Container Instances with Azure Database

### Environment-Specific Configuration

#### Production Environment Variables
```bash
# Security
ENVIRONMENT=production
ALLOWED_ORIGINS=https://yourdomain.com
API_RATE_LIMIT=100

# Database
NEO4J_URI=neo4j+s://your-cloud-neo4j.com:7687
SUPABASE_URL=https://your-project.supabase.co

# Monitoring
LOG_LEVEL=INFO
SENTRY_DSN=your_sentry_dsn
```

## 🔧 Troubleshooting

### Common Issues

#### 1. Services Not Starting
```bash
# Check Docker resources
docker system df
docker system prune

# Restart services
docker-compose -f docker-compose.full-stack.yml restart
```

#### 2. Frontend Can't Connect to Backend
- Verify `CREWAI_BACKEND_URL` in frontend environment
- Check backend health: `curl http://localhost:12000/health`
- Review Docker network connectivity

#### 3. Neo4j Connection Issues
- Verify Neo4j credentials in `.env`
- Check Neo4j logs: `docker-compose logs neo4j`
- Ensure Neo4j is fully started before backend

#### 4. Chat Interface Not Responding
- Check browser console for JavaScript errors
- Verify Supabase configuration
- Test API route directly: `curl -X POST http://localhost:12001/api/chat/crewai`

### Performance Optimization

#### 1. Resource Allocation
```yaml
# docker-compose.full-stack.yml
services:
  backend:
    deploy:
      resources:
        limits:
          memory: 2G
          cpus: '1.0'
```

#### 2. Caching
- Enable Redis for session caching
- Configure CDN for static assets
- Implement API response caching

## 📚 API Documentation

### CrewAI Backend Endpoints

#### POST /crewai
Process marketing analytics queries.

**Request:**
```json
{
  "query": "Analyze my Google Ads performance",
  "agent_type": "google-ads-analyst" // optional
}
```

**Response:**
```json
{
  "status": "success",
  "result": "Detailed analysis...",
  "insights": ["insight1", "insight2"],
  "recommendations": ["rec1", "rec2"],
  "metrics": {"ctr": "3.2%", "cpc": "$1.45"},
  "agent_used": "Google Ads Campaign Analyst"
}
```

### Frontend API Routes

#### GET /api/health
Frontend health check with backend connectivity.

#### POST /api/chat/crewai
Chat interface to CrewAI backend integration.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Development Guidelines

- Follow TypeScript/Python best practices
- Add comprehensive error handling
- Include unit tests for new features
- Update documentation for changes
- Maintain backward compatibility

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 🆘 Support

- **Documentation**: This guide and inline code comments
- **Issues**: GitHub Issues for bug reports
- **Discussions**: GitHub Discussions for questions
- **Email**: support@tradiemate.com

---

**Built with ❤️ for the trade industry by TradieMate**