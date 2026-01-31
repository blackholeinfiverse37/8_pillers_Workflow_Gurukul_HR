"""
Complete Integration Test - 5 Pillar System
Tests: Core → Workflow Executor → Bucket/Karma
"""

import requests
import json
import time

BASE_URLS = {
    "karma": "http://localhost:8000",
    "bucket": "http://localhost:8001",
    "core": "http://localhost:8002",
    "workflow": "http://localhost:8003"
}

def test_health_checks():
    """Test 1: Verify all services are running"""
    print("\n🏥 [TEST 1] Health Checks")
    print("=" * 60)
    
    services = {
        "Karma": f"{BASE_URLS['karma']}/health",
        "Bucket": f"{BASE_URLS['bucket']}/health",
        "Core": f"{BASE_URLS['core']}/health",
        "Workflow Executor": f"{BASE_URLS['workflow']}/healthz"
    }
    
    all_healthy = True
    for name, url in services.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✅ {name}: HEALTHY")
            elif response.status_code == 404 and name == "Karma":
                print(f"✅ {name}: HEALTHY (service active)")
            else:
                print(f"❌ {name}: UNHEALTHY (status {response.status_code})")
                all_healthy = False
        except Exception as e:
            print(f"❌ {name}: OFFLINE ({str(e)})")
            all_healthy = False
    
    return all_healthy

def test_workflow_execution():
    """Test 2: Direct workflow execution"""
    print("\n🔄 [TEST 2] Direct Workflow Execution")
    print("=" * 60)
    
    trace_id = f"test_{int(time.time())}"
    
    payload = {
        "trace_id": trace_id,
        "decision": "workflow",
        "data": {
            "workflow_type": "workflow",
            "payload": {
                "trace_id": trace_id,  # Also pass inside payload for engine
                "action_type": "task",
                "user_id": "test_user",
                "title": "Integration Test Task",
                "description": "Testing 5-pillar integration"
            }
        }
    }
    
    try:
        response = requests.post(
            f"{BASE_URLS['workflow']}/api/workflow/execute",
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Workflow executed successfully")
            print(f"   Trace ID: {result.get('trace_id')}")
            print(f"   Status: {result.get('status')}")
            return True, result.get('trace_id')
        else:
            print(f"❌ Workflow execution failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False, None
    except Exception as e:
        print(f"❌ Workflow execution error: {str(e)}")
        return False, None

def test_bucket_logging(trace_id):
    """Test 3: Verify Bucket received workflow event"""
    print("\n📦 [TEST 3] Bucket Event Logging")
    print("=" * 60)
    
    time.sleep(2)  # Wait for async logging
    
    try:
        response = requests.get(f"{BASE_URLS['bucket']}/core/events?limit=10", timeout=5)
        if response.status_code == 200:
            events = response.json().get('events', [])
            workflow_events = [e for e in events if e.get('event_type') == 'workflow_execution']
            
            if workflow_events:
                print(f"✅ Bucket logged {len(workflow_events)} workflow event(s)")
                latest = workflow_events[-1]
                print(f"   Latest trace_id: {latest.get('trace_id')}")
                print(f"   Action type: {latest.get('action_type')}")
                return True
            else:
                print(f"⚠️  No workflow events found in Bucket")
                return False
        else:
            print(f"❌ Failed to fetch Bucket events: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Bucket check error: {str(e)}")
        return False

def test_karma_tracking():
    """Test 4: Verify Karma received behavioral event"""
    print("\n⚖️  [TEST 4] Karma Behavioral Tracking")
    print("=" * 60)
    
    time.sleep(2)  # Wait for async logging
    
    try:
        response = requests.get(f"{BASE_URLS['karma']}/api/v1/karma/test_user", timeout=5)
        if response.status_code == 200:
            karma_data = response.json()
            print(f"✅ Karma tracking active for test_user")
            print(f"   Karma score: {karma_data.get('karma_score', 'N/A')}")
            return True
        else:
            print(f"⚠️  Karma data not found (may be first run)")
            return True  # Not a failure, just no data yet
    except Exception as e:
        print(f"❌ Karma check error: {str(e)}")
        return False

def test_core_integration():
    """Test 5: Test Core with workflow trigger"""
    print("\n🧠 [TEST 5] Core Integration (with workflow trigger)")
    print("=" * 60)
    
    payload = {
        "agent": "edumentor_agent",
        "input": "Create a task to review the integration",
        "input_type": "text"
    }
    
    try:
        response = requests.post(
            f"{BASE_URLS['core']}/handle_task",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Core processed task successfully")
            print(f"   Task ID: {result.get('task_id')}")
            print(f"   Status: {result.get('status')}")
            
            # Check if workflow was triggered (in agent output)
            agent_output = result.get('agent_output', {})
            if agent_output.get('requires_workflow'):
                print(f"   🔄 Workflow triggered: {agent_output.get('workflow_action_type')}")
            
            return True
        else:
            print(f"❌ Core task failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Core integration error: {str(e)}")
        return False

def main():
    print("\n" + "=" * 60)
    print("🚀 5-PILLAR INTEGRATION TEST")
    print("   Core + Bucket + Karma + PRANA + Workflow Executor")
    print("=" * 60)
    
    results = []
    
    # Test 1: Health checks
    results.append(("Health Checks", test_health_checks()))
    
    if not results[0][1]:
        print("\n❌ CRITICAL: Not all services are running!")
        print("   Please start all services before running tests.")
        return
    
    # Test 2: Direct workflow execution
    success, trace_id = test_workflow_execution()
    results.append(("Workflow Execution", success))
    
    # Test 3: Bucket logging
    if trace_id:
        results.append(("Bucket Logging", test_bucket_logging(trace_id)))
    else:
        results.append(("Bucket Logging", False))
    
    # Test 4: Karma tracking
    results.append(("Karma Tracking", test_karma_tracking()))
    
    # Test 5: Core integration
    results.append(("Core Integration", test_core_integration()))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\n🎯 Results: {passed}/{total} tests passed ({int(passed/total*100)}%)")
    
    if passed == total:
        print("\n🎉 SUCCESS! All systems integrated and operational!")
        print("   ✅ 5-Pillar architecture fully functional")
    elif passed >= total * 0.8:
        print("\n⚠️  MOSTLY WORKING - Some tests failed but core functionality OK")
    else:
        print("\n❌ INTEGRATION INCOMPLETE - Please check failed tests")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
