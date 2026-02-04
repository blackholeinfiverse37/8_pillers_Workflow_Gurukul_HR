# 🎓 Gurukul Backend Integration Plan

**Status**: 📋 PLANNING PHASE  
**Target**: Integrate Gurukul backend (port 3000) with existing 8-pillar system  
**Last Updated**: 2026-02-04  
**Version**: 1.0.0

---

## 📊 Current System Analysis

### Existing 8-Pillar Architecture (ALL WORKING ✅)

| Service | Port | Status | Purpose |
|---------|------|--------|---------|
| **Karma** | 8000 | ✅ Running | Q-learning behavioral tracking |
| **Bucket** | 8001 | ✅ Running | Constitutional governance + audit |
| **Core** | 8002 | ✅ Running | AI decision engine (RL-based) |
| **Workflow** | 8003 | ✅ Running | Deterministic action execution |
| **UAO** | 8004 | ✅ Running | Unified action orchestration |
| **Insight Core** | 8005 | ✅ Running | JWT + replay attack prevention |
| **Insight Flow Bridge** | 8006 | ✅ Running | Intelligent agent routing |
| **Insight Flow Backend** | 8007 | ⚠️ Optional | Full Q-learning routing |

### Gurukul Backend (TO BE INTEGRATED)

| Service | Port | Status | Purpose |
|---------|------|--------|---------|
| **Gurukul Backend** | 3000 | 🔄 Standalone | Learning management system |

---

## 🎯 Integration Goals

### Primary Objectives
1. ✅ **Maintain Integrity**: Keep all 8 existing services working perfectly
2. 🔗 **Add Gurukul Layer**: Integrate as 9th pillar without breaking existing flow
3. 🔄 **Bidirectional Communication**: Gurukul ↔ Core ↔ Bucket ↔ Karma
4. 📊 **PRANA Telemetry**: Gurukul frontend → Bucket → Karma (already exists!)
5. 🔒 **Security**: JWT validation through Insight Core
6. 🎭 **Agent Routing**: Gurukul queries → Insight Flow → Core agents

### Key Requirements
- ✅ Zero regression on existing services
- ✅ Graceful degradation (Gurukul works standalone if needed)
- ✅ Fire-and-forget pattern (non-blocking)
- ✅ Complete audit trail
- ✅ Karma tracking for student behavior

---

## 🏗️ Architecture Design

### Integration Pattern

```
┌─────────────────────────────────────────────────────────────┐
│  GURUKUL FRONTEND (React/Vite)                              │
│  ├─ Student Dashboard                                       │
│  ├─ Lesson Viewer                                           │
│  ├─ Quiz System                                             │
│  └─ PRANA Telemetry (already integrated!) ✅                │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│  GURUKUL BACKEND (Port 3000) - NEW INTEGRATION 🆕           │
│  ├─ Auth (JWT-based)                                        │
│  ├─ Learning Management                                     │
│  ├─ Quiz Engine                                             │
│  ├─ Flashcards                                              │
│  ├─ Chat (AI-powered)                                       │
│  ├─ Bucket Router (PRANA ingestion) ✅                      │
│  └─ Karma Tracker (embedded) ✅                             │
└──────────┬────────────────────────────┬─────────────────────┘
           ↓ (AI queries)               ↓ (PRANA packets)
┌──────────────────────────┐   ┌────────────────────────────────┐
│  INSIGHT CORE (8005) ✨  │   │  BUCKET (8001)                 │
│  - JWT Validation        │   │  - PRANA Ingestion ✅          │
│  - Replay Prevention     │   │  - Event Storage               │
│  - Security Metrics      │   │  - Constitutional Gov          │
└──────────┬───────────────┘   └──────────┬─────────────────────┘
           ↓ (validated)                  ↓ (forward)
┌──────────────────────────┐   ┌────────────────────────────────┐
│  INSIGHT FLOW (8006) ✨  │   │  KARMA (8000)                  │
│  - Q-Learning Routing    │   │  - Q-Learning Engine           │
│  - Karma Weighting       │   │  - Behavioral Tracking         │
│  - Agent Selection       │   │  - Student Progress            │
└──────────┬───────────────┘   └────────────────────────────────┘
           ↓ (route to agent)
┌─────────────────────────────────────────────────────────────┐
│  BHIV CORE (8002)                                           │
│  ├─ Agent Registry (RL-based selection)                     │
│  ├─ EduMentor Agent (educational queries)                   │
│  ├─ Knowledge Agent (Vedabase search)                       │
│  ├─ Quiz Agent (question generation)                        │
│  └─ Multi-Modal Processing                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 Integration Points

### 1. PRANA Telemetry (ALREADY WORKING ✅)

**Current Status**: Gurukul backend already has PRANA bucket router!

**File**: `gurukul-backend--main/backend/app/routers/bucket.py`

**Endpoints**:
- ✅ `POST /api/v1/bucket/prana/ingest` - Receive PRANA packets
- ✅ `GET /api/v1/bucket/prana/packets/pending` - Get pending packets
- ✅ `POST /api/v1/bucket/prana/packets/mark-processed` - Mark as processed
- ✅ `GET /api/v1/bucket/prana/status` - Get bucket status

**Integration Flow**:
```
Gurukul Frontend → POST /api/v1/bucket/prana/ingest (Gurukul Backend)
                 → Store in PostgreSQL/SQLite
                 → Queue in Redis (optional)
                 → Karma Tracker polls /api/v1/bucket/prana/packets/pending
                 → Process and update karma
                 → Mark as processed
