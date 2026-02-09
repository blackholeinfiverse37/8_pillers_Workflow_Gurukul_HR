"""
HR Platform Integration Test
Tests connectivity with 9-Pillar system (Bucket, Karma, Core)
"""
import asyncio
import httpx
from datetime import datetime

# Color codes for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

async def test_service_health(name: str, url: str) -> bool:
    """Test if a service is healthy"""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(url)
            if response.status_code == 200:
                print(f"{GREEN}✓{RESET} {name:30} - HEALTHY")
                return True
            else:
                print(f"{RED}✗{RESET} {name:30} - UNHEALTHY (Status: {response.status_code})")
                return False
    except Exception as e:
        print(f"{RED}✗{RESET} {name:30} - NOT RUNNING ({str(e)[:50]})")
        return False

async def test_bucket_event_logging() -> bool:
    """Test event logging to Bucket"""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            payload = {
                "event_type": "hr_test_event",
                "event_data": {
                    "test": "integration_test",
                    "timestamp": datetime.now().isoformat()
                },
                "source": "hr_platform_test"
            }
            response = await client.post(
                "http://localhost:8001/events",
                json=payload
            )
            if response.status_code == 200:
                print(f"{GREEN}✓{RESET} Bucket Event Logging      - WORKING")
                return True
            else:
                print(f"{RED}✗{RESET} Bucket Event Logging      - FAILED (Status: {response.status_code})")
                return False
    except Exception as e:
        print(f"{RED}✗{RESET} Bucket Event Logging      - FAILED ({str(e)[:50]})")
        return False

async def test_karma_action_tracking() -> bool:
    """Test action tracking in Karma"""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            payload = {
                "user_id": "test_hr_user",
                "action_type": "hr_test_action",
                "action_data": {
                    "test": "integration_test",
                    "timestamp": datetime.now().isoformat()
                },
                "source": "hr_platform_test"
            }
            response = await client.post(
                "http://localhost:8000/actions",
                json=payload
            )
            if response.status_code == 200:
                print(f"{GREEN}✓{RESET} Karma Action Tracking     - WORKING")
                return True
            else:
                print(f"{RED}✗{RESET} Karma Action Tracking     - FAILED (Status: {response.status_code})")
                return False
    except Exception as e:
        print(f"{RED}✗{RESET} Karma Action Tracking     - FAILED ({str(e)[:50]})")
        return False

async def main():
    """Run all integration tests"""
    print("\n" + "="*80)
    print(f"{BLUE}HR PLATFORM 9-PILLAR INTEGRATION TEST{RESET}")
    print("="*80 + "\n")
    
    results = []
    
    # Test HR Platform Services
    print(f"{YELLOW}▶ HR Platform Services{RESET}")
    results.append(await test_service_health("HR Gateway (8009)", "http://localhost:8009/health"))
    results.append(await test_service_health("HR Agent (9000)", "http://localhost:9000/health"))
    results.append(await test_service_health("HR LangGraph (9001)", "http://localhost:9001/health"))
    
    print(f"\n{YELLOW}▶ 9-Pillar Core Services{RESET}")
    results.append(await test_service_health("Karma (8000)", "http://localhost:8000/health"))
    results.append(await test_service_health("Bucket (8001)", "http://localhost:8001/health"))
    results.append(await test_service_health("Core (8002)", "http://localhost:8002/health"))
    
    print(f"\n{YELLOW}▶ Integration Tests{RESET}")
    results.append(await test_bucket_event_logging())
    results.append(await test_karma_action_tracking())
    
    # Summary
    print("\n" + "="*80)
    passed = sum(results)
    total = len(results)
    percentage = (passed / total * 100) if total > 0 else 0
    
    if passed == total:
        print(f"{GREEN}✓ ALL TESTS PASSED{RESET} - {passed}/{total} ({percentage:.0f}%)")
        print(f"{GREEN}HR Platform is fully integrated with 9-Pillar system!{RESET}")
    else:
        print(f"{YELLOW}⚠ PARTIAL SUCCESS{RESET} - {passed}/{total} ({percentage:.0f}%)")
        print(f"{YELLOW}Some services are not running or integration failed{RESET}")
    
    print("="*80 + "\n")
    
    return passed == total

if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)
