# Rally Sync - Simple (No Auth)

The easiest way to self-host Rally Sync - just a web app server, no login system needed.

## Quick Start

### Option 1: Docker Compose (Easiest)

```bash
cd simple-docker
docker-compose up -d
```

Access: `http://localhost:5001/rally-sync.html`

### Option 2: Docker Run

```bash
docker run -d \
  --name rally-sync \
  -p 5001:5000 \
  --restart unless-stopped \
  gentoonix/rally-sync:simple
```

### Option 3: Manual (Python)

```bash
pip install -r requirements-simple.txt
python app-simple.py
```

Access: `http://localhost:5000/rally-sync.html`

## What's Included

- Web-based rally timing calculator
- No login required
- No database
- All data stored locally in browser
- Works offline
- Export/import sessions

## What's NOT Included

- Player authentication
- Admin dashboard
- Login history
- IP blocking
- Session transfer (requires backend)

## Files

- `Dockerfile` - Docker image
- `app-simple.py` - Flask web server
- `requirements-simple.txt` - Python dependencies
- `rally-sync.html` - The app
- `docker-compose.yml` - Easy orchestration

## Configuration

No configuration needed! Just run and access.

## Deployment

### Docker Hub

```bash
docker pull gentoonix/rally-sync:simple
```

### TrueNAS

```bash
docker run -d \
  --name rally-sync \
  -p 5001:5000 \
  --restart unless-stopped \
  gentoonix/rally-sync:simple
```

### Production (Nginx)

```nginx
server {
    listen 443 ssl;
    server_name rally.yourdomain.com;
    
    location / {
        proxy_pass http://localhost:5001;
        proxy_set_header Host $host;
    }
}
```

## Troubleshooting

**Port already in use?**
```bash
docker run -p 5002:5000 gentoonix/rally-sync:simple
```

**Can't access from outside?**
- Check firewall: `sudo ufw allow 5001`
- Check DNS resolves to your server
- Use HTTPS proxy (Nginx, Cloudflare)

## Need Auth?

If you need login/admin features, use the **auth-docker** version instead.

See [../auth-docker/README.md](../auth-docker/README.md)

---

For full docs, see [../DEPLOYMENT.md](../DEPLOYMENT.md)
