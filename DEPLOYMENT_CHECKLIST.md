# ⚡ Quick Deployment Checklist - BHIV Core on Render

## Pre-Deployment (15 minutes)

- [ ] **MongoDB Atlas Setup**
  - [ ] Create free cluster
  - [ ] Create database user
  - [ ] Whitelist all IPs (0.0.0.0/0)
  - [ ] Copy connection string
  - [ ] Test connection locally

- [ ] **Qdrant Setup** (Optional)
  - [ ] Create Qdrant Cloud account
  - [ ] Create cluster
  - [ ] Copy API endpoint and key
  - [ ] OR set `QDRANT_URLS=disabled`

- [ ] **GitHub Repository**
  - [ ] Push Core code to GitHub
  - [ ] Verify `render.yaml` exists
  - [ ] Verify `runtime.txt` exists
  - [ ] Verify `requirements.txt` exists

## Render Setup (10 minutes)

- [ ] **Create Web Service**
  - [ ] Sign up/login to Render
  - [ ] Connect GitHub repository
  - [ ] Name: `bhiv-core`
  - [ ] Region: Oregon (US West)
  - [ ] Branch: `main`
  - [ ] Build: `pip install -r requirements.txt`
  - [ ] Start: `python mcp_bridge.py`
  - [ ] Instance: Starter ($7/month) or Free

- [ ] **Environment Variables**
  ```
  PORT=10000
  ENVIRONMENT=production
  MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/bhiv_core_db
  USE_RL=true
  RL_EXPLORATION_RATE=0.2
  QDRANT_URLS=https://xxxxx.qdrant.io
  QDRANT_API_KEY=your_key
  BUCKET_URL=http://localhost:8001
  KARMA_URL=http://localhost:8000
  ```

- [ ] **Health Check**
  - [ ] Path: `/health`
  - [ ] Interval: 30 seconds

## Deploy & Verify (5 minutes)

- [ ] **Deploy**
  - [ ] Click "Create Web Service"
  - [ ] Wait for build (2-5 min)
  - [ ] Wait for deploy (30 sec)
  - [ ] Check logs for errors

- [ ] **Test Endpoints**
  ```bash
  # Health check
  curl https://your-service.onrender.com/health
  
  # Task processing
  curl -X POST https://your-service.onrender.com/handle_task \
    -H "Content-Type: application/json" \
    -d '{"agent":"edumentor_agent","input":"test","input_type":"text"}'
  ```

## Post-Deployment (5 minutes)

- [ ] **Configure**
  - [ ] Enable auto-deploy
  - [ ] Set up notifications (email/Slack)
  - [ ] Add custom domain (optional)

- [ ] **Monitor**
  - [ ] Check logs for errors
  - [ ] Monitor CPU/memory usage
  - [ ] Set up external monitoring (UptimeRobot)

## Total Time: ~35 minutes

---

## Quick Commands

### Test Health
```bash
curl https://your-service.onrender.com/health
```

### Test Task
```bash
curl -X POST https://your-service.onrender.com/handle_task \
  -H "Content-Type: application/json" \
  -d '{"agent":"edumentor_agent","input":"What is AI?","input_type":"text"}'
```

### View Logs
```bash
# In Render dashboard: Logs tab
# Or use Render CLI:
render logs -s bhiv-core
```

### Redeploy
```bash
# Push to GitHub (if auto-deploy enabled)
git push origin main

# Or manual deploy in Render dashboard
```

---

## Troubleshooting Quick Fixes

**Build fails**: Check `requirements.txt` has all dependencies
**Service crashes**: Check MongoDB connection string
**Timeout**: Upgrade to Starter plan or optimize code
**Memory error**: Upgrade instance type

---

## Cost Summary

- **Free**: $0/month (testing only, spins down)
- **Starter**: $7/month (production, always on)
- **Standard**: $25/month (high traffic)

Plus MongoDB Atlas:
- **Free**: $0/month (512MB, good for dev)
- **M10**: $57/month (production)

---

## Support

- Render Docs: https://render.com/docs
- MongoDB Docs: https://docs.atlas.mongodb.com
- GitHub Issues: Create issue in your repo

---

✅ **Deployment Complete!**
