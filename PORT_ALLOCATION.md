# 🔌 Complete Port Allocation - 9-Pillar + Gurukul + EMS System

## Port Allocation Table

| Service | Port | Status | Required | URL |
|---------|------|--------|----------|-----|
| **Karma** | **8000** | ✅ Running | Yes | http://localhost:8000 |
| **Bucket** | **8001** | ✅ Running | Yes | http://localhost:8001 |
| **Core** | **8002** | ✅ Running | Yes | http://localhost:8002 |
| **Workflow** | **8003** | ✅ Running | Yes | http://localhost:8003 |
| **UAO** | **8004** | ✅ Running | Yes | http://localhost:8004 |
| **Insight Core** | **8005** | ✅ Running | Yes | http://localhost:8005 |
| **Insight Flow Bridge** | **8006** | ✅ Running | Optional | http://localhost:8006 |
| **Insight Flow Backend** | **8007** | ⚠️ Optional | No | http://localhost:8007 |
| **EMS Backend** | **8008** | ✅ Running | Yes | http://localhost:8008 |
| **Gurukul Backend** | **3000** | ✅ Running | Yes | http://localhost:3000 |
| **EMS Frontend** | **3001** | ✅ Running | Yes | http://localhost:3001 |
| **Gurukul Frontend** | **5173** | ✅ Running | Yes | http://localhost:5173 |

---

## Port Conflict Resolution

### ⚠️ CRITICAL: Port 8000 Conflict Resolved

**Issue**: Both Karma service and EMS Backend wanted port 8000

**Solution**: 
- ✅ **Karma keeps 8000** (core 9-pillar service, cannot change)
- ✅ **EMS moved to 8008** (application service, flexible)

**Files Updated**:
1. `gurukul-backend--main/START_COMMANDS.md` - EMS port changed to 8008
2. `gurukul-backend--main/backend/.env` - EMS_API_BASE_URL updated to http://localhost:8008

---

## Service Groups

### 9-Pillar Core Services (Ports 8000-8007)
```
8000 - Karma (Q-learning behavioral tracking)
8001 - Bucket (Constitutional governance + audit)
8002 - Core (AI Decision Engine)
8003 - Workflow (Deterministic execution)
8004 - UAO (Action orchestration)
8005 - Insight Core (JWT security)
8006 - Insight Flow Bridge (Intelligent routing)
8007 - Insight Flow Backend (Optional Q-learning)
```

### Application Services (Ports 3000-3001, 8008)
```
3000 - Gurukul Backend (Student learning platform)
3001 - EMS Frontend (Employee management UI)
5173 - Gurukul Frontend (Student learning UI)
8008 - EMS Backend (Employee management API)
```

---

## Startup Order

### Phase 1: Core 9-Pillar Services (Required)
```bash
# Terminal 1: Karma (8000)
cd "karma_chain_v2-main"
python main.py

# Terminal 2: Bucket (8001)
cd "BHIV_Central_Depository-main"
python main.py

# Terminal 3: Core (8002)
cd "v1-BHIV_CORE-main"
python mcp_bridge.py

# Terminal 4: Workflow (8003)
cd "workflow-executor-main"
python main.py

# Terminal 5: UAO (8004)
cd "Unified Action Orchestration"
python action_orchestrator.py

# Terminal 6: Insight Core (8005)
cd "insightcore-bridgev4x-main"
python insight_service.py

# Terminal 7: Insight Flow Bridge (8006) - Optional
cd "Insight_Flow-main"
start_bridge_standalone.bat
```

### Phase 2: Application Services
```bash
# Terminal 8: Gurukul Backend (3000)
cd "gurukul-backend--main/backend"
uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload

# Terminal 9: EMS Backend (8008)
cd "gurukul-backend--main/EMS System"
uvicorn app.main:app --host 0.0.0.0 --port 8008 --reload

# Terminal 10: Gurukul Frontend (5173)
cd "gurukul-backend--main/Frontend"
npm run dev

# Terminal 11: EMS Frontend (3001)
cd "gurukul-backend--main/EMS System/frontend"
npm run dev
```

---

## Health Check Commands

```bash
# 9-Pillar Services
curl http://localhost:8000/health  # Karma
curl http://localhost:8001/health  # Bucket
curl http://localhost:8002/health  # Core
curl http://localhost:8003/healthz # Workflow
curl http://localhost:8004/docs    # UAO
curl http://localhost:8005/health  # Insight Core
curl http://localhost:8006/health  # Insight Flow Bridge

# Application Services
curl http://localhost:3000/health  # Gurukul Backend
curl http://localhost:8008/health  # EMS Backend
curl http://localhost:5173         # Gurukul Frontend
curl http://localhost:3001         # EMS Frontend
```

---

## Integration URLs

### Gurukul Backend Integration (.env)
```env
# 9-Pillar Integration
CORE_URL=http://localhost:8002
BUCKET_URL=http://localhost:8001
KARMA_URL=http://localhost:8000
INSIGHT_CORE_URL=http://localhost:8005
INSIGHT_FLOW_URL=http://localhost:8006

# EMS Integration
EMS_API_BASE_URL=http://localhost:8008
```

---

## Port Availability Check

Before starting services, verify ports are free:

```bash
# Windows
netstat -ano | findstr ":8000"
netstat -ano | findstr ":8001"
netstat -ano | findstr ":8002"
netstat -ano | findstr ":8003"
netstat -ano | findstr ":8004"
netstat -ano | findstr ":8005"
netstat -ano | findstr ":8006"
netstat -ano | findstr ":8007"
netstat -ano | findstr ":8008"
netstat -ano | findstr ":3000"
netstat -ano | findstr ":3001"
netstat -ano | findstr ":5173"
```

If any port is in use, kill the process:
```bash
# Windows
taskkill /PID <PID> /F
```

---

## Summary

✅ **Total Services**: 12 (8 core + 4 application)  
✅ **Port Range**: 3000-3001, 5173, 8000-8008  
✅ **Port Conflicts**: RESOLVED (EMS moved from 8000 to 8008)  
✅ **Integration**: Complete (Gurukul ↔ 9-Pillar ↔ EMS)  
✅ **Status**: Production Ready

**Last Updated**: 2026-01-31  
**Port Conflict Resolution**: Complete ✅
