#!/bin/bash

# TradieMate Marketing Analytics Full Stack Setup
# This script sets up the complete platform with frontend and backend

set -e

echo "🚀 Setting up TradieMate Marketing Analytics Platform..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    print_error "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create environment file if it doesn't exist
if [ ! -f .env ]; then
    print_status "Creating environment configuration..."
    cat > .env << EOF
# TradieMate Marketing Analytics Configuration
OPENAI_API_KEY=your_openai_api_key_here
CREWAI_BACKEND_URL=http://localhost:12000
CREWAI_API_KEY=

# Neo4j Configuration
NEO4J_URI=neo4j://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=tradiemate123

# Application Settings
ENVIRONMENT=development
LOG_LEVEL=INFO
PORT=12000
HOST=0.0.0.0

# Frontend Configuration
NEXT_PUBLIC_APP_NAME=TradieMate Marketing Analytics
NEXT_PUBLIC_APP_DESCRIPTION=AI-powered Google Ads and website optimization for trade businesses

# Supabase Configuration (for frontend data storage)
NEXT_PUBLIC_SUPABASE_URL=http://localhost:54321
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImV4cCI6MTk4MzgxMjk5Nn0.EGIM96RAZx35lJzdJsyH-qQwv8Hdp7fsn3W0YpN81IU
EOF
    print_warning "Created .env file. Please update OPENAI_API_KEY with your actual API key."
fi

# Create frontend environment file
if [ ! -f frontend/.env.local ]; then
    print_status "Creating frontend environment configuration..."
    cp frontend/.env.local.example frontend/.env.local
    print_warning "Created frontend/.env.local file. Please update with your configuration."
fi

# Build and start the services
print_status "Building and starting services..."
docker-compose -f docker-compose.full-stack.yml up --build -d

# Wait for services to be healthy
print_status "Waiting for services to start..."
sleep 30

# Check service health
print_status "Checking service health..."

# Check Neo4j
if curl -f http://localhost:7474 > /dev/null 2>&1; then
    print_success "Neo4j is running at http://localhost:7474"
else
    print_warning "Neo4j may still be starting up..."
fi

# Check Backend
if curl -f http://localhost:12000/health > /dev/null 2>&1; then
    print_success "Backend API is running at http://localhost:12000"
else
    print_warning "Backend API may still be starting up..."
fi

# Check Frontend
if curl -f http://localhost:12001/api/health > /dev/null 2>&1; then
    print_success "Frontend is running at http://localhost:12001"
else
    print_warning "Frontend may still be starting up..."
fi

echo ""
print_success "🎉 TradieMate Marketing Analytics Platform Setup Complete!"
echo ""
echo "📊 Access your services:"
echo "   • Frontend (Chat Interface): http://localhost:12001"
echo "   • Backend API: http://localhost:12000"
echo "   • Neo4j Browser: http://localhost:7474"
echo "   • Supabase Dashboard: http://localhost:54323"
echo ""
echo "🔑 Default Credentials:"
echo "   • Neo4j: neo4j / tradiemate123"
echo "   • Supabase: Check the Supabase documentation"
echo ""
echo "📝 Next Steps:"
echo "   1. Update your OpenAI API key in .env file"
echo "   2. Access the chat interface at http://localhost:12001"
echo "   3. Start chatting with your marketing analytics agents!"
echo ""
echo "🛠️  Useful Commands:"
echo "   • View logs: docker-compose -f docker-compose.full-stack.yml logs -f"
echo "   • Stop services: docker-compose -f docker-compose.full-stack.yml down"
echo "   • Restart services: docker-compose -f docker-compose.full-stack.yml restart"
echo ""