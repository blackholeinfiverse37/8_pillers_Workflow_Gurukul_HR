# 🚀 BHIV Core ↔ Bucket ↔ Karma ↔ PRANA ↔ Workflow ↔ UAO ↔ Insight ↔ Gurukul ↔ EMS Integration System

**Status**: ✅ **PRODUCTION READY** | **Test Results**: 5/5 Passing (100%) ✅  
**Architecture**: 12-service integrated platform with AI orchestration + behavioral tracking + telemetry + learning management  
**Last Updated**: 2026-02-04 | **Version**: 3.0.0

## 🎯 System Overview

Complete integration of **12 services** across **3 layers**:

### Layer 1: Core 9-Pillar Services (Ports 8000-8007)
- **Karma (8000)**: Q-learning behavioral tracking with karma computation
- **Bucket (8001)**: Constitutional governance, audit trail, and event storage
- **Core (8002)**: AI Decision Engine with UCB-based agent selection & multi-modal processing
- **Workflow (8003)**: Deterministic real-world action execution
- **UAO (8004)**: Unified action orchestration & lifecycle management
- **Insight Core (8005)**: JWT security enforcement & replay attack prevention
- **Insight Flow Bridge (8006)**: Intelligent agent routing with Q-learning
- **Insight Flow Backend (8007)**: Optional full Q-learning routing

### Layer 2: Application Services (Ports 3000, 8008)
- **Gurukul Backend (3000)**: Student learning platform API with Core/Bucket/Karma integration
- **EMS Backend (8008)**: Employee management system API

### Layer 3: Frontend Services (Ports 3001, 5173)
- **Gurukul Frontend (5173)**: Student learning interface with PRANA telemetry
- **EMS Frontend (3001)**: Employee management interface

### Key Features
✅ **12-Service Architecture**: 9-Pillar + Gurukul + EMS (complete integration)  
✅ **Gurukul Integration**: AI tutoring with Core routing, Bucket logging, Karma tracking  
✅ **Security Layer**: JWT validation + replay attack prevention (Insight Core)  
✅ **Deep Integration**: Gurukul → Insight Flow → Core → Bucket → Karma  
✅ **Workflow Execution**: Deterministic task/email/WhatsApp/AI/reminder execution  
✅ **Action Orchestration**: High-level action lifecycle management  
✅ **PRANA Telemetry**: Real-time user behavior tracking (7 cognitive states)  
✅ **Fire-and-Forget**: Non-blocking async operations (2s timeout, zero latency impact)  
✅ **Zero Regression**: Original functionality preserved (100% backward compatible)  
✅ **Graceful Degradation**: Each service works independently (no circular dependencies)  
✅ **Complete Audit Trail**: Every action logged permanently (immutable audit)  
✅ **RL Intelligence**: UCB agent selection + Q-learning behavioral tracking  
✅ **Multi-Modal**: Text, PDF, image, audio processing with knowledge base integration  
✅ **Timezone Fix**: All datetime operations are timezone-aware (Python 3.12+ compatible)

---

## 🏗️ Complete System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    USER (Student/Teacher/Employee)                   │
└────────────────────────────┬────────────────────────────────────────┘
                             ↓
        ┌────────────────────┴────────────────────┐
        ↓                                         ↓
┌───────────────────┐                    ┌───────────────────┐
│ GURUKUL FRONTEND  │                    │   EMS FRONTEND    │
│    (Port 5173)    │                    │   (Port 3001)     │
│ • Chat Interface  │                    │ • Employee Mgmt   │
│ • PRANA Telemetry │                    │ • Attendance      │
└─────────┬─────────┘                    └─────────┬─────────┘
          ↓                                        ↓
┌─────────────────────────────────────────────────────────────────────┐
│                     APPLICATION LAYER (3000, 8008)                   │
│  ┌──────────────────────┐         ┌──────────────────────┐          │
│  │ GURUKUL BACKEND      │         │   EMS BACKEND        │          │
│  │ • Core Client        │         │ • Student Mgmt       │          │
│  │ • Bucket Client      │         │ • Teacher Mgmt       │          │
│  │ • Karma Client       │         │ • School Mgmt        │          │
│  └──────────┬───────────┘         └──────────────────────┘          │
└─────────────┼─────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────────────────────┐
│              9-PILLAR CORE SERVICES (8000-8007)                      │
│                                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │ INSIGHT FLOW │→ │    CORE      │→ │ INSIGHT CORE │              │
│  │    (8006)    │  │   (8002)     │  │   (8005)     │              │
│  │ Q-Learning   │  │ AI Engine    │  │ JWT Security │              │
│  └──────────────┘  └──────────────┘  └──────┬───────┘              │
│                                              ↓                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │   BUCKET     │← │    KARMA     │← │  WORKFLOW    │              │
│  │   (8001)     │  │   (8000)     │  │   (8003)     │              │
│  │ Event Store  │  │ Q-Learning   │  │ Task Exec    │              │
│  └──────────────┘  └──────────────┘  └──────────────┘              │
│                                                                      │
│  ┌──────────────┐                                                   │
│  │     UAO      │                                                   │
│  │   (8004)     │                                                   │
│  │ Orchestrator │                                                   │
│  └──────────────┘                                                   │
└─────────────────────────────────────────────────────────────────────┘

