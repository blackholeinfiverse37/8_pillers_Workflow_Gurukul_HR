# Karma Service Timezone Fix

## Issue
Karma service returning 500 error: "can't subtract offset-naive and offset-aware datetimes"

## Root Cause
In `karma_chain_v2-main/utils/tokens.py`, the `apply_decay_and_expiry()` function was comparing timezone-aware datetime (`now_utc()`) with timezone-naive datetime from database (`last_decay` and `created_at`).

## Fix Applied
Updated `utils/tokens.py` to ensure all datetime objects are timezone-aware before comparison:

```python
# Line 22-27: Fix last_decay comparison
if last_decay.tzinfo is None:
    last_decay = last_decay.replace(tzinfo=timezone.utc)

# Line 37-42: Fix created_at comparison  
if created.tzinfo is None:
    created = created.replace(tzinfo=timezone.utc)
```

## Action Required
**RESTART KARMA SERVICE** to load the fix:

```bash
# Stop current Karma service (Ctrl+C in terminal)
# Then restart:
cd "karma_chain_v2-main"
python main.py
```

## Verification
After restart, test the endpoint:
```bash
curl http://localhost:8000/api/v1/karma/test_student_123
```

Expected: Either 404 (user not found) or 200 (user profile) - NOT 500 error

## Integration Test
Run the full integration test:
```bash
python test_gurukul_integration.py
```

Expected: 5/5 tests passing (100%)

---

**Status**: Fix applied, awaiting Karma service restart
**File Modified**: `karma_chain_v2-main/utils/tokens.py`
**Lines Changed**: 22-27, 37-42
