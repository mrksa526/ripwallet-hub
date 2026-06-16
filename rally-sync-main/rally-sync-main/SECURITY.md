# Security Policy

## Reporting Vulnerabilities

**Do NOT open a public GitHub issue for security vulnerabilities.**

Instead, please email: admin@gentoonix.com

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if available)

We will acknowledge receipt within 24 hours and work to fix it promptly.

## Security Features

### Web Version (rally-sync.html)
- No network requests (except optional comparisons)
- No authentication required
- All data stored locally in browser (localStorage)
- No data sent to any server
- Works offline
- Open source - code is fully auditable

### Backend (app-auth.py)
- Optional login system
- Password-protected admin panel
- IP rate limiting (5 failed attempts per 15 minutes)
- IP blocklist with auto-expire (5 days)
- Server whitelist/blacklist support
- Login history tracking
- SQLite database (encrypted at rest if using full disk encryption)

## Security Best Practices

### Using the Web Version

✅ **Safe to use:**
- In public settings (no data leaves your device)
- On any browser/device
- Offline
- In mobile games during rallies

### Self-Hosting the Backend

✅ **Do:**
- Change `RALLY_ADMIN_PASSWORD` from default
- Use HTTPS/SSL (via Nginx, Cloudflare, etc.)
- Keep Docker images updated
- Monitor logs for suspicious activity
- Regularly backup your database
- Use strong passwords
- Enable firewall rules

❌ **Don't:**
- Expose to internet without HTTPS
- Use weak/default passwords
- Leave admin panel publicly accessible
- Commit `.env` files to git
- Run with outdated dependencies

## Known Limitations

1. **No end-to-end encryption** - If using backend, data sent over HTTP (use HTTPS proxy)
2. **localStorage is not encrypted** - Anyone with browser access can see data
3. **No rate limiting on calculations** - Could be used for DoS if exposed to internet
4. **Admin password in plaintext** - Environment variables not encrypted at rest

## Responsible Disclosure

If you discover a vulnerability:

1. Report privately (don't post publicly)
2. Allow reasonable time to fix (typically 30 days)
3. Don't access/modify other users' data
4. Don't disrupt service availability
5. Don't share vulnerability details publicly until fixed

## Updates

Security patches will be released as soon as possible. Always keep your deployment updated:

```bash
# Docker
docker pull gentoonix/rally-sync:latest
docker-compose up -d

# Manual
git pull origin main
```

## Dependencies

Rally Sync uses:
- Flask (Python web framework)
- Python 3.11 (language)
- SQLite (database)

All dependencies pinned to specific versions in `requirements.txt`. Check for updates regularly:

```bash
pip list --outdated
```

## Security Headers (for deployments)

If using Nginx reverse proxy, add these security headers:

```nginx
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "no-referrer-when-downgrade" always;
add_header Content-Security-Policy "default-src 'self'" always;
```

## GDPR & Privacy

- **No tracking** - No analytics, no cookies
- **No personal data storage** - Only login history (optional)
- **No external services** - All data stays on your device/server
- **Data deletion** - Clear browser storage or delete database file
- **No data sharing** - We don't collect or share anything

## SSL/TLS

For production deployments, always use HTTPS:

**Option 1: Cloudflare Tunnel** (easiest)
```bash
cloudflared tunnel run rally-sync
```

**Option 2: Let's Encrypt + Nginx**
```bash
sudo certbot certonly --standalone -d rally.yourdomain.com
# Configure Nginx to use certificate
```

**Option 3: Self-signed (testing only)**
```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

## Security Checklist for Deployment

- [ ] HTTPS enabled
- [ ] Admin password changed
- [ ] Firewall configured
- [ ] Docker images updated
- [ ] Logs monitored
- [ ] Database backed up
- [ ] .env not committed
- [ ] IP rate limiting enabled
- [ ] Server blocklist reviewed

## Contact

For security issues: security@gentoonix.com
For general questions: Use GitHub Discussions

Thank you for helping keep Rally Sync secure! 🔒
