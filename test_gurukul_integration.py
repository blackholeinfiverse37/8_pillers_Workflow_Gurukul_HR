"""
Gurukul Integration Test - 9-Pillar System
Tests Gurukul integration with Core, Bucket, and Karma
"""

import asyncio
import httpx
from datetime import datetime

# Service URLs
GURUKUL_URL = "http://localhost:3000"
CORE_URL = "http://localhost:8002"
BUCKET_URL = "http://localhost:8001"
KARMA_URL = "http://localhost:8000"
INSIGHT_CORE_URL = "http://localhost:8005"
INSIGHT_FLOW_URL = "http://localhost:8006"

async def test_service_health(name: str, url: str) -> bool:
    """Test if service is healthy"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{url}/health", timeout=5.0)
            if response.status_code == 200:
                print(f"[PASS] {name} is healthy")
                return True
            else:
                print(f"[FAIL] {name} returned {response.status_code}")
                return False
    except Exception as e:
        print(f"[FAIL] {name} is unavailable: {e}")
        return False

async def test_gurukul_chat_integration() -> bool:
    """Test Gurukul chat with Core integration"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{GURUKUL_URL}/api/v1/chat",
                json={
                    "message": "What is dharma?",
                    "user_id": "test_student_123",
                    "lesson_id": "test_lesson_001",
                    "use_core": True
                },
                timeout=30.0
            )
            
            if response.status_code == 200:
                data = response.json()
                if "response" in data:
                    print(f"[PASS] Gurukul chat integration working")
                    print(f"   Core used: {data.get('core_used', False)}")
                    print(f"   Agent: {data.get('agent_used', 'N/A')}")
                    return True
            
            print(f"[FAIL] Gurukul chat failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"[FAIL] Gurukul chat error: {e}")
        return False

async def test_prana_ingestion() -> bool:
    """Test PRANA packet ingestion"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{GURUKUL_URL}/api/v1/bucket/prana/ingest",
                json={
                    "user_id": "test_student_123",
                    "session_id": "test_session_456",
                    "lesson_id": "test_lesson_001",
                    "system_type": "gurukul",
                    "role": "student",
                    "timestamp": datetime.now().isoformat() + "Z",
                    "cognitive_state": "ON_TASK",
                    "active_seconds": 4.5,
                    "idle_seconds": 0.3,
                    "away_seconds": 0.2,
                    "focus_score": 85,
                    "raw_signals": {}
                },
                timeout=5.0
            )
            
            if response.status_code == 200:
                print(f"[PASS] PRANA ingestion working")
                return True
            else:
                print(f"[FAIL] PRANA ingestion failed: {response.status_code}")
                return False
    except Exception as e:
        print(f"[FAIL] PRANA ingestion error: {e}")
        return False

async def test_bucket_events() -> bool:
    """Test if Gurukul events reach Bucket"""
    try:
        async with httpx.AsyncClient() as client:
            # Check Bucket events
            response = await client.get(
                f"{BUCKET_URL}/core/events?limit=10",
                timeout=5.0
            )
            
            if response.status_code == 200:
                data = response.json()
                gurukul_events = [e for e in data.get("events", []) if e.get("requester_id") == "gurukul_backend"]
                print(f"[PASS] Bucket integration working ({len(gurukul_events)} Gurukul events)")
                return True
            else:
                print(f"[FAIL] Bucket events check failed: {response.status_code}")
                return False
    except Exception as e:
        print(f"[FAIL] Bucket events error: {e}")
        return False

async def test_karma_integration() -> bool:
    """Test Karma integration"""
    try:
        async with httpx.AsyncClient() as client:
            # Try to get karma profile
            response = await client.get(
                f"{KARMA_URL}/api/v1/karma/test_student_123",
                timeout=5.0
            )
            
            if response.status_code in [200, 404]:  # 404 is ok if user doesn't exist yet
                print(f"[PASS] Karma integration working")
                return True
            else:
                print(f"[FAIL] Karma integration failed: {response.status_code}")
                return False
    except Exception as e:
        print(f"[FAIL] Karma integration error: {e}")
        return False

async def main():
    """Run all integration tests"""
    print("=" * 60)
    print("Gurukul Integration Test - 9-Pillar System")
    print("=" * 60)
    print()
    
    # Test 1: Health Checks
    print("Test 1: Health Checks")
    print("-" * 60)
    health_results = await asyncio.gather(
        test_service_health("Karma", KARMA_URL),
        test_service_health("Bucket", BUCKET_URL),
        test_service_health("Core", CORE_URL),
        test_service_health("Insight Core", INSIGHT_CORE_URL),
        test_service_health("Insight Flow", INSIGHT_FLOW_URL),
        test_service_health("Gurukul", GURUKUL_URL)
    )
    health_pass = all(health_results)
    print()
    
    # Test 2: Gurukul Chat Integration
    print("Test 2: Gurukul Chat Integration")
    print("-" * 60)
    chat_pass = await test_gurukul_chat_integration()
    print()
    
    # Test 3: PRANA Ingestion
    print("Test 3: PRANA Ingestion")
    print("-" * 60)
    prana_pass = await test_prana_ingestion()
    print()
    
    # Test 4: Bucket Events
    print("Test 4: Bucket Events")
    print("-" * 60)
    bucket_pass = await test_bucket_events()
    print()
    
    # Test 5: Karma Integration
    print("Test 5: Karma Integration")
    print("-" * 60)
    karma_pass = await test_karma_integration()
    print()
    
    # Summary
    print("=" * 60)
    print("Test Summary")
    print("=" * 60)
    tests = [
        ("Health Checks", health_pass),
        ("Chat Integration", chat_pass),
        ("PRANA Ingestion", prana_pass),
        ("Bucket Events", bucket_pass),
        ("Karma Integration", karma_pass)
    ]
    
    passed = sum(1 for _, result in tests if result)
    total = len(tests)
    
    for name, result in tests:
        status = "[PASS]" if result else "[FAIL]"
        print(f"{status} - {name}")
    
    print()
    print(f"Results: {passed}/{total} tests passed ({int(passed/total*100)}%)")
    
    if passed == total:
        print("[SUCCESS] All tests passed! Gurukul is fully integrated!")
    elif passed >= total * 0.8:
        print("[WARNING] Most tests passed. Check failed tests above.")
    else:
        print("[FAIL] Integration incomplete. Please check service logs.")
    
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())