DATA FLOW:
1. User → Frontend (5173/3001)
2. Frontend → Backend (3000/8008)
3. Backend → Insight Flow (8006) → Core (8002) [AI Routing]
4. Core → Insight Core (8005) [Security Validation]
5. Backend → Bucket (8001) [Event Logging]
6. Backend → Karma (8000) [Behavioral Tracking]
7. Bucket → Karma [Event Forwarding]
```

---

## 🔌 Complete Port Allocation

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

## 🚀 Starting the Complete System

### Prerequisites
- Python 3.11+
- Node.js 16+
- MongoDB Atlas account
- Redis Cloud account (optional)

### Step-by-Step Startup (11 Terminals)

**Terminal 1: Karma (8000)**
```bash
cd "karma_chain_v2-main"
python main.py
```
✅ Wait for: "Application startup complete"

**Terminal 2: Bucket (8001)**
```bash
cd "BHIV_Central_Depository-main"
python main.py
```
✅ Wait for: "Application startup complete"

**Terminal 3: Core (8002)**
```bash
cd "v1-BHIV_CORE-main"
python mcp_bridge.py
```
✅ Wait for: "Uvicorn running on http://0.0.0.0:8002"

**Terminal 4: Workflow (8003)**
```bash
cd "workflow-executor-main"
python main.py
```
✅ Wait for: "Uvicorn running on http://0.0.0.0:8003"

**Terminal 5: UAO (8004)**
```bash
cd "Unified Action Orchestration"
python action_orchestrator.py
```
✅ Wait for: "Uvicorn running on http://0.0.0.0:8004"

**Terminal 6: Insight Core (8005)**
```bash
cd "insightcore-bridgev4x-main"
python insight_service.py
```
✅ Wait for: "Uvicorn running on http://0.0.0.0:8005"

**Terminal 7: Insight Flow Bridge (8006) - Optional**
```bash
cd "Insight_Flow-main"
start_bridge_standalone.bat
```
✅ Wait for: "Uvicorn running on http://0.0.0.0:8006"

**Terminal 8: Gurukul Backend (3000)**
```bash
cd "gurukul-backend--main/backend"
uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload
```
✅ Wait for: "Application startup complete"

**Terminal 9: EMS Backend (8008)**
```bash
cd "gurukul-backend--main/EMS System"
uvicorn app.main:app --host 0.0.0.0 --port 8008 --reload
```
✅ Wait for: "Application startup complete"

**Terminal 10: Gurukul Frontend (5173)**
```bash
cd "gurukul-backend--main/Frontend"
npm run dev
```
✅ Wait for: "Local: http://localhost:5173"

**Terminal 11: EMS Frontend (3001)**
```bash
cd "gurukul-backend--main/EMS System/frontend"
npm run dev
```
✅ Wait for: "Local: http://localhost:3001"

**Total Startup Time**: ~2 minutes

---

## 🧪 Testing & Verification

### Health Checks (All 12 Services)
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
```

### Gurukul Integration Test
```bash
cd "gurukul-backend--main"
python test_gurukul_integration.py
```

**Expected Result**: 5/5 tests passing (100%)
```
[PASS] - Health Checks
[PASS] - Chat Integration
[PASS] - PRANA Ingestion
[PASS] - Bucket Events
[PASS] - Karma Integration

Results: 5/5 tests passed (100%)
[SUCCESS] All tests passed! Gurukul is fully integrated!
```

---

## 📚 Gurukul Integration Details

### What is Gurukul?
Gurukul is a student learning platform integrated with the 9-pillar system:
- **AI Tutoring**: Chat interface with intelligent agent routing through Core
- **Subject Learning**: Explore subjects with AI-powered explanations
- **Quiz System**: Take quizzes with automatic grading and feedback
- **PRANA Telemetry**: Real-time cognitive state tracking (7 states)
- **Behavioral Tracking**: Karma-based role progression (learner → volunteer → seva → guru)

