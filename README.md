# 🚀 TradieMate Marketing Analytics - Unified Platform

A complete AI-powered marketing analytics platform that combines a modern chat interface with specialized CrewAI agents to provide Google Ads optimization and website performance analysis for trade businesses.

## ✨ Platform Overview

This unified platform includes:
- **🎨 Modern Chat Interface**: Intuitive web UI for interacting with marketing agents
- **🤖 Specialized AI Agents**: CrewAI-powered agents for Google Ads and website optimization  
- **📊 Real-time Analytics**: Live marketing performance insights and recommendations
- **🗄️ Graph Database**: Neo4j for complex marketing data relationships
- **🔒 Production Ready**: Enterprise-grade security, monitoring, and deployment

## 🏗️ Architecture

```
Frontend (Next.js)     Backend (FastAPI + CrewAI)     Database (Neo4j)
├─ Chat Interface  →   ├─ Marketing Agents        →   ├─ Campaign Data
├─ TradieMate UI       ├─ Google Ads Analyst          ├─ Customer Journey
├─ Real-time Chat      ├─ Website Optimizer           ├─ Attribution Models
└─ Supabase Auth       └─ Performance Analytics       └─ Graph Analytics
```

## 🚀 Features

### Chat Interface
- 💬 **Conversational AI**: Natural language queries for marketing insights
- 🎨 **TradieMate Branding**: Custom branded interface for trade businesses
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- 🔄 **Real-time Updates**: Live chat with streaming responses
- 📚 **Chat History**: Persistent conversation storage with Supabase

### AI Marketing Agents
- 🎯 **Google Ads Analyst**: Campaign optimization and performance analysis
- 🌐 **Website Optimizer**: Landing page and conversion rate optimization
- 📊 **Marketing Analytics**: ROI, ROAS, CTR, and attribution analysis
- 🔍 **Keyword Research**: Trade-specific keyword recommendations
- 📈 **Performance Tracking**: Campaign and website performance monitoring

### Technical Features
- 🚀 **FastAPI Backend**: Modern, fast API with automatic documentation
- 🗄️ **Neo4j Integration**: Graph database for complex marketing relationships
- 🐳 **Docker Orchestration**: Complete containerized deployment
- 🔒 **Production Security**: Rate limiting, input validation, API authentication
- 📊 **Monitoring**: Health checks, logging, and performance metrics

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))
- 8GB+ RAM recommended
- Ports 3000, 7474, 7687, 12000, 12001, 54321-54323 available

### One-Command Setup

```bash
# Clone the repository
git clone --recursive https://github.com/TradieMate/crewai-mcp-neo4j-fastapi.git
cd crewai-mcp-neo4j-fastapi

# Run the automated setup
./setup-full-stack.sh
```

This will:
1. ✅ Set up all environment configurations
2. 🐳 Build and start all Docker services
3. 🗄️ Initialize Neo4j with sample data
4. 🎨 Launch the chat interface
5. 🤖 Start the CrewAI backend

### Access Your Platform

After setup completes (2-3 minutes):

| Service | URL | Purpose |
|---------|-----|---------|
| **🎨 Chat Interface** | http://localhost:12001 | Main user interface |
| **🔧 Backend API** | http://localhost:12000 | CrewAI FastAPI backend |
| **🗄️ Neo4j Browser** | http://localhost:7474 | Database management |
| **📊 API Docs** | http://localhost:12000/docs | Interactive API documentation |

### First Steps

1. **Open the chat interface**: http://localhost:12001
2. **Select a marketing agent** from the dropdown
3. **Start chatting**: Ask questions like:
   - "Analyze my Google Ads performance for plumbing services"
   - "How can I improve my electrician website's conversion rate?"
   - "What keywords should I target for HVAC services?"

## 🛠️ Development Setup

### Backend Development
```bash
# Install dependencies
poetry install

# Start backend only
poetry run uvicorn main:app --host 0.0.0.0 --port 12000 --reload
```

### Frontend Development
```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### Manual Docker Setup
```bash
# Start all services
docker-compose -f docker-compose.full-stack.yml up --build -d

# View logs
docker-compose -f docker-compose.full-stack.yml logs -f

