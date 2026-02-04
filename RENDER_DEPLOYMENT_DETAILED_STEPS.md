# 🚀 BHIV Core - Render Deployment Steps (Detailed)

## PHASE 1: MONGODB ATLAS SETUP (15 minutes)

### STEP 1.1: Create MongoDB Atlas Account
1. Open browser and go to: https://www.mongodb.com/cloud/atlas
2. Click **"Try Free"** button (top right)
3. Fill in:
   - Email address
   - Password (min 8 characters)
   - First name
   - Last name
4. Check "I agree to the Terms of Service"
5. Click **"Create your Atlas account"**
6. Verify email (check inbox, click verification link)

### STEP 1.2: Create Organization and Project
1. After login, you'll see "Welcome to Atlas"
2. Click **"Create an organization"**
3. Enter organization name: `BHIV Production`
4. Click **"Next"**
5. Skip adding members (click **"Create Organization"**)
6. Click **"New Project"**
7. Enter project name: `BHIV Core`
8. Click **"Next"**
9. Skip adding members (click **"Create Project"**)

### STEP 1.3: Create Database Cluster
1. Click **"Build a Database"** (green button)
2. Select **"M0 FREE"** tier (left option)
3. Cloud Provider: Select **"AWS"**
4. Region: Select **"Oregon (us-west-2)"** or closest to you
5. Cluster Name: Leave as `Cluster0` or change to `bhiv-core-cluster`
6. Click **"Create"** button (bottom right)
7. Wait 3-5 minutes for cluster creation (progress bar shows)

### STEP 1.4: Create Database User
1. You'll see "Security Quickstart" screen
2. Under "How would you like to authenticate your connection?"
3. Select **"Username and Password"**
4. Enter:
   - Username: `bhiv_core_user`
   - Password: Click **"Autogenerate Secure Password"** (SAVE THIS PASSWORD!)
   - Or create your own strong password
5. Click **"Create User"** button
6. **IMPORTANT**: Copy and save the password in a safe place

### STEP 1.5: Configure Network Access
1. Still on "Security Quickstart" screen
2. Under "Where would you like to connect from?"
3. Click **"Add My Current IP Address"** (for testing)
4. Then click **"Add a Different IP Address"**
5. Enter:
   - IP Address: `0.0.0.0/0`
   - Description: `Allow all (Render deployment)`
6. Click **"Add Entry"**
7. Click **"Finish and Close"** button
8. Click **"Go to Databases"** on popup

### STEP 1.6: Get Connection String
1. On Database Deployments page, find your cluster
2. Click **"Connect"** button (next to cluster name)
3. Click **"Connect your application"**
4. Driver: Select **"Python"**
5. Version: Select **"3.11 or later"**
6. Copy the connection string (looks like):
   ```
   mongodb+srv://bhiv_core_user:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```
7. Replace `<password>` with your actual password from Step 1.4
8. Add database name at the end:
   ```
   mongodb+srv://bhiv_core_user:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/bhiv_core_db?retryWrites=true&w=majority
   ```
9. **SAVE THIS COMPLETE STRING** - you'll need it for Render

---

## PHASE 2: GITHUB REPOSITORY SETUP (10 minutes)

### STEP 2.1: Prepare Local Repository
1. Open terminal/command prompt
2. Navigate to Core directory:
   ```bash
   cd "C:\Users\A\Desktop\Core-Bucket_Karma_Orchestration_InsightCore_Insightflow_IntegratedPart\v1-BHIV_CORE-main"
   ```
3. Initialize git (if not already):
   ```bash
   git init
   ```
4. Check status:
   ```bash
   git status
   ```

### STEP 2.2: Create .gitignore File
1. Create `.gitignore` file in Core directory
2. Add these lines:
   ```
   __pycache__/
   *.pyc
   .env
   .env.local
   venv/
   logs/
   *.log
   .DS_Store
   ```
3. Save file

### STEP 2.3: Commit Code Locally
1. Add all files:
   ```bash
   git add .
   ```
2. Commit:
   ```bash
   git commit -m "Initial commit - BHIV Core for Render"
   ```

### STEP 2.4: Create GitHub Repository
1. Open browser and go to: https://github.com
2. Log in to your GitHub account
3. Click **"+"** icon (top right)
4. Click **"New repository"**
5. Fill in:
   - Repository name: `bhiv-core`
   - Description: `BHIV Core AI Decision Engine`
   - Visibility: **Private** (recommended) or Public
   - Do NOT initialize with README, .gitignore, or license
