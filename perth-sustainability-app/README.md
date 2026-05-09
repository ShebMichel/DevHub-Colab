# 🚀 Quick Start - Development Mode

Get the Sustainability Tracker running in Docker with hot reload in under 5 minutes!

---

## ✅ Prerequisites

1. **Install Docker Desktop**

   - Mac: https://docs.docker.com/desktop/install/mac-install/
   - Windows: https://docs.docker.com/desktop/install/windows-install/
   - Linux: https://docs.docker.com/desktop/install/linux-install/

2. **Start Docker Desktop**

   - Open the Docker Desktop app
   - Wait for it to fully start (whale icon in taskbar/menu bar)

3. **Verify Docker is running**
   ```bash
   docker --version
   docker-compose --version
   ```

---

## 🎯 Run the Project (3 Steps)

### Step 1: Clone/Download the Project

```bash
cd sustainability-app
```

### Step 2: Start Development Environment Using Docker Compose directly

```bash
docker-compose -f docker-compose.dev.yml up -d
```

### Step 3: Open Your Browser

Go to: **http://localhost:3000**

🎉 **You're done!**

---

## 📋 What Just Happened?

Docker started 3 containers:

1. **PostgreSQL** (database) on port 5432
2. **Backend** (Node.js API) on port 3001
3. **Frontend** (React app) on port 3000

All with **hot reload** enabled - edit code and see changes instantly!

---

## 🛠️ Common Commands

### Start the project

```bash
docker-compose -f docker-compose.dev.yml up -d
```

### Stop the project

```bash
docker-compose -f docker-compose.dev.yml down
```

### View logs

```bash
docker-compose -f docker-compose.dev.yml logs -f
```

---

## 🔍 Check If It's Working

### 1. Check containers are running

```bash
docker-compose -f docker-compose.dev.yml ps
```

You should see 3 containers with status "Up":

- `sustainability-postgres-dev`
- `sustainability-backend-dev`
- `sustainability-frontend-dev`

### 2. Test the backend

```bash
curl http://localhost:3001/health
```

Should return: `{"status":"ok","timestamp":"..."}`

### 3. Open frontend

Open browser: http://localhost:3000

You should see the Sustainability Tracker homepage!

---

## 💻 Making Changes (Hot Reload)

### Edit Backend Code

```bash
# Edit any file in backend/src/
code backend/src/index.ts

# Save the file
# Server automatically restarts
```

### Edit Frontend Code

```bash
# Edit any file in frontend/src/
code frontend/src/App.tsx

# Save the file
# Browser automatically reloads
# See changes immediately!
```

---

## 🗃️ Access the Database

### Using command line

```bash
docker-compose -f docker-compose.dev.yml exec postgres psql -U postgres -d sustainability
```

Inside PostgreSQL:

```sql
-- List all tables
\dt

-- View households
SELECT * FROM households;

-- View usage entries
SELECT * FROM usage_entries;

-- Exit
\q
```

### Using a GUI tool (pgAdmin, DBeaver, etc.)

- **Host:** localhost
- **Port:** 5432
- **Database:** sustainability
- **Username:** postgres
- **Password:** postgres

---

## 🐛 Troubleshooting

### Problem: Containers won't start

**Check if Docker is running:**

```bash
docker info
```

**Check if ports are available:**

```bash
# Check if ports 3000, 3001, or 5432 are in use
lsof -i :3000
lsof -i :3001
lsof -i :5432
```

**Solution:**

```bash
# Stop any conflicting services
# Or change ports in docker-compose.dev.yml
```

---

### Problem: Can't access http://localhost:3000

**Check frontend logs:**

```bash
docker-compose -f docker-compose.dev.yml logs frontend
```

**Restart frontend:**

```bash
docker-compose -f docker-compose.dev.yml restart frontend
```

---

### Problem: Backend not connecting to database

**Check PostgreSQL logs:**

```bash
docker-compose -f docker-compose.dev.yml logs postgres
```

**Wait for database to be ready:**

```bash
# Database takes ~10-20 seconds to start
# Backend will retry automatically
```

---

### Problem: Changes not showing up

**Backend changes:**

```bash
# Check if nodemon is running
docker-compose -f docker-compose.dev.yml logs backend | grep nodemon

# Restart backend
docker-compose -f docker-compose.dev.yml restart backend
```

**Frontend changes:**

```bash
# Hard refresh browser
# Windows/Linux: Ctrl + Shift + R
# Mac: Cmd + Shift + R

# Or restart frontend
docker-compose -f docker-compose.dev.yml restart frontend
```

---

### Problem: "Port already in use"

**Find what's using the port:**

```bash
lsof -i :3000  # Frontend
lsof -i :3001  # Backend
lsof -i :5432  # Database
```

**Kill the process or change ports:**

```bash
# Kill process
kill -9 <PID>

# OR change port in docker-compose.dev.yml
ports:
  - "3002:3000"  # Use port 3002 instead
```

---

### Problem: Everything is broken, start fresh

**Nuclear option (removes all data):**

```bash
# Stop everything
docker-compose -f docker-compose.dev.yml down -v

# Remove all containers
docker container prune -f

```

---

## 📊 Useful Commands

### View all containers

```bash
docker ps
```

### View all logs

```bash
docker-compose -f docker-compose.dev.yml logs -f
```

### View specific service logs

```bash
docker-compose -f docker-compose.dev.yml logs -f backend
docker-compose -f docker-compose.dev.yml logs -f frontend
docker-compose -f docker-compose.dev.yml logs -f postgres
```

### Restart a specific service

```bash
docker-compose -f docker-compose.dev.yml restart backend
docker-compose -f docker-compose.dev.yml restart frontend
```

### Stop everything

```bash
docker-compose -f docker-compose.dev.yml down
```

### Stop and remove all data

```bash
docker-compose -f doc
```
