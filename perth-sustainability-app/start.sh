#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   🌱 Sustainability Tracker Setup    ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo -e "${RED}✗ Docker is not installed${NC}"
    echo "Please install Docker Desktop: https://www.docker.com/products/docker-desktop/"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}✗ Docker Compose is not installed${NC}"
    echo "Please install Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo -e "${RED}✗ Docker is not running${NC}"
    echo "Please start Docker Desktop"
    exit 1
fi

echo -e "${GREEN}✓ Docker is installed and running${NC}"
echo ""

# Ask user what to do
echo "What would you like to do?"
echo "1) Start production environment (Port 80)"
echo "2) Start development environment (Port 3000)"
echo "3) Stop all services"
echo "4) View logs"
echo "5) Clean up everything"
echo ""
read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo ""
        echo -e "${BLUE}Starting production environment...${NC}"
        docker-compose build
        docker-compose up -d
        echo ""
        echo -e "${GREEN}✓ Services started successfully!${NC}"
        echo ""
        echo -e "${YELLOW}Access your application:${NC}"
        echo -e "  Frontend: ${GREEN}http://localhost${NC}"
        echo -e "  Backend:  ${GREEN}http://localhost:3001${NC}"
        echo -e "  Health:   ${GREEN}http://localhost:3001/health${NC}"
        echo ""
        echo -e "View logs: ${BLUE}docker-compose logs -f${NC}"
        echo -e "Stop:      ${BLUE}docker-compose down${NC}"
        ;;
    2)
        echo ""
        echo -e "${BLUE}Starting development environment...${NC}"
        docker-compose -f docker-compose.dev.yml build
        docker-compose -f docker-compose.dev.yml up -d
        echo ""
        echo -e "${GREEN}✓ Development services started!${NC}"
        echo ""
        echo -e "${YELLOW}Access your application:${NC}"
        echo -e "  Frontend: ${GREEN}http://localhost:3000${NC}"
        echo -e "  Backend:  ${GREEN}http://localhost:3001${NC}"
        echo ""
        echo -e "${YELLOW}Hot reload enabled - edit files and see changes instantly!${NC}"
        echo ""
        echo -e "View logs: ${BLUE}docker-compose -f docker-compose.dev.yml logs -f${NC}"
        echo -e "Stop:      ${BLUE}docker-compose -f docker-compose.dev.yml down${NC}"
        ;;
    3)
        echo ""
        echo -e "${BLUE}Stopping all services...${NC}"
        docker-compose down
        docker-compose -f docker-compose.dev.yml down
        echo -e "${GREEN}✓ All services stopped${NC}"
        ;;
    4)
        echo ""
        echo -e "${BLUE}Showing logs (Ctrl+C to exit)...${NC}"
        echo ""
        if docker-compose ps | grep -q "Up"; then
            docker-compose logs -f
        elif docker-compose -f docker-compose.dev.yml ps | grep -q "Up"; then
            docker-compose -f docker-compose.dev.yml logs -f
        else
            echo -e "${YELLOW}No services are currently running${NC}"
        fi
        ;;
    5)
        echo ""
        echo -e "${RED}⚠️  This will remove all containers, volumes, and images!${NC}"
        read -p "Are you sure? (yes/no): " confirm
        if [ "$confirm" = "yes" ]; then
            echo ""
            echo -e "${BLUE}Cleaning up...${NC}"
            docker-compose down -v
            docker-compose -f docker-compose.dev.yml down -v
            docker system prune -f
            echo -e "${GREEN}✓ Cleanup complete${NC}"
        else
            echo "Cancelled"
        fi
        ;;
    *)
        echo -e "${RED}Invalid choice${NC}"
        exit 1
        ;;
esac

echo ""