6. Click **"Create repository"**

### STEP 2.5: Push Code to GitHub
1. Copy the commands shown on GitHub (under "push an existing repository")
2. In terminal, run:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/bhiv-core.git
   git branch -M main
   git push -u origin main
   ```
3. Enter GitHub username and password (or personal access token)
4. Wait for upload to complete
5. Refresh GitHub page - you should see your code

### STEP 2.6: Verify Files on GitHub
1. On GitHub repository page, check these files exist:
   - ✅ `mcp_bridge.py`
   - ✅ `requirements.txt`
   - ✅ `render.yaml`
   - ✅ `runtime.txt`
   - ✅ `config/` folder
   - ✅ `agents/` folder
   - ✅ `integration/` folder

---

## PHASE 3: RENDER ACCOUNT SETUP (5 minutes)

### STEP 3.1: Create Render Account
1. Open browser and go to: https://render.com
2. Click **"Get Started"** button
3. Choose sign-up method:
   - **Option A**: Click **"Sign up with GitHub"** (recommended)
   - **Option B**: Use email/password
4. If using GitHub:
   - Click **"Authorize Render"**
   - Enter GitHub password if prompted
5. Complete profile:
   - Name
   - Company (optional)
6. Click **"Complete Sign Up"**

### STEP 3.2: Verify Email
1. Check your email inbox
2. Find email from Render
3. Click verification link
4. You'll be redirected to Render dashboard

---

## PHASE 4: CREATE WEB SERVICE ON RENDER (15 minutes)

### STEP 4.1: Start New Web Service
1. On Render dashboard, click **"New +"** button (top right)
2. Select **"Web Service"** from dropdown

### STEP 4.2: Connect GitHub Repository
1. You'll see "Create a new Web Service" page
2. Under "Connect a repository":
   - If GitHub not connected: Click **"Connect GitHub"**
   - Authorize Render to access repositories
3. Find your repository: `bhiv-core`
4. Click **"Connect"** button next to it

### STEP 4.3: Configure Basic Settings
1. **Name**: Enter `bhiv-core` (or your preferred name)
   - This will be part of your URL: `bhiv-core.onrender.com`
2. **Region**: Select **"Oregon (US West)"**
   - Or choose region closest to your users
3. **Branch**: Select `main`
4. **Root Directory**: Leave blank
5. **Runtime**: Should auto-detect as **"Python 3"**

### STEP 4.4: Configure Build Settings
1. **Build Command**: Enter exactly:
   ```
   pip install -r requirements.txt
   ```
2. **Start Command**: Enter exactly:
   ```
   python mcp_bridge.py
   ```

### STEP 4.5: Select Instance Type
1. Scroll down to "Instance Type"
2. Choose one:
   - **Free**: $0/month (spins down after 15 min inactivity) - for testing
   - **Starter**: $7/month (always on, 512MB RAM) - recommended for production
   - **Standard**: $25/month (2GB RAM) - for high traffic
3. Click your choice

### STEP 4.6: Expand Advanced Settings
1. Click **"Advanced"** button (bottom of page)
2. This opens additional configuration options

---

## PHASE 5: CONFIGURE ENVIRONMENT VARIABLES (10 minutes)

### STEP 5.1: Add Environment Variables
1. In Advanced settings, find **"Environment Variables"** section
2. Click **"Add Environment Variable"** button

### STEP 5.2: Add Each Variable (Repeat for each)

**Variable 1: PORT**
- Key: `PORT`
- Value: `10000`
- Click **"Add"**

**Variable 2: ENVIRONMENT**
- Key: `ENVIRONMENT`
- Value: `production`
- Click **"Add"**

**Variable 3: LOG_LEVEL**
- Key: `LOG_LEVEL`
- Value: `INFO`
- Click **"Add"**

**Variable 4: MONGO_URI** (IMPORTANT)
- Key: `MONGO_URI`
- Value: Paste your MongoDB connection string from Step 1.6
  ```
  mongodb+srv://bhiv_core_user:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/bhiv_core_db?retryWrites=true&w=majority
  ```
- Click **"Add"**

**Variable 5: USE_RL**
- Key: `USE_RL`
- Value: `true`
- Click **"Add"**

**Variable 6: RL_EXPLORATION_RATE**
- Key: `RL_EXPLORATION_RATE`
- Value: `0.2`
- Click **"Add"**

**Variable 7: QDRANT_URLS** (Optional - if you have Qdrant)
- Key: `QDRANT_URLS`
- Value: `https://your-qdrant-url.qdrant.io` OR `disabled`
- Click **"Add"**

