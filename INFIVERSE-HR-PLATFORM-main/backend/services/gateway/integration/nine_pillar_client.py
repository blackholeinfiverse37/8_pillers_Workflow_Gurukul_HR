"""
9-Pillar Integration Client for HR Platform Gateway
Provides connectivity to Bucket, Karma, and Core services
"""
import httpx
import asyncio
from datetime import datetime, timezone
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

class NinePillarClient:
    """Client for integrating HR Platform with 9-Pillar system"""
    
    def __init__(
        self,
        bucket_url: str = "http://localhost:8001",
        karma_url: str = "http://localhost:8000",
        core_url: str = "http://localhost:8002",
        timeout: float = 2.0,
        enabled: bool = True
    ):
        self.bucket_url = bucket_url
        self.karma_url = karma_url
        self.core_url = core_url
        self.timeout = timeout
        self.enabled = enabled
        
    async def log_event_to_bucket(
        self,
        event_type: str,
        event_data: Dict[str, Any],
        user_id: Optional[str] = None
    ) -> bool:
        """Log event to Bucket (fire-and-forget with timeout)"""
        if not self.enabled:
            return False
            
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                payload = {
                    "event_type": event_type,
                    "event_data": event_data,
                    "user_id": user_id,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "source": "hr_platform"
                }
                response = await client.post(
                    f"{self.bucket_url}/events",
                    json=payload
                )
                return response.status_code == 200
        except Exception as e:
            logger.warning(f"Bucket event logging failed: {e}")
            return False
    
    async def track_action_in_karma(
        self,
        user_id: str,
        action_type: str,
        action_data: Dict[str, Any]
    ) -> bool:
        """Track action in Karma (fire-and-forget with timeout)"""
        if not self.enabled:
            return False
            
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                payload = {
                    "user_id": user_id,
                    "action_type": action_type,
                    "action_data": action_data,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "source": "hr_platform"
                }
                response = await client.post(
                    f"{self.karma_url}/actions",
                    json=payload
                )
                return response.status_code == 200
        except Exception as e:
            logger.warning(f"Karma action tracking failed: {e}")
            return False
    
    async def route_through_core(
        self,
        query: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:
        """Route AI query through Core (optional, with fallback)"""
        if not self.enabled:
            return None
            
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                payload = {
                    "query": query,
                    "context": context or {},
                    "source": "hr_platform"
                }
                response = await client.post(
                    f"{self.core_url}/query",
                    json=payload
                )
                if response.status_code == 200:
                    return response.json()
                return None
        except Exception as e:
            logger.warning(f"Core routing failed: {e}")
            return None

# Global instance
nine_pillar_client = None

def get_nine_pillar_client() -> NinePillarClient:
    """Get or create global 9-Pillar client instance"""
    global nine_pillar_client
    if nine_pillar_client is None:
        import os
        nine_pillar_client = NinePillarClient(
            bucket_url=os.getenv("BUCKET_URL", "http://localhost:8001"),
            karma_url=os.getenv("KARMA_URL", "http://localhost:8000"),
            core_url=os.getenv("CORE_URL", "http://localhost:8002"),
            enabled=os.getenv("ENABLE_9PILLAR_INTEGRATION", "true").lower() == "true"
        )
    return nine_pillar_client
