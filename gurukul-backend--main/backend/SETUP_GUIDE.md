# Gurukul Backend Setup Guide

## Quick Setup

### 1. Copy Environment File
```bash
cd backend
cp .env.example .env
```

### 2. Configure Required Variables

Edit `.env` and set these **required** values:

```env
# Required: Get from https://console.groq.com
GROQ_API_KEY=gsk_your_actual_groq_api_key_here

# Required: Change to a secure random string
JWT_SECRET_KEY=your-secure-random-string-here
```

### 3. Optional: Configure Integration URLs

If running the full 9-pillar system, these are already set correctly:
```env
CORE_URL=http://localhost:8002
BUCKET_URL=http://localhost:8001
KARMA_URL=http://localhost:8000
INSIGHT_CORE_URL=http://localhost:8005
INSIGHT_FLOW_URL=http://localhost:8006
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Start Server
```bash
python -m app.main
```

Server will run on: http://localhost:3000

---

## Configuration Details

### Database
- **Default**: SQLite (no setup needed)
- **PostgreSQL**: Change `DATABASE_URL` to `postgresql://user:password@localhost:5432/gurukul`

### API Keys

#### Groq (Required for AI Chat)
1. Sign up at https://console.groq.com
2. Create API key
3. Set `GROQ_API_KEY` in `.env`

#### YouTube (Optional)
1. Get API key from Google Cloud Console
2. Set `YOUTUBE_API_KEY` in `.env`

#### OpenAI/Gemini (Optional)
- Only needed if using those providers
- Set respective API keys in `.env`

### Integration Features

#### Enable/Disable Integrations
```env
ENABLE_CORE_INTEGRATION=true    # AI routing through Core
ENABLE_BUCKET_INTEGRATION=true  # Event logging to Bucket
ENABLE_KARMA_INTEGRATION=true   # Student tracking in Karma
```

Set to `false` to disable any integration (Gurukul will work standalone).

### Redis (Optional)
- Only needed for PRANA packet queuing
- If not configured, uses in-memory queue
- Set `REDIS_HOST`, `REDIS_PORT`, `REDIS_PASSWORD` if using

---

## Verification

### Test Configuration
```bash
# Check if server starts
python -m app.main

# In another terminal, test health endpoint
curl http://localhost:3000/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "Gurukul Backend API"
}
```

### Test Integration (if 9-pillar system running)
```bash
# Test chat with Core integration
curl -X POST http://localhost:3000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello", "use_core": true}'
```

---

## Troubleshooting

### "GROQ_API_KEY not set"
- Make sure `.env` file exists in `backend/` directory
- Check that `GROQ_API_KEY` is set in `.env`
- Restart the server after changing `.env`

### "Database connection failed"
- Default SQLite should work without setup
- Check `DATABASE_URL` is correct
- Ensure write permissions in backend directory

### "Integration services unavailable"
- This is normal if 9-pillar system not running
- Gurukul will work standalone with local AI
- Set `ENABLE_*_INTEGRATION=false` to disable warnings

---

## Production Deployment

### Security Checklist
- [ ] Change `JWT_SECRET_KEY` to a strong random string
- [ ] Set `ENV=production`
- [ ] Use PostgreSQL instead of SQLite
- [ ] Enable HTTPS
- [ ] Set proper CORS origins
- [ ] Secure API keys (use secrets manager)
- [ ] Enable rate limiting

### Environment Variables for Production
```env
ENV=production
DATABASE_URL=postgresql://user:password@host:5432/gurukul
JWT_SECRET_KEY=use-a-very-long-random-string-here
CORS_ORIGINS=https://yourdomain.com
```

---

## Need Help?

- Check logs in terminal where server is running
- Review `README_9_PILLAR.md` for full system setup
- Test individual services with health checks