### Integration Architecture
```
Gurukul Frontend (5173)
    ↓ (user interaction)
Gurukul Backend (3000)
    ├─→ Core Client → Insight Flow (8006) → Core (8002) [AI Routing]
    ├─→ Bucket Client → Bucket (8001) [Event Logging]
    └─→ Karma Client → Karma (8000) [Behavioral Tracking]
```

### Key Integration Points
1. **Chat Integration**: Routes queries through Insight Flow → Core with fallback to local Groq
2. **Event Logging**: Logs lesson completions, quiz submissions, chat interactions to Bucket
3. **Behavioral Tracking**: Tracks student actions in Karma for role progression
4. **PRANA Telemetry**: Ingests cognitive state packets every 5 seconds
5. **Fire-and-Forget**: All integrations are non-blocking with 2s timeout

### Environment Configuration
See `gurukul-backend--main/README.md` for complete `.env` configuration with all API keys and integration URLs.

---

## ⚙️ Key Environment Variables

### Gurukul Backend (.env)
```env
# 9-Pillar Integration URLs
CORE_URL=http://localhost:8002
BUCKET_URL=http://localhost:8001
KARMA_URL=http://localhost:8000
INSIGHT_CORE_URL=http://localhost:8005
INSIGHT_FLOW_URL=http://localhost:8006

# Feature Flags
ENABLE_CORE_INTEGRATION=true
ENABLE_BUCKET_INTEGRATION=true
ENABLE_KARMA_INTEGRATION=true

# API Keys
GROQ_API_KEY=your-groq-api-key
OPENAI_API_KEY=your-openai-api-key
GEMINI_API_KEY=your-gemini-api-key

# MongoDB (for Karma Tracker)
MONGODB_URI=your-mongodb-atlas-uri
MONGODB_DATABASE=gurukul_karma

# EMS Integration
EMS_API_BASE_URL=http://localhost:8008
```

### Karma Service (.env)
```env
MONGODB_URI=your-mongodb-atlas-uri
DB_NAME=karma-chain
ALPHA=0.15
GAMMA=0.9
```

### Bucket Service (.env)
```env
REDIS_HOST=your-redis-cloud-host
REDIS_PASSWORD=your-redis-password
MONGODB_URI=your-mongodb-atlas-uri
```

---

## 🔧 Troubleshooting

### Issue: Karma returns 500 error (timezone)
**Solution**: Run the datetime fix script
```bash
cd "karma_chain_v2-main"
python fix_user_datetimes.py
```

### Issue: Port already in use
**Solution**: Check and kill process
```bash
netstat -ano | findstr ":8000"
taskkill /PID <PID> /F
```

### Issue: Gurukul can't connect to Core/Bucket/Karma
**Solution**: Gurukul continues with fallback. Verify services are running:
```bash
curl http://localhost:8000/health
curl http://localhost:8001/health
curl http://localhost:8002/health
```

---

## ✅ Success Indicators

✅ All 12 services start without errors  
✅ Health checks return "healthy" status  
✅ Gurukul integration test passes 5/5 checks (100%)  
✅ Chat routes through Core with fallback to Groq  
✅ Events logged to Bucket (lesson, quiz, chat)  
✅ Karma tracks behavioral data (Q-learning updates)  
✅ PRANA telemetry ingested (cognitive states)  
✅ Port conflicts resolved (EMS moved to 8008)  
✅ Timezone issues fixed (datetime.now(timezone.utc))  
✅ Graceful degradation working (services independent)  
✅ Fire-and-forget pattern operational (2s timeout)  
✅ Zero regression (original functionality preserved)  

**The complete 12-service integrated system (9-Pillar + Gurukul + EMS) is production-ready! 🧠📚⚖️👁️⚙️🎼🔒🧭🎓💼**

---

## 📚 Documentation

### Gurukul Integration
- **gurukul-backend--main/README.md** - Complete setup guide with all `.env` configurations
- **GURUKUL_INTEGRATION_COMPLETE.md** - Integration completion report
- **PORT_ALLOCATION.md** - Complete port allocation table
- **KARMA_TIMEZONE_FIX.md** - Timezone fix documentation

### 9-Pillar System
- **INSIGHT_FLOW_INTEGRATION.md** - Insight Flow integration guide
- **INSIGHT_CORE_INTEGRATION_COMPLETE.md** - Insight Core technical guide
- **UAO_INTEGRATION_COMPLETE.md** - UAO integration guide
- **PRANA_INTEGRATION_COMPLETE.md** - PRANA technical guide

---

**Last Updated**: 2026-02-04  
**Maintained By**: Integration Team  
**Status**: Production Ready ✅  
**Version**: 3.0.0 (12-Service Integration Complete)  
**Gurukul Integration**: 100% Complete ✅  
**Test Pass Rate**: 5/5 (100%) ✅