```

**Action Required**: 
- ✅ PRANA endpoints already exist in Gurukul backend
- 🔄 Need to connect Karma Tracker (8000) to poll Gurukul's PRANA endpoints
- 🔄 Alternative: Forward PRANA packets from Gurukul → Bucket (8001) → Karma (8000)

---

### 2. AI Chat Integration (NEW)

**Current**: Gurukul has its own chat router (`app/routers/chat.py`)

**Target**: Route AI queries through Core for better agent selection

**Integration Options**:

#### Option A: Direct Core Integration (Recommended)
```python
# In gurukul-backend/app/routers/chat.py

import httpx
from app.core.config import settings

CORE_URL = settings.CORE_URL or "http://localhost:8002"
INSIGHT_CORE_URL = settings.INSIGHT_CORE_URL or "http://localhost:8005"

async def process_chat_message(message: str, user_id: str, lesson_id: str = None):
    # Step 1: Validate through Insight Core (JWT + nonce)
    async with httpx.AsyncClient() as client:
        # Generate JWT token for request
        token = generate_jwt_token(user_id)
        nonce = generate_nonce()
        
        # Validate through Insight Core
        insight_response = await client.post(
            f"{INSIGHT_CORE_URL}/validate",
            json={
                "token": token,
                "nonce": nonce,
                "request_data": {"message": message, "user_id": user_id}
            },
            timeout=2.0
        )
        
        if insight_response.status_code != 200:
            return {"error": "Security validation failed"}
        
        # Step 2: Route through Insight Flow for intelligent agent selection
        flow_response = await client.post(
            f"{INSIGHT_FLOW_URL}/route-agent",
            json={
                "query": message,
                "user_id": user_id,
                "context": {"lesson_id": lesson_id, "system": "gurukul"}
            },
            timeout=2.0
        )
        
        selected_agent = flow_response.json().get("agent", "edumentor_agent")
        
        # Step 3: Send to Core for processing
        core_response = await client.post(
            f"{CORE_URL}/handle_task",
            json={
                "agent": selected_agent,
                "input": message,
                "input_type": "text",
                "tags": ["gurukul", "student_query", lesson_id]
            },
            timeout=30.0
        )
        
        return core_response.json()
```

#### Option B: Keep Gurukul Standalone (Fallback)
- Keep existing Gurukul chat implementation
- Add optional Core integration as enhancement
- Graceful degradation if Core is unavailable

---

### 3. Knowledge Base Integration (NEW)

**Current**: Gurukul has vector store support (ChromaDB/Qdrant)

**Target**: Use Core's multi-folder Qdrant setup for Vedabase queries

**Integration**:

```python
# In gurukul-backend/app/routers/learning.py

async def query_knowledge_base(query: str, filters: dict = None):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{CORE_URL}/query-kb",
            json={
                "query": query,
                "filters": filters or {},
                "tags": ["gurukul", "vedabase"]
            },
            timeout=10.0
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            # Fallback to local vector store
            return local_vector_search(query, filters)
```

---

### 4. Karma Integration (ALREADY EMBEDDED ✅)

**Current Status**: Gurukul backend has Karma Tracker embedded!

**Files**:
- ✅ `app/routers/karma_tracker/` - Full Karma API
- ✅ `app/utils/karma/` - Karma utilities (Q-learning, analytics, etc.)
- ✅ `app/models/karma_models.py` - Karma data models

**Endpoints** (already available):
- ✅ `POST /api/v1/karma/log-action/` - Log student actions
- ✅ `GET /api/v1/karma/{user_id}` - Get karma profile
- ✅ `GET /api/v1/analytics/karma_trends` - Get karma trends

**Integration Options**:

#### Option A: Use Embedded Karma (Current)
- Keep using Gurukul's embedded Karma Tracker
- Sync with standalone Karma (8000) periodically

#### Option B: Forward to Standalone Karma (Recommended)
```python
# In gurukul-backend/app/routers/karma_tracker/karma.py