# Stop services
docker-compose -f docker-compose.full-stack.yml down
```

## 📚 Documentation

- **[🚀 Unified Platform Guide](UNIFIED_PLATFORM_GUIDE.md)**: Complete setup and usage guide
- **[📋 Production Requirements](PRODUCTION_REQUIREMENTS.md)**: Environment variables and deployment requirements
- **[🔒 Production Deployment](PRODUCTION_DEPLOYMENT.md)**: Enterprise deployment guide
- **[🐳 Docker Setup](DOCKER_UNIFIED.md)**: Docker configuration and optimization

## 💬 Example Chat Interactions

### Google Ads Analysis
```
User: "Analyze my Google Ads performance for my plumbing business"

Agent: 📊 Marketing Analytics Report

Based on your plumbing business Google Ads data:

## 💡 Key Insights
1. Your "emergency plumber" keywords have 40% higher CTR than industry average
2. Mobile traffic converts 25% better than desktop for urgent services
3. Local service ads outperform search ads by 60% for immediate bookings

## 🎯 Recommendations
1. Increase budget allocation to emergency plumbing keywords
2. Optimize mobile landing pages for faster booking
3. Expand local service ads coverage to neighboring areas
4. Add negative keywords to reduce irrelevant clicks

## 📈 Performance Metrics
- **CTR**: 3.2% (Industry avg: 2.1%)
- **CPC**: $4.50 (Competitive for plumbing)
- **Conversion Rate**: 8.5% (Above average)
- **ROAS**: 420% (Excellent performance)
```

### Website Optimization
```
User: "How can I improve my electrician website's conversion rate?"

Agent: 🌐 Website Optimization Analysis

## 💡 Key Issues Identified
1. Contact form is below the fold on mobile devices
2. No clear pricing information visible
3. Missing customer testimonials and reviews
4. Slow page load time (4.2 seconds)

## 🎯 Optimization Recommendations
1. Move contact form above the fold with prominent CTA
2. Add transparent pricing ranges for common services
3. Display customer reviews prominently on homepage
4. Optimize images and implement lazy loading
5. Add click-to-call buttons for mobile users

## 📈 Expected Impact
- **Conversion Rate**: +35% improvement expected
- **Page Load Time**: Reduce to <2 seconds
- **Mobile Experience**: +50% better user engagement
- **Lead Quality**: Higher intent leads with pricing transparency
```

## 🔧 Configuration

### Required Environment Variables

```bash
# Core Configuration
OPENAI_API_KEY=your_openai_api_key_here
NEO4J_URI=neo4j://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=tradiemate123

# Frontend Configuration
CREWAI_BACKEND_URL=http://localhost:12000
NEXT_PUBLIC_APP_NAME=TradieMate Marketing Analytics
```

See [PRODUCTION_REQUIREMENTS.md](PRODUCTION_REQUIREMENTS.md) for complete configuration details.

## 🤖 AI Marketing Agents

The platform includes specialized AI agents for comprehensive marketing analysis:

### 🎯 Google Ads Campaign Analyst
- **Focus**: PPC campaign optimization, keyword analysis, ROAS improvement
- **Triggers**: Queries about ads, campaigns, keywords, bidding, CPC, ROAS
- **Expertise**: Budget allocation, audience targeting, conversion optimization

### 🌐 Website Optimization Specialist  
- **Focus**: Conversion rate optimization, user experience, lead generation
- **Triggers**: Queries about website, landing pages, traffic, conversions, SEO
- **Expertise**: Funnel analysis, page optimization, mobile performance

### 📊 Marketing Analytics Generalist
- **Focus**: Overall marketing strategy and cross-channel analysis
- **Triggers**: General marketing queries, strategy questions, ROI analysis
- **Expertise**: Attribution modeling, customer journey analysis, budget optimization

## 🔌 API Endpoints

### Base URLs
- **Frontend**: `http://localhost:12001`
- **Backend API**: `http://localhost:12000`
- **Neo4j Browser**: `http://localhost:7474`

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint with platform information |
| GET | `/health` | Comprehensive health check |
| POST | `/crewai` | Process marketing analytics queries |
| GET | `/docs` | Interactive API documentation |
| POST | `/api/chat/crewai` | Frontend chat interface endpoint |

### Example Marketing Queries

