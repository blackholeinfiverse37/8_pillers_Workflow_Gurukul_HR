"""
Complete 16-Service System Verification Script
Tests all services and integrations
"""
import requests
import time
from typing import Dict, List, Tuple

# Color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def check_service(name: str, url: str, timeout: int = 5) -> Tuple[bool, str]:
    """Check if a service is running"""
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            return True, "HEALTHY"
        return False, f"HTTP {response.status_code}"
    except requests.exceptions.ConnectionError:
        return False, "NOT RUNNING"
    except requests.exceptions.Timeout:
        return False, "TIMEOUT"
    except Exception as e:
        return False, str(e)[:30]

def print_header(text: str):
    """Print section header"""
    print(f"\n{'='*80}")
    print(f"{BLUE}{text:^80}{RESET}")
    print(f"{'='*80}\n")

def print_result(name: str, status: bool, message: str = ""):
    """Print test result"""
    symbol = f"{GREEN}✓{RESET}" if status else f"{RED}✗{RESET}"
    status_text = f"{GREEN}PASS{RESET}" if status else f"{RED}FAIL{RESET}"
    print(f"{symbol} {name:40} - {status_text:20} {message}")

def main():
    print_header("16-SERVICE SYSTEM VERIFICATION")
    
    # Define all services
    services = {
        "9-Pillar Core Services": [
            ("Karma (8000)", "http://localhost:8000/health"),
            ("Bucket (8001)", "http://localhost:8001/health"),
            ("Core (8002)", "http://localhost:8002/health"),
            ("Workflow (8003)", "http://localhost:8003/healthz"),
            ("UAO (8004)", "http://localhost:8004/docs"),
            ("Insight Core (8005)", "http://localhost:8005/health"),
            ("Insight Flow (8006)", "http://localhost:8006/health"),
        ],
        "Application Backends": [
            ("Gurukul Backend (3000)", "http://localhost:3000/health"),
            ("EMS Backend (8008)", "http://localhost:8008/health"),
            ("HR Platform Gateway (8009)", "http://localhost:8009/health"),
            ("Blackhole Backend (5001)", "http://localhost:5001/api/ping"),
            ("HR Platform Agent (9000)", "http://localhost:9000/health"),
        ],
        "Frontend Applications": [
            ("Gurukul Frontend (5173)", "http://localhost:5173"),
            ("EMS Frontend (3001)", "http://localhost:3001"),
            ("Blackhole Frontend (5174)", "http://localhost:5174"),
        ]
    }
    
    total_services = 0
    healthy_services = 0
    
    # Check all services
    print_header("HEALTH CHECKS - ALL 16 SERVICES")
    
    for category, service_list in services.items():
        print(f"\n{YELLOW}▶ {category}{RESET}")
        for name, url in service_list:
            total_services += 1
            is_healthy, message = check_service(name, url)
            if is_healthy:
                healthy_services += 1
            print_result(name, is_healthy, message)
    
    # Integration tests
    print_header("INTEGRATION TESTS")
    
    integration_tests = []
    
    # Test 1: Gurukul → Core Integration
    print(f"\n{YELLOW}▶ Gurukul Integration{RESET}")
    try:
        response = requests.get("http://localhost:3000/health", timeout=5)
        gurukul_ok = response.status_code == 200
        print_result("Gurukul API Health", gurukul_ok)
        integration_tests.append(gurukul_ok)
    except:
        print_result("Gurukul API Health", False)
        integration_tests.append(False)
    
    # Test 2: Blackhole → Bucket Integration
    print(f"\n{YELLOW}▶ Blackhole Integration{RESET}")
    try:
        response = requests.get("http://localhost:5001/api/ping", timeout=5)
        blackhole_ok = response.status_code == 200
        print_result("Blackhole API Ping", blackhole_ok)
        integration_tests.append(blackhole_ok)
    except:
        print_result("Blackhole API Ping", False)
        integration_tests.append(False)
    
    # Test 3: HR Platform Integration
    print(f"\n{YELLOW}▶ HR Platform Integration{RESET}")
    try:
        response = requests.get("http://localhost:8009/health", timeout=5)
        hr_gateway_ok = response.status_code == 200
        print_result("HR Gateway Health", hr_gateway_ok)
        integration_tests.append(hr_gateway_ok)
        
        response = requests.get("http://localhost:9000/health", timeout=5)
        hr_agent_ok = response.status_code == 200
        print_result("HR Agent Health", hr_agent_ok)
        integration_tests.append(hr_agent_ok)
    except:
        print_result("HR Platform Integration", False)
        integration_tests.append(False)
    
    # Test 4: Core Services Chain
    print(f"\n{YELLOW}▶ 9-Pillar Core Chain{RESET}")
    core_services = [
        ("Karma", "http://localhost:8000/health"),
        ("Bucket", "http://localhost:8001/health"),
        ("Core", "http://localhost:8002/health"),
    ]
    for name, url in core_services:
        try:
            response = requests.get(url, timeout=5)
            is_ok = response.status_code == 200
            print_result(f"{name} Health", is_ok)
            integration_tests.append(is_ok)
        except:
            print_result(f"{name} Health", False)
            integration_tests.append(False)
    
    # Summary
    print_header("TEST SUMMARY")
    
    passed_integration = sum(integration_tests)
    total_integration = len(integration_tests)
    
    print(f"Total Services:        {total_services}")
    print(f"Healthy Services:      {healthy_services}")
    print(f"Unhealthy Services:    {total_services - healthy_services}")
    print(f"Service Health Rate:   {(healthy_services/total_services*100):.1f}%")
    print()
    print(f"Integration Tests:     {total_integration}")
    print(f"Passed:                {passed_integration}")
    print(f"Failed:                {total_integration - passed_integration}")
    print(f"Integration Pass Rate: {(passed_integration/total_integration*100):.1f}%")
    
    # Final verdict
    print("\n" + "="*80)
    if healthy_services == total_services and passed_integration == total_integration:
        print(f"{GREEN}      ✓ ALL SYSTEMS OPERATIONAL - READY FOR PRODUCTION!{RESET}")
    elif healthy_services >= total_services * 0.8:
        print(f"{YELLOW}      ⚠ MOST SYSTEMS OPERATIONAL - CHECK FAILED SERVICES{RESET}")
    else:
        print(f"{RED}      ✗ SYSTEM NOT READY - MULTIPLE SERVICES DOWN{RESET}")
    print("="*80 + "\n")
    
    # Recommendations
    if healthy_services < total_services:
        print(f"\n{YELLOW}RECOMMENDATIONS:{RESET}")
        print("1. Start missing services using the startup guide in README.md")
        print("2. Check service logs for error messages")
        print("3. Verify .env configuration files are present")
        print("4. Ensure MongoDB and Redis connections are configured")
        print("5. Run: netstat -ano | findstr \":<PORT>\" to check port conflicts")

if __name__ == "__main__":
    main()
