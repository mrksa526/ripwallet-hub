[DEPLOYMENT.md](https://github.com/user-attachments/files/28317958/DEPLOYMENT.md)
# Rally Sync Deployment Guide

## Quick Start - No Server Required

The simplest way to use Rally Sync:

1. Download `rally-sync.html`
2. Open in your web browser
3. Done! No installation needed.

---

## Docker Deployment (Recommended)

### With Docker Compose

```bash
# Clone repo
git clone https://github.com/gentoonix/rally-sync.git
cd rally-sync

# Set admin password
export RALLY_ADMIN_PASSWORD="your-secure-password"

# Start
docker-compose up -d

# Access
# App: http://localhost:5001/rally-sync.html
# Login: http://localhost:5001/login.html (if enabled)
# Admin: http://localhost:5001/admin-dashboard.html
```

### With Docker CLI

```bash
docker run -d \
  --name rally-sync \
  -p 5001:5000 \
  -e RALLY_ADMIN_PASSWORD="your-secure-password" \
  -v rally-data:/app/data \
  gentoonix/rally-sync:latest
```

---

## Manual Installation (Linux/Mac)

### Requirements
- Python 3.11+
- pip

### Install

```bash
# Clone repo
git clone https://github.com/gentoonix/rally-sync.git
cd rally-sync

# Install dependencies
pip install -r requirements.txt

# Set password
export RALLY_ADMIN_PASSWORD="your-secure-password"

# Run
python app-auth.py

# Access
# http://localhost:5000/rally-sync.html
```

---

## TrueNAS SCALE Installation

### Via Web UI

1. Go to **Applications → Docker → Containers**
2. Click **Create**
3. Configure:
   - **Image**: `gentoonix/rally-sync:latest`
   - **Name**: `rally-sync`
   - **Port Mappings**: 
     - Container: 5000 → Host: 5001
   - **Environment Variables**:
     - `RALLY_ADMIN_PASSWORD`: your-secure-password
   - **Volumes**:
     - Host: `/mnt/tank/rally-data`
     - Container: `/app/data`
4. Click **Create Container**

### Via SSH

```bash
mkdir -p /mnt/tank/rally-data
chmod 777 /mnt/tank/rally-data

docker run -d \
  --name rally-sync \
  -p 5001:5000 \
  -e RALLY_ADMIN_PASSWORD="your-secure-password" \
  -v /mnt/tank/rally-data:/app/data \
  --restart unless-stopped \
  gentoonix/rally-sync:latest
```

---

## Cloudflare Tunnel Setup

### 1. Install Cloudflare Tunnel

```bash
# On your server
curl -L --output cloudflared.tgz https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.tgz
tar -xzf cloudflared.tgz
sudo mv cloudflared /usr/local/bin
```

### 2. Authenticate

```bash
cloudflared tunnel login
```

### 3. Create Tunnel

```bash
cloudflared tunnel create rally-sync
```

### 4. Configure

Create `~/.cloudflared/config.yml`:

```yaml
tunnel: rally-sync
credentials-file: /home/user/.cloudflared/UUID-credentials.json

ingress:
  - hostname: rally.yourdomain.com
    service: http://localhost:5001
  - service: http_status:404
```

### 5. Run

```bash
cloudflared tunnel run rally-sync
```

### 6. DNS

Add CNAME in Cloudflare:
- Name: `rally`
- Target: `rally-sync.cfargotunnel.com`

---

## Nginx Reverse Proxy

```nginx
server {
    listen 443 ssl http2;
    server_name rally.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location / {
        proxy_pass http://localhost:5001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

---

## Environment Variables

```bash
# Admin password for dashboard
RALLY_ADMIN_PASSWORD=your-secure-password

# Flask environment (production or development)
FLASK_ENV=production

# Database location (default: /tmp/rally_auth.db)
DATABASE=/tmp/rally_auth.db
```

---

## Persistent Data

### Docker Volume

```bash
docker volume create rally-data
docker run -v rally-data:/app/data ...
```

### Host Volume

```bash
docker run -v /mnt/tank/rally-data:/app/data ...
```

---

## Monitoring

### Check Status

```bash
docker ps -a | grep rally-sync
```

### View Logs

```bash
docker logs -f rally-sync
```

### Restart

```bash
docker restart rally-sync
```

### Stop

```bash
docker stop rally-sync
```

---

## Troubleshooting

**Port already in use:**
```bash
lsof -i :5001  # See what's using port
docker run -p 5002:5000 ...  # Use different port
```

**Database errors:**
```bash
docker stop rally-sync
docker run -it --rm -v rally-data:/app/data \
  gentoonix/rally-sync:latest python
# In Python: import sqlite3; sqlite3.connect('/app/data/rally_auth.db')
```

**Can't access from outside:**
- Check firewall: `sudo ufw allow 5001`
- Check proxy config
- Verify DNS resolves
- Check container logs: `docker logs rally-sync`

---

## Backup & Restore

### Backup

```bash
docker cp rally-sync:/app/data/rally_auth.db ~/rally_auth.db.backup
```

### Restore

```bash
docker cp ~/rally_auth.db.backup rally-sync:/app/data/rally_auth.db
docker restart rally-sync
```

---

## Updates

### Pull Latest

```bash
docker pull gentoonix/rally-sync:latest
docker-compose up -d  # Or docker run with new image
```

---

## Security Best Practices

1. **Change default password**
   ```bash
   export RALLY_ADMIN_PASSWORD="strong-password-here"
   ```

2. **Use HTTPS**
   - Set up Cloudflare Tunnel or Nginx proxy
   - Use SSL certificates (Let's Encrypt)

3. **Keep Docker updated**
   ```bash
   docker pull gentoonix/rally-sync:latest
   ```

4. **Regular backups**
   ```bash
   # Backup daily
   0 2 * * * docker cp rally-sync:/app/data/rally_auth.db /backups/rally_$(date +\%Y\%m\%d).db
   ```

5. **Monitor logs**
   ```bash
   docker logs -f rally-sync
   ```

---

## Need Help?

- Check GitHub issues: https://github.com/gentoonix/rally-sync/issues
- Review logs: `docker logs rally-sync`
- Test locally first before production

Happy rallying! 🎯
