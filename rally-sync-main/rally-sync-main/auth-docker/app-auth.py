from flask import Flask, request, jsonify
import sqlite3
import hashlib
import time
import aiohttp
import asyncio
import ssl
import requests
from datetime import datetime, timedelta
from functools import wraps
import json
import os

app = Flask(__name__)
DATABASE = '/app/data/rally_auth.db'  # Use /app/data directory
KINGSHOT_API = "https://kingshot-giftcode.centurygame.com/api/player"
KINGSHOT_SECRET = "mN4!pQs6JrYwV9"

# Get admin password from environment variable
ADMIN_PASSWORD = os.getenv('RALLY_ADMIN_PASSWORD')
if not ADMIN_PASSWORD:
    print("⚠️  ERROR: RALLY_ADMIN_PASSWORD environment variable not set!")
    print("⚠️  Set it before running: export RALLY_ADMIN_PASSWORD='your-secure-password'")
    ADMIN_PASSWORD = None  # Will cause auth to fail safely

# ============================================================================
# DATABASE SETUP
# ============================================================================

def init_db():
    # Ensure directory exists
    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
