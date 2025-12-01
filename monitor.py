#!/usr/bin/env python3
"""
Render Monitor Service - PRODUCTION READY
Keeps running to monitor Minecraft server in Google Colab
Updated: 2025-12-01 with new Colab link
"""

import os
import sys
import logging
from flask import Flask, jsonify
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Track uptime
start_time = datetime.now()

# NEW COLAB LINK - UPDATED
COLAB_LINK = "https://colab.research.google.com/drive/1jckV8xUJSmLhhol6wZwVJzpybsimiRw1?usp=sharing"

@app.route('/')
def health():
    """Health check endpoint"""
    uptime = (datetime.now() - start_time).total_seconds()
    return jsonify({
        "status": "alive",
        "service": "Minecraft 24/7 Monitor",
        "message": "Minecraft server runs in Google Colab",
        "colab_link": COLAB_LINK,
        "github": "https://github.com/Albin123725/ColabKeeper",
        "uptime_seconds": uptime,
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route('/health')
def status():
    """Uptime robot ping endpoint"""
    return jsonify({"alive": True, "timestamp": datetime.now().isoformat()}), 200

@app.route('/colab')
def colab_link():
    """Get Colab link endpoint"""
    return jsonify({
        "link": COLAB_LINK,
        "description": "Click to open Minecraft 24/7 server in Google Colab"
    }), 200

@app.route('/status')
def detailed_status():
    """Detailed status endpoint"""
    uptime = (datetime.now() - start_time).total_seconds()
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    return jsonify({
        "service": "ColabKeeper Monitor",
        "running": True,
        "uptime": f"{hours}h {minutes}m",
        "server_location": "Google Colab",
        "colab_link": COLAB_LINK,
        "ports": {
            "java": 25565,
            "bedrock": 19132
        },
        "features": [
            "Google Drive Sync (Latest)",
            "PlayIt.gg Tunneling",
            "Geyser MC (Bedrock)",
            "8 Pre-configured Plugins",
            "AI Crash Prevention",
            "Auto-backup",
            "24/7 Operation"
        ]
    }), 200

@app.route('/restart')
def restart_info():
    """Restart information"""
    return jsonify({
        "message": "To restart Colab server, open the Colab link and re-run the cell",
        "colab_link": COLAB_LINK,
        "steps": [
            "1. Open Colab link",
            "2. Click Runtime → Restart runtime",
            "3. Re-run the Minecraft server cell",
            "4. Server restarts in 30-60 seconds"
        ]
    }), 200

if __name__ == '__main__':
    logger.info("🎮 Starting Minecraft 24/7 Monitor Service...")
    logger.info("📍 Deployment: Render (Monitoring)")
    logger.info("🖥️  Server Location: Google Colab")
    logger.info(f"🔗 Colab Link: {COLAB_LINK}")
    logger.info("✅ Ready to monitor!")
    
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"🚀 Starting Flask on 0.0.0.0:{port}")
    logger.info("📊 Endpoints:")
    logger.info("  GET  /              - Health check")
    logger.info("  GET  /health        - Uptime robot ping")
    logger.info("  GET  /colab         - Get Colab link")
    logger.info("  GET  /status        - Detailed status")
    logger.info("  GET  /restart       - Restart instructions")
    
    try:
        app.run(
            host='0.0.0.0',
            port=port,
            debug=debug,
            use_reloader=False,
            threaded=True
        )
    except Exception as e:
        logger.error(f"❌ Flask error: {e}")
        sys.exit(1)
