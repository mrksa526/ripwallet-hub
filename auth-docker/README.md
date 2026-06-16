# Rally Sync - With Auth

Self-hosted Rally Sync with optional player authentication, admin dashboard, and session management.

## Quick Start

### Option 1: Docker Compose (Easiest)

```bash
cd auth-docker
export RALLY_ADMIN_PASSWORD="your-secure-password"
docker-compose up -d
```

Access:
- App: `http://localhost:5001/rally-sync.html`
- Login: `http://localhost:5001/login.html`
- Admin: `http://localhost:5001/admin-dashboard.html`

### Option 2: Docker Run

```bash
docker run -d \
  --name rally-sync \
  -p 5001:5000 \
  -e RALLY_ADMIN_PASSWORD="your-secure-password" \
  -v rally-data:/app/data \
  --restart unless-stopped \
  gentoonix/rally-sync:latest
```

### Option 3: Manual (Python)

```bash
pip install -r requirements.txt
export RALLY_ADMIN_PASSWORD="your-secure-password"
python app-auth.py
```

## Features

✅ Player login (ID + Server Number validation)
✅ Admin dashboard (password-protected)
✅ Login history tracking
✅ IP blocklist (5-day auto-expire)
✅ Server whitelist/blacklist
✅ Session management & transfer
✅ Persistent database

## Configuration

### Admin Password

```bash
export RALLY_ADMIN_PASSWORD="your-secure-password"
```

**Requirements:**
- At least 12 characters
- Mix of uppercase, lowercase, numbers, symbols
- Example: `P@ssw0rd!Rally2024`

### Optional: Environment Variables

```bash
RALLY_ADMIN_PASSWORD=your-password    # Required
FLASK_ENV=production                  # Optional
DATABASE=/app/data/rally_auth.db      # Optional
```

## Files

- `Dockerfile` - Docker image
- `app-auth.py` - Flask web server with auth
- `requirements.txt` - Python dependencies (includes auth libs)
- `rally-sync.html` - The app
- `login.html` - Login page
- `admin-dashboard.html` - Admin panel
- `docker-compose.yml` - Easy orchestration

## Persistent Data

Database stored in volume: `rally-data`

Backup:
```bash
docker cp rally-sync:/app/data/rally_auth.db ./backup.db
```

Restore:
```bash
docker cp ./backup.db rally-sync:/app/data/rally_auth.db
docker restart rally-sync
```

## Admin Dashboard

After starting, visit: `http://localhost:5001/admin-dashboard.html`

Login with your `RALLY_ADMIN_PASSWORD`

Features:
- View login history (500 recent)
- Manage IP blocklist
- Manage server whitelist/blacklist
- Real-time statistics

## Player Login

Players access: `http://localhost:5001/login.html`

Enter:
- Player ID (from game)
- Server Number (their server)

System validates against Kingshot API.

## Deployment

### Docker Hub

```bash
docker pull gentoonix/rally-sync:latest
```

### TrueNAS

```bash
docker run -d \
  --name rally-sync \
  -p 5001:5000 \
  -e RALLY_ADMIN_PASSWORD="your-password" \
  -v /mnt/tank/rally-data:/app/data \
  --restart unless-stopped \
  gentoonix/rally-sync:latest
```

### Production (with HTTPS)

See [../DEPLOYMENT.md](../DEPLOYMENT.md) for Nginx, Cloudflare Tunnel, etc.

## Troubleshooting

**Can't login to admin?**
- Check password matches `RALLY_ADMIN_PASSWORD`
- Clear browser cache/localStorage
- Check browser console (F12)

**Player login fails?**
- Check Player ID is valid
- Verify Server Number matches their game server
- Check docker logs: `docker logs rally-sync`

**Lost admin password?**
```bash
export RALLY_ADMIN_PASSWORD="new-password"
docker-compose up -d --force-recreate
```

## Need simpler version?

For no-auth version, use **simple-docker** instead.

See [../simple-docker/README.md](../simple-docker/README.md)

---

For full docs, see [../DEPLOYMENT.md](../DEPLOYMENT.md)