**Variable 8: QDRANT_API_KEY** (Optional - if you have Qdrant)
- Key: `QDRANT_API_KEY`
- Value: Your Qdrant API key OR leave blank if disabled
- Click **"Add"**

**Variable 9: BUCKET_URL** (For future integration)
- Key: `BUCKET_URL`
- Value: `http://localhost:8001`
- Click **"Add"**

**Variable 10: KARMA_URL** (For future integration)
- Key: `KARMA_URL`
- Value: `http://localhost:8000`
- Click **"Add"**

### STEP 5.3: Verify All Variables
1. Scroll through environment variables list
2. Verify all 10 variables are added
3. Check for typos in keys and values

---

## PHASE 6: CONFIGURE HEALTH CHECK (2 minutes)

### STEP 6.1: Set Health Check Path
1. Still in Advanced settings
2. Find **"Health Check Path"** field
3. Enter: `/health`
4. Leave other health check settings as default:
   - Health Check Interval: 30 seconds
   - Health Check Timeout: 10 seconds

---

## PHASE 7: DEPLOY SERVICE (10 minutes)

### STEP 7.1: Review Configuration
1. Scroll to bottom of page
2. Review summary:
   - Name: bhiv-core
   - Region: Oregon
   - Branch: main
   - Build: pip install -r requirements.txt
   - Start: python mcp_bridge.py
   - Instance: Starter (or Free)
   - Environment variables: 10 variables

### STEP 7.2: Create Web Service
1. Click **"Create Web Service"** button (bottom of page)
2. You'll be redirected to service dashboard
3. Deployment starts automatically

### STEP 7.3: Monitor Build Phase
1. Click **"Logs"** tab (top of page)
2. Watch real-time logs
3. Build phase steps:
   - Cloning repository from GitHub
   - Installing Python 3.11
   - Running `pip install -r requirements.txt`
   - Installing dependencies (takes 2-5 minutes)
4. Look for: `Build succeeded` message

### STEP 7.4: Monitor Deploy Phase
1. After build succeeds, deploy phase starts
2. Watch logs for:
   - Starting application
   - Running `python mcp_bridge.py`
   - Uvicorn server starting
   - Health check attempts
3. Look for: `Deploy succeeded` message

### STEP 7.5: Check Service Status
1. Click **"Events"** tab
2. You should see:
   - ✅ Build succeeded
   - ✅ Deploy succeeded
   - ✅ Service is live
3. Status indicator (top left) should be green: **"Live"**

---

## PHASE 8: VERIFY DEPLOYMENT (5 minutes)

### STEP 8.1: Get Service URL
1. On service dashboard, find your URL (top of page):
   ```
   https://bhiv-core-xxxx.onrender.com
   ```
2. Copy this URL

### STEP 8.2: Test Health Endpoint
1. Open new browser tab
2. Go to: `https://bhiv-core-xxxx.onrender.com/health`
3. You should see JSON response:
   ```json
   {
     "status": "healthy",
     "timestamp": "2026-02-02T10:00:00",
     "services": {
       "mongodb": "healthy",
       "agent_registry": "healthy"
     }
   }
   ```

### STEP 8.3: Test with cURL (Optional)
1. Open terminal
2. Run:
   ```bash
   curl https://bhiv-core-xxxx.onrender.com/health
   ```
3. Should return same JSON response

### STEP 8.4: Test Task Processing
1. In terminal, run:
   ```bash
   curl -X POST https://bhiv-core-xxxx.onrender.com/handle_task \
     -H "Content-Type: application/json" \
     -d '{"agent":"edumentor_agent","input":"What is AI?","input_type":"text"}'
   ```
2. Should return:
   ```json
   {
     "task_id": "uuid-here",
     "agent_output": {
       "response": "...",
       "status": 200
     },
     "status": "success"
   }
   ```

### STEP 8.5: Check Logs for Errors
1. Go back to Render dashboard
2. Click **"Logs"** tab
3. Look for any ERROR messages
4. Verify MongoDB connection successful
5. Verify agent registry loaded

---

