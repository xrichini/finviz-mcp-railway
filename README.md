# Finviz MCP Server for Railway

Deploy finviz-mcp to Railway.app for market data, insider trading, and stock screening on Claude.ai mobile! ☁️

## 🚀 Deploy to Railway (3 steps)

### Step 1: Push to GitHub ✅ (already done)

### Step 2: Create Railway Project

1. Go to https://railway.app
2. Click **New Project**
3. Select **Deploy from GitHub repo**
4. Select `finviz-mcp-railway` repo
5. Railway auto-detects the Procfile
6. Click **Deploy** → wait 2-3 minutes

### Step 3: Add to Claude.ai Mobile

1. Open Claude.ai on mobile
2. Settings → **MCPs**
3. Add new MCP:
   ```json
   {
     "name": "finviz-mcp",
     "url": "https://finviz-mcp-xxx.railway.app"
   }
   ```
   (Replace `xxx` with your Railway project ID)
4. Test in chat

## 📊 Available Tools

- `finviz_get_market_insiders()` — Insider trading data
- `finviz_get_sector_performance()` — Sector trends
- `finviz_screener()` — Stock screening
- `finviz_get_quote()` — Stock quotes
- And more...

## 🔗 Get Your URL

In Railway dashboard:
- Select your service
- Go to **Deployments**
- Copy the URL like `https://finviz-mcp-xxx.railway.app`
- This is what you paste into Claude.ai settings

## 💡 Pro Tips

- **Real-time logs**: Railway dashboard → Deployments → Logs tab
- **Auto-redeploy**: Push to GitHub, Railway redeploys automatically in ~30 sec
- **Free for 3-6 months**: $5 monthly credits never expire
- **After free credits**: Pay $5/mo, switch to GitHub Actions, or self-host

## ❓ Troubleshooting

### "Can't connect to the URL"
1. Wait 2 minutes after deploy
2. Check Railway dashboard → Deployments for build/deploy errors
3. View logs: Deployments → Logs tab

### "MCP not responding in Claude.ai"
1. Verify the URL is correct (no typos)
2. Check Railway logs for errors
3. Test the URL directly in a browser: https://your-url.railway.app
   Should show MCP connection info

## 📚 Links

- Railway docs: https://docs.railway.app
- MCP protocol: https://modelcontextprotocol.io
- Railway pricing: https://railway.app/pricing
