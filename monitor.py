#!/usr/bin/env python3
"""
Render Monitor Service
Just monitors/logs - actual Minecraft server runs in Google Colab
"""

import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def health():
    return jsonify({
        "status": "monitoring",
        "message": "Minecraft server runs in Google Colab",
        "github": "https://github.com/Albin123725/ColabKeeper"
    })

@app.route('/health')
def status():
    return jsonify({"alive": True})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
