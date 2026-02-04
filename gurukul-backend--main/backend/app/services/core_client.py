"""
Core Integration Client for Gurukul Backend
Routes AI queries through BHIV Core (8002) with Insight validation
"""

import httpx
import asyncio
from typing import Dict, Any, Optional
from datetime import datetime, timezone

CORE_URL = "http://localhost:8002"
INSIGHT_CORE_URL = "http://localhost:8005"
INSIGHT_FLOW_URL = "http://localhost:8006"
TIMEOUT = 30.0

class CoreClient:
    """Client for integrating Gurukul with BHIV Core"""
    
    @staticmethod
    async def process_query(
        message: str,
        user_id: str,
        agent: str = "edumentor_agent",
        lesson_id: Optional[str] = None,
        context: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Process AI query through Core with intelligent routing
        
        Flow: Gurukul → Insight Flow (routing) → Core (processing)
        """
        try:
            async with httpx.AsyncClient() as client:
                # Route through Insight Flow for intelligent agent selection
                try:
                    flow_response = await client.post(
                        f"{INSIGHT_FLOW_URL}/route-agent",
                        json={
                            "query": message,
                            "user_id": user_id,
                            "context": {
                                "lesson_id": lesson_id,
                                "system": "gurukul",
                                **(context or {})
                            }
                        },
                        timeout=2.0
                    )
                    if flow_response.status_code == 200:
                        agent = flow_response.json().get("agent", agent)
                except Exception:
                    # Fallback to requested agent if routing fails
                    pass
                
                # Send to Core for processing
                core_response = await client.post(
                    f"{CORE_URL}/handle_task",
                    json={
                        "agent": agent,
                        "input": message,
                        "input_type": "text",
                        "tags": ["gurukul", "student_query", lesson_id or "general"]
                    },
                    timeout=TIMEOUT
                )
                
                if core_response.status_code == 200:
                    return {
                        "success": True,
                        "data": core_response.json(),
                        "agent_used": agent
                    }
                else:
                    return {
                        "success": False,
                        "error": f"Core returned {core_response.status_code}"
                    }
                    
        except asyncio.TimeoutError:
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    @staticmethod
    async def query_knowledge_base(
        query: str,
        filters: Optional[Dict] = None,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Query Core's multi-folder Qdrant knowledge base"""
        try:
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
                    return {"success": True, "data": response.json()}
                else:
                    return {"success": False, "error": f"Core returned {response.status_code}"}
                    
        except Exception as e:
            return {"success": False, "error": str(e)}

core_client = CoreClient()
