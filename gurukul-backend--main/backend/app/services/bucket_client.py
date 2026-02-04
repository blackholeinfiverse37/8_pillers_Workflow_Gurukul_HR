"""
Bucket Integration Client for Gurukul Backend
Forwards events to Bucket (8001) for audit trail and governance
"""

import httpx
import asyncio
from typing import Dict, Any
from datetime import datetime, timezone
import logging

logger = logging.getLogger(__name__)

BUCKET_URL = "http://localhost:8001"
TIMEOUT = 2.0

class BucketClient:
    """Client for integrating Gurukul with BHIV Bucket"""
    
    @staticmethod
    async def write_event(event_data: Dict[str, Any]) -> None:
        """
        Fire-and-forget event write to Bucket
        Non-blocking - Gurukul continues even if Bucket is unavailable
        """
        try:
            async with httpx.AsyncClient() as client:
                await asyncio.wait_for(
                    client.post(
                        f"{BUCKET_URL}/core/write-event",
                        json={
                            "requester_id": "gurukul_backend",
                            "event_data": {
                                "timestamp": datetime.now(timezone.utc).isoformat(),
                                "source": "gurukul",
                                **event_data
                            }
                        },
                        timeout=TIMEOUT
                    ),
                    timeout=TIMEOUT
                )
        except Exception as e:
            # Silently log and continue - Gurukul doesn't depend on Bucket
            logger.debug(f"Bucket write failed (non-blocking): {e}")
    
    @staticmethod
    async def log_lesson_event(
        user_id: str,
        lesson_id: str,
        event_type: str,
        metadata: Dict[str, Any] = None
    ) -> None:
        """Log lesson-related events"""
        await BucketClient.write_event({
            "event_type": f"lesson_{event_type}",
            "user_id": user_id,
            "lesson_id": lesson_id,
            "metadata": metadata or {}
        })
    
    @staticmethod
    async def log_quiz_event(
        user_id: str,
        quiz_id: str,
        score: float,
        total_questions: int,
        metadata: Dict[str, Any] = None
    ) -> None:
        """Log quiz completion events"""
        await BucketClient.write_event({
            "event_type": "quiz_completed",
            "user_id": user_id,
            "quiz_id": quiz_id,
            "score": score,
            "total_questions": total_questions,
            "metadata": metadata or {}
        })
    
    @staticmethod
    async def log_chat_event(
        user_id: str,
        message: str,
        response: str,
        agent_used: str,
        metadata: Dict[str, Any] = None
    ) -> None:
        """Log AI chat interactions"""
        await BucketClient.write_event({
            "event_type": "chat_interaction",
            "user_id": user_id,
            "message": message[:100],  # Truncate for privacy
            "response": response[:100],
            "agent_used": agent_used,
            "metadata": metadata or {}
        })

bucket_client = BucketClient()