import httpx

KARMA_SERVICE_URL = "http://localhost:8000"

async def log_action(user_id: str, action: str, role: str, note: str = None):
    # Try standalone Karma service first
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{KARMA_SERVICE_URL}/api/v1/log-action/",
                json={
                    "user_id": user_id,
                    "action": action,
                    "role": role,
                    "note": note
                },
                timeout=2.0
            )
            if response.status_code == 200:
                return response.json()
    except Exception as e:
        logger.warning(f"Standalone Karma unavailable: {e}")
    
    # Fallback to embedded Karma
    return embedded_karma_log_action(user_id, action, role, note)
```

---

### 5. Bucket Integration (NEW)

**Target**: Forward Gurukul events to Bucket for audit trail

**Integration**:

```python
# In gurukul-backend/app/services/bucket_client.py

import httpx
import asyncio
from datetime import datetime, timezone

BUCKET_URL = "http://localhost:8001"

class BucketClient:
    @staticmethod
    async def write_event(event_data: dict):
        """Fire-and-forget event write to Bucket"""
        try:
            async with httpx.AsyncClient() as client:
                await asyncio.wait_for(
                    client.post(
                        f"{BUCKET_URL}/core/write-event",
                        json={
                            "requester_id": "gurukul_backend",
                            "event_data": {
                                "timestamp": datetime.now(timezone.utc).isoformat(),
                                **event_data
                            }
                        },
                        timeout=2.0
                    ),
                    timeout=2.0
                )
        except Exception:
            # Silently continue - Gurukul doesn't depend on Bucket
            pass

# Usage in routers
await BucketClient.write_event({
    "event_type": "lesson_completed",
    "user_id": user_id,
    "lesson_id": lesson_id,
    "score": score
})
```

---

## 📝 Implementation Steps

### Phase 1: Analysis & Planning (CURRENT)
- [x] Analyze Gurukul backend structure
- [x] Identify integration points
- [x] Document existing PRANA integration
- [x] Document embedded Karma Tracker
- [ ] Review Gurukul API endpoints
- [ ] Map Gurukul → Core agent routing

### Phase 2: Core Integration (Week 1)
- [ ] Add Core client to Gurukul backend
- [ ] Implement chat routing through Core
- [ ] Add Insight Core JWT validation
- [ ] Add Insight Flow agent routing
- [ ] Test AI query flow end-to-end

### Phase 3: Bucket Integration (Week 1)
- [ ] Add Bucket client to Gurukul backend
- [ ] Forward lesson events to Bucket
- [ ] Forward quiz events to Bucket
- [ ] Forward user actions to Bucket
- [ ] Test audit trail completeness

### Phase 4: Karma Integration (Week 2)
- [ ] Connect Gurukul PRANA to Karma (8000)
- [ ] Forward student actions to Karma
- [ ] Sync embedded Karma with standalone Karma
- [ ] Test behavioral tracking
- [ ] Verify karma score updates

### Phase 5: Knowledge Base Integration (Week 2)
- [ ] Route Vedabase queries to Core
- [ ] Test multi-folder Qdrant search
- [ ] Implement fallback to local vector store
- [ ] Optimize query performance

### Phase 6: Testing & Validation (Week 3)
- [ ] End-to-end integration tests
- [ ] Performance testing
- [ ] Security validation
- [ ] Graceful degradation tests
- [ ] Load testing

### Phase 7: Documentation & Deployment (Week 3)
- [ ] Update README with Gurukul integration
- [ ] Create startup scripts
- [ ] Update health check endpoints
- [ ] Create monitoring dashboard
- [ ] Production deployment

---

## 🔒 Security Considerations

### JWT Validation
- All Gurukul → Core requests must go through Insight Core (8005)
- JWT tokens with user_id, role, and expiry
- Nonce-based replay attack prevention

### Data Privacy
- Student data stays in Gurukul database
- Only behavioral events sent to Karma
- PRANA packets anonymized (no PII)
- Audit trail in Bucket (encrypted)

### Rate Limiting
- Implement rate limiting on Gurukul endpoints
- Prevent abuse of AI chat
- Throttle PRANA packet ingestion

---

## 📊 Monitoring & Observability

### Health Checks
```bash
# Gurukul Backend
curl http://localhost:3000/health

