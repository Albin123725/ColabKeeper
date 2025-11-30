#!/usr/bin/env python3
"""
Render Monitor Service - PRODUCTION READY
Keeps running to monitor Minecraft server in Google Colab
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

@app.route('/')
def health():
    """Health check endpoint"""
    uptime = (datetime.now() - start_time).total_seconds()
    return jsonify({
        "status": "alive",
        "service": "Minecraft 24/7 Monitor",
        "message": "Minecraft server runs in Google Colab",
        "github": "https://github.com/Albin123725/ColabKeeper",
        "uptime_seconds": uptime,
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route('/health')
def status():
    """Uptime robot ping endpoint"""
    return jsonify({"alive": True, "timestamp": datetime.now().isoformat()}), 200

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
        "ports": {
            "java": 25565,
            "bedrock": 19132
        },
        "features": [
            "PlayIt.gg Tunneling",
            "Geyser MC (Bedrock)",
            "8 Pre-configured Plugins",
            "AI Crash Prevention",
            "Auto-backup",
            "24/7 Operation"
        ]
    }), 200

if __name__ == '__main__':
    logger.info("🎮 Starting Minecraft 24/7 Monitor Service...")
    logger.info("📍 Deployment: Render (Monitoring)")
    logger.info("🖥️  Server Location: Google Colab")
    logger.info("✅ Ready to monitor!")
    
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"🚀 Starting Flask on 0.0.0.0:{port}")
    
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
