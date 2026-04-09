#!/usr/bin/env python3
"""
Finviz MCP Server Wrapper for Railway deployment
Starts finviz-mcp with FastAPI proxy
"""

import os
import subprocess
import sys
import threading
import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()
mcp_process = None

@app.get("/")
async def health():
    """Health check endpoint"""
    return JSONResponse({
        "status": "ok",
        "service": "finviz-mcp",
        "version": "1.0",
        "message": "MCP is running. Add to Claude.ai with this URL."
    })

@app.get("/_health")
async def deep_health():
    """Deep health check"""
    return JSONResponse({
        "status": "ok",
        "mcp_process": mcp_process.poll() is None if mcp_process else False,
        "port": os.getenv("PORT", "8000")
    })

def start_mcp_background():
    """Start the finviz-mcp server in background"""
    global mcp_process
    
    print("\n⏳ Waiting for FastAPI to initialize...")
    time.sleep(2)
    
    host = "127.0.0.1"
    port = "8001"
    
    print(f"\n🚀 Starting MCP server on {host}:{port}")
    print("=" * 70)
    
    cmd = [
        "finviz-mcp",
        "streamable-http",
        "--host", host,
        "--port", port
    ]
    
    print(f"Command: {' '.join(cmd)}")
    print("=" * 70)
    
    try:
        mcp_process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        for line in iter(mcp_process.stdout.readline, ''):
            if line:
                print(f"[MCP] {line.rstrip()}")
        
        mcp_process.wait()
    except Exception as e:
        print(f"❌ Error starting MCP: {e}")
        sys.exit(1)

def main():
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")
    
    print(f"🚀 Starting Finviz MCP Server on {host}:{port}")
    print("=" * 70)
    
    mcp_thread = threading.Thread(target=start_mcp_background, daemon=False)
    mcp_thread.start()
    
    print(f"\n📡 Starting FastAPI on {host}:{port}")
    uvicorn.run(app, host=host, port=port, log_level="info")

if __name__ == "__main__":
    main()