# Expected Response
{
  "status": "healthy",
  "services": {
    "database": "connected",
    "redis": "connected",
    "core_integration": "active",
    "bucket_integration": "active",
    "karma_integration": "active"
  }
}
```

### Metrics
- Request count per endpoint
- AI query latency
- PRANA packet ingestion rate
- Karma score updates
- Error rates

---

## 🚀 Startup Sequence

### Updated 9-Pillar Startup

```bash
# Terminal 1: Karma
cd karma_chain_v2-main
python main.py

# Terminal 2: Bucket
cd BHIV_Central_Depository-main
python main.py

# Terminal 3: Core
cd v1-BHIV_CORE-main
python mcp_bridge.py

# Terminal 4: Workflow
cd workflow-executor-main
python main.py

# Terminal 5: UAO
cd "Unified Action Orchestration"
python action_orchestrator.py

# Terminal 6: Insight Core
cd insightcore-bridgev4x-main
python insight_service.py

# Terminal 7: Insight Flow Bridge
cd Insight_Flow-main
start_bridge_standalone.bat

# Terminal 8: Insight Flow Backend (Optional)
cd Insight_Flow-main
start_insight_flow_fixed.bat

# Terminal 9: Gurukul Backend (NEW)
cd gurukul-backend--main/backend
python -m app.main
```

---

## 🧪 Testing Strategy

### Integration Tests

```python
# test_gurukul_integration.py

import pytest
import httpx

GURUKUL_URL = "http://localhost:3000"
CORE_URL = "http://localhost:8002"
BUCKET_URL = "http://localhost:8001"
KARMA_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_gurukul_health():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{GURUKUL_URL}/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

@pytest.mark.asyncio
async def test_gurukul_to_core_chat():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{GURUKUL_URL}/api/v1/chat",
            json={
                "message": "What is dharma?",
                "user_id": "test_student_123",
                "lesson_id": "lesson_001"
            }
        )
        assert response.status_code == 200
        assert "response" in response.json()

@pytest.mark.asyncio
async def test_prana_ingestion():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{GURUKUL_URL}/api/v1/bucket/prana/ingest",
            json={
                "user_id": "test_student_123",
                "session_id": "session_456",
                "lesson_id": "lesson_001",
                "system_type": "gurukul",
                "role": "student",
                "timestamp": "2026-02-04T10:00:00Z",
                "cognitive_state": "ON_TASK",
                "active_seconds": 4.5,
                "idle_seconds": 0.3,
                "away_seconds": 0.2,
                "focus_score": 85,
                "raw_signals": {}
            }
        )
        assert response.status_code == 200

@pytest.mark.asyncio
async def test_karma_logging():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{GURUKUL_URL}/api/v1/karma/log-action/",
            json={
                "user_id": "test_student_123",
                "action": "completing_lessons",
                "role": "learner",
                "note": "Completed lesson on dharma"
            }
        )
        assert response.status_code == 200
```

---

## 📚 Configuration

### Environment Variables

```env
# Gurukul Backend .env

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/gurukul

# Integration URLs
CORE_URL=http://localhost:8002
BUCKET_URL=http://localhost:8001
KARMA_URL=http://localhost:8000
INSIGHT_CORE_URL=http://localhost:8005
INSIGHT_FLOW_URL=http://localhost:8006

# JWT
JWT_SECRET_KEY=your-secret-key-change-in-production
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=10080

# Feature Flags
ENABLE_CORE_INTEGRATION=true
ENABLE_BUCKET_INTEGRATION=true
ENABLE_KARMA_INTEGRATION=true
ENABLE_INSIGHT_VALIDATION=true

# Redis (for PRANA queue)
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=
```

---

## 🎯 Success Criteria

### Integration Complete When:
- ✅ All 9 services start without errors
- ✅ Gurukul health check passes
- ✅ AI chat routes through Core
- ✅ PRANA packets reach Karma
- ✅ Student actions logged in Bucket
- ✅ Karma scores update correctly
- ✅ Knowledge base queries work
- ✅ JWT validation active
- ✅ Graceful degradation works
- ✅ Zero regression on existing 8 pillars

---

## 📖 Next Steps

1. **Review this plan** with team
2. **Approve integration approach**
3. **Start Phase 2** (Core Integration)
4. **Create integration branch** in Git
5. **Begin implementation**

---

**Status**: 📋 READY FOR IMPLEMENTATION  
**Owner**: Development Team  
**Timeline**: 3 weeks  
**Risk Level**: LOW (non-invasive integration)

