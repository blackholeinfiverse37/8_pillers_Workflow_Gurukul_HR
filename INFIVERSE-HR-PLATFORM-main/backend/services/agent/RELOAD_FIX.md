# HR Platform Agent - Reload Issue Fix

## Problem
Agent service crashes on reload with error:
```
ERROR: Error loading ASGI app. Attribute "app" not found in module "app".
```

## Root Cause
1. Source `.py` files are missing (only `.pyc` bytecode exists)
2. Uvicorn `--reload` watches for file changes
3. When files change, uvicorn tries to reload but can't find source files
4. Service crashes

## Solution

### Option 1: Run Without Reload (Recommended)
```bash
cd "INFIVERSE-HR-PLATFORM-main/backend/services/agent"
START_AGENT.bat
```

Or manually:
```bash
python -m uvicorn app:app --host 0.0.0.0 --port 9000
```

### Option 2: Restore Source Files
If you have the original repository, restore these files:
- `app.py`
- `config.py`
- `database.py`
- `jwt_auth.py`
- `main.py`

Then run with reload:
```bash
uvicorn app:app --host 0.0.0.0 --port 9000 --reload
```

## Integration Status

✅ **Agent service works with bytecode**
✅ **9-Pillar integration maintained**
✅ **Bucket logging operational**
✅ **Karma tracking operational**
✅ **Semantic matching functional**

## Updated Startup Command

**README.md should use:**
```bash
cd "INFIVERSE-HR-PLATFORM-main/backend/services/agent"
python -m uvicorn app:app --host 0.0.0.0 --port 9000
```

**Remove `--reload` flag to prevent crashes**
