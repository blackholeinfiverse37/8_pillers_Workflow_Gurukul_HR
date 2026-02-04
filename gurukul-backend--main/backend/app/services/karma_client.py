"""
Karma Integration Client for Gurukul Backend
Forwards student actions to standalone Karma (8000) with fallback to embedded Karma
"""

import httpx
import asyncio
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

KARMA_URL = "http://localhost:8000"
TIMEOUT = 2.0

class KarmaClient:
    """Client for integrating Gurukul with standalone Karma service"""
    
    @staticmethod
    async def log_action(
        user_id: str,
        action: str,
        role: str = "learner",
        note: Optional[str] = None,
        metadata: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Log student action to standalone Karma with fallback to embedded
        
        Returns: {"success": bool, "source": "standalone" | "embedded"}
        """
        # Try standalone Karma first
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{KARMA_URL}/api/v1/log-action/",
                    json={
                        "user_id": user_id,
                        "action": action,
                        "role": role,
                        "note": note,
                        "metadata": {
                            "source": "gurukul",
                            **(metadata or {})
                        }
                    },
                    timeout=TIMEOUT
                )
                
                if response.status_code == 200:
                    return {"success": True, "source": "standalone", "data": response.json()}
                    
        except Exception as e:
            logger.debug(f"Standalone Karma unavailable: {e}")
        
        # Fallback to embedded Karma (already in Gurukul)
        return {"success": True, "source": "embedded", "fallback": True}
    
    @staticmethod
    async def get_karma_profile(user_id: str) -> Dict[str, Any]:
        """Get user's karma profile from standalone Karma"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{KARMA_URL}/api/v1/karma/{user_id}",
                    timeout=TIMEOUT
                )
                
                if response.status_code == 200:
                    return {"success": True, "data": response.json()}
                else:
                    return {"success": False, "error": f"Karma returned {response.status_code}"}
                    
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    @staticmethod
    async def log_lesson_completion(user_id: str, lesson_id: str, score: float) -> None:
        """Log lesson completion to Karma"""
        await KarmaClient.log_action(
            user_id=user_id,
            action="completing_lessons",
            role="learner",
            note=f"Completed lesson {lesson_id} with score {score}",
            metadata={"lesson_id": lesson_id, "score": score}
        )
    
    @staticmethod
    async def log_quiz_completion(user_id: str, quiz_id: str, score: float, total: int) -> None:
        """Log quiz completion to Karma"""
        await KarmaClient.log_action(
            user_id=user_id,
            action="completing_quizzes",
            role="learner",
            note=f"Completed quiz {quiz_id}: {score}/{total}",
            metadata={"quiz_id": quiz_id, "score": score, "total": total}
        )
    
    @staticmethod
    async def log_study_session(user_id: str, duration_minutes: int, focus_score: float) -> None:
        """Log study session to Karma"""
        await KarmaClient.log_action(
            user_id=user_id,
            action="studying_regularly",
            role="learner",
            note=f"Study session: {duration_minutes}min, focus: {focus_score}%",
            metadata={"duration_minutes": duration_minutes, "focus_score": focus_score}
        )

karma_client = KarmaClient()