## PHASE 9: CONFIGURE AUTO-DEPLOY (3 minutes)

### STEP 9.1: Enable Auto-Deploy
1. On service dashboard, click **"Settings"** tab
2. Scroll to **"Build & Deploy"** section
3. Find **"Auto-Deploy"** toggle
4. Click toggle to turn it **ON** (should be blue)
5. Verify it says: "Auto-Deploy: Yes"

### STEP 9.2: Configure Deploy Branch
1. Still in Settings
2. Find **"Branch"** field
3. Verify it's set to: `main`
4. This means every push to `main` triggers deployment

### STEP 9.3: Test Auto-Deploy (Optional)
1. Make a small change locally:
   ```bash
   echo "# Updated" >> README.md
   git add README.md
   git commit -m "Test auto-deploy"
   git push origin main
   ```
2. Go to Render dashboard
3. Watch **"Events"** tab - new deployment should start
4. Wait for deployment to complete

---

## PHASE 10: SET UP MONITORING (5 minutes)

### STEP 10.1: Configure Email Notifications
1. Click **"Settings"** tab
2. Scroll to **"Notifications"** section
3. Click **"Add Notification"**
4. Select **"Email"**
5. Enter your email address
6. Select events to notify:
   - ✅ Deploy failed
   - ✅ Service suspended
   - ✅ Service resumed
7. Click **"Save"**

### STEP 10.2: View Metrics
1. Click **"Metrics"** tab
2. You'll see graphs for:
   - CPU usage
   - Memory usage
   - Request count
   - Response time
3. Bookmark this page for monitoring

### STEP 10.3: Set Up External Monitoring (Optional)
1. Go to https://uptimerobot.com
2. Sign up for free account
3. Add new monitor:
   - Type: HTTP(s)
   - URL: `https://bhiv-core-xxxx.onrender.com/health`
   - Interval: 5 minutes
4. Get alerts if service goes down

---

## PHASE 11: FINAL VERIFICATION (5 minutes)

### STEP 11.1: Complete Checklist
- ✅ Service status is "Live" (green)
- ✅ Health endpoint returns 200 OK
- ✅ MongoDB connection working
- ✅ Task processing working
- ✅ No errors in logs
- ✅ Auto-deploy enabled
- ✅ Notifications configured
- ✅ Metrics visible

### STEP 11.2: Document Service Details
Save these details in a safe place:
```
Service Name: bhiv-core
Service URL: https://bhiv-core-xxxx.onrender.com
Health Check: https://bhiv-core-xxxx.onrender.com/health
API Docs: https://bhiv-core-xxxx.onrender.com/docs
MongoDB URI: mongodb+srv://...
Deployment Date: [Today's date]
Instance Type: Starter ($7/month)
Region: Oregon (US West)
```

### STEP 11.3: Test from Different Location
1. Share health URL with colleague or use different device
2. Verify service is accessible globally
3. Check response time from different locations

---

## 🎉 DEPLOYMENT COMPLETE!

Your BHIV Core is now live on Render!

**Service URL**: `https://bhiv-core-xxxx.onrender.com`
**Status**: ✅ Production Ready

### Next Steps:
1. Deploy Bucket service (port 8001)
2. Deploy Karma service (port 8000)
3. Update BUCKET_URL and KARMA_URL environment variables
4. Test complete integration
5. Set up backup strategy
6. Configure custom domain (optional)

---

## 🆘 Troubleshooting

### If Build Fails:
1. Check **Logs** tab for error message
2. Verify `requirements.txt` has all dependencies
3. Check Python version in `runtime.txt` is 3.11.7
4. Verify `render.yaml` syntax is correct

### If Deploy Fails:
1. Check **Logs** tab for error message
2. Verify MongoDB connection string is correct
3. Check environment variables are set correctly
4. Verify PORT is set to 10000
5. Check `mcp_bridge.py` uses `os.getenv("PORT")`

### If Health Check Fails:
1. Verify `/health` endpoint exists in code
2. Check MongoDB connection is working
3. Verify agent registry loads successfully
4. Check logs for startup errors

### If Service Crashes:
1. Check **Logs** tab for crash reason
2. Upgrade to Starter plan if on Free tier
3. Check memory usage in **Metrics** tab
4. Verify all dependencies are installed

---

**Total Deployment Time**: ~60 minutes
**Status**: ✅ Complete
**Date**: 2026-02-02