#### Google Ads Optimization
```bash
# Campaign performance analysis
curl -X POST "http://localhost:12000/crewai" \
     -H "Content-Type: application/json" \
     -d '{"query": "What are our top performing Google Ads campaigns and how can we optimize budget allocation?"}'

# Keyword analysis
curl -X POST "http://localhost:12000/crewai" \
     -H "Content-Type: application/json" \
     -d '{"query": "Which keywords are driving the most qualified leads for our plumbing services?"}'

# ROAS optimization
curl -X POST "http://localhost:12000/crewai" \
     -H "Content-Type: application/json" \
     -d '{"query": "How can we improve our electrical services ads ROAS in the Sydney market?"}'
```

#### Website Optimization
```bash
# Conversion analysis
curl -X POST "http://localhost:12000/crewai" \
     -H "Content-Type: application/json" \
     -d '{"query": "Why is our landing page conversion rate declining and how can we fix it?"}'

# Mobile optimization
curl -X POST "http://localhost:12000/crewai" \
     -H "Content-Type: application/json" \
     -d '{"query": "How can we improve quote request completions on mobile devices?"}'

# Traffic source analysis
curl -X POST "http://localhost:12000/crewai" \
     -H "Content-Type: application/json" \
     -d '{"query": "What traffic sources are bringing the highest quality leads?"}'
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

## 🚀 Production Deployment

### Cloud Deployment Options

#### Option 1: Vercel + Railway (Recommended)
```bash
# Frontend: Deploy to Vercel
# Backend: Deploy to Railway
# Databases: Use managed services (Neo4j Aura, Supabase)
```

#### Option 2: Docker Production
```bash
# Build production images
docker-compose -f docker-compose.full-stack.yml build

# Deploy with production configuration
ENVIRONMENT=production docker-compose -f docker-compose.full-stack.yml up -d
```

#### Option 3: Kubernetes
```bash
# Use provided Kubernetes manifests
kubectl apply -f k8s/
```

See [PRODUCTION_DEPLOYMENT.md](PRODUCTION_DEPLOYMENT.md) for detailed deployment guides.

## 🏗️ Platform Architecture

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

### Data Flow
```
User Chat → Frontend → API Route → FastAPI Backend → CrewAI Agents → 
Neo4j Tools → Graph Analytics → Formatted Response → Chat Interface
```

## 🛠️ Development

### Running Tests
```bash
# Backend tests
poetry run pytest

# Frontend tests
cd frontend && npm test
```

### Code Quality
```bash
# Backend formatting
poetry run black .
poetry run isort .
poetry run mypy .

# Frontend formatting
cd frontend && npm run lint:fix
```

## 🔧 Troubleshooting

### Common Issues

1. **Services Not Starting**
   ```bash
   # Check Docker resources
   docker system df
   docker system prune
   
   # Restart services
   docker-compose -f docker-compose.full-stack.yml restart
   ```

2. **Frontend Can't Connect to Backend**
   - Verify `CREWAI_BACKEND_URL` in frontend environment
   - Check backend health: `curl http://localhost:12000/health`

3. **Neo4j Connection Issues**
   - Verify Neo4j credentials in `.env`
   - Check Neo4j logs: `docker-compose logs neo4j`

### Logs
```bash
# View all logs
docker-compose -f docker-compose.full-stack.yml logs -f

# View specific service
docker-compose -f docker-compose.full-stack.yml logs -f frontend
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Guidelines
- Follow TypeScript/Python best practices
- Add comprehensive error handling
- Include unit tests for new features
- Update documentation for changes
- Maintain backward compatibility

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **📖 Documentation**: [Unified Platform Guide](UNIFIED_PLATFORM_GUIDE.md)
- **🐛 Bug Reports**: [GitHub Issues](https://github.com/TradieMate/crewai-mcp-neo4j-fastapi/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/TradieMate/crewai-mcp-neo4j-fastapi/discussions)
- **📧 Email**: support@tradiemate.com

## 🌟 Acknowledgments

- [CrewAI](https://docs.crewai.com/) for the AI agent framework
- [Neo4j](https://neo4j.com/) for the graph database and MCP tools
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [Next.js](https://nextjs.org/) for the frontend framework
- [Supabase](https://supabase.com/) for the user data backend

---

**Built with ❤️ for the trade industry by TradieMate**

*Empowering trade businesses with AI-powered marketing analytics*
