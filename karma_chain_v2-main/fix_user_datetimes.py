"""
Fix timezone-naive datetimes in existing Karma MongoDB users
"""
from datetime import datetime, timezone
from database import users_col
import sys

def fix_user_datetimes():
    """Fix all users with timezone-naive datetimes"""
    print("Fixing timezone-naive datetimes in Karma database...")
    
    try:
        # Get all users
        users = list(users_col.find({}))
        print(f"Found {len(users)} users to check")
        
        fixed_count = 0
        for user in users:
            updates = {}
            
            # Fix last_decay
            if "last_decay" in user:
                last_decay = user["last_decay"]
                if isinstance(last_decay, datetime) and last_decay.tzinfo is None:
                    updates["last_decay"] = last_decay.replace(tzinfo=timezone.utc)
                    print(f"  Fixing last_decay for user {user['user_id']}")
            
            # Fix token_meta created_at and last_update
            if "token_meta" in user:
                token_meta = user["token_meta"]
                for token, meta in token_meta.items():
                    if isinstance(meta, dict):
                        if "created_at" in meta:
                            created_at = meta["created_at"]
                            if isinstance(created_at, datetime) and created_at.tzinfo is None:
                                if "token_meta" not in updates:
                                    updates["token_meta"] = token_meta.copy()
                                updates["token_meta"][token]["created_at"] = created_at.replace(tzinfo=timezone.utc)
                                print(f"  Fixing token_meta.{token}.created_at for user {user['user_id']}")
                        
                        if "last_update" in meta:
                            last_update = meta["last_update"]
                            if isinstance(last_update, datetime) and last_update.tzinfo is None:
                                if "token_meta" not in updates:
                                    updates["token_meta"] = token_meta.copy()
                                updates["token_meta"][token]["last_update"] = last_update.replace(tzinfo=timezone.utc)
                                print(f"  Fixing token_meta.{token}.last_update for user {user['user_id']}")
            
            # Apply updates if any
            if updates:
                users_col.update_one(
                    {"user_id": user["user_id"]},
                    {"$set": updates}
                )
                fixed_count += 1
                print(f"✅ Fixed user {user['user_id']}")
        
        print(f"\n✅ Fixed {fixed_count} users with timezone issues")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing datetimes: {e}")
        return False

if __name__ == "__main__":
    success = fix_user_datetimes()
    sys.exit(0 if success else 1)
