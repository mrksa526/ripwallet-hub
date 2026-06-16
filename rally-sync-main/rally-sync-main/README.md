# Rally Sync - Real-time Rally Coordinator

A web-based rally timing coordinator for mobile strategy games. Calculate exact launch times for coordinated group attacks with per-player and per-group offsets.

## Features

✅ **Precise Timing Calculations**
- Real-time rally start time calculation
- Configurable global start delay (in seconds)
- Per-group offsets (minutes + seconds)
- Per-player offsets (minutes + seconds)
- Automatic march time detection

✅ **Multi-Group Support**
- Create unlimited groups
- Add unlimited members per group
- Independent offset configuration per group and player
- Export/import sessions as JSON

✅ **Smart Calculations**
- Launch Time = Rally Start + Spacing + Group Offset + Player Offset
- Spacing = Longest March - Player's March
- No negative offsets allowed
- Rally start never before current time

✅ **Session Management**
- Save and load rally sessions
- Transfer leadership between players
- Compare multiple alliance rallies
- Local storage persistence

## Quick Start

### Local Installation
1. Download `rally-sync.html`
2. Open in any modern web browser
3. No server required!

## How to Use

### 1. Configure Rally Settings
- **Rally Time**: Select march duration (1/5/10/15 minutes)
- **Start Delay**: How many seconds before rally starts (default: 60)
  - Use standard dropdown or check "Custom Value" for custom seconds (min 30)

### 2. Create Groups
- Click **"Add Group"** to create a new rally group
- Name it (e.g., "Wave 1", "Backup Group", etc.)
- Set group offset (optional - delays entire group)

### 3. Add Players
- Click **"Add Member"** to add a player to a group
- Enter player name
- Enter march time (if different from rally time)
- Set player offset (optional - individual delay)

### 4. Calculate Launch Times
- Click **"CALCULATE"** to compute exact launch times
- See each player's launch time in the group display
- All times in UTC

### 5. Save/Share
- Click **"Export"** to save session as JSON file
- Click **"Import"** to load a saved session
- Share sessions with alliance members

## Calculation Example

**Settings:**
- Rally Time: 5 minutes
- Start Delay: 35 seconds (custom)
- Current Time: 12:00:00 UTC

**Rally Start:** 12:00:35 UTC

**Group 1** (30 second offset):
- Player A (5 min march, no offset)
  - Launch: 12:00:35 + 0 spacing + 30 offset = **12:01:05**
- Player B (3 min march, 10 second offset)
  - Launch: 12:00:35 + 120 spacing + 30 offset + 10 offset = **12:02:35**

## Offset Rules

- **Start Delay**: Global heads-up time before rally (seconds, min 30)
- **Group Offset**: Delay for entire group (minutes + seconds)
- **Player Offset**: Individual delay for player (minutes + seconds)
- **All offsets cumulative**: Total = Group Offset + Player Offset
- **No negative values**: System prevents any negative offsets

## Storage

- All data stored locally in browser (localStorage)
- No server required
- No data sent anywhere
- Works offline

## Browser Support

- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Self-Hosting (Optional)

### Docker
```bash
docker pull gentoonix/rally-sync:latest
docker run -d -p 5001:5000 gentoonix/rally-sync:latest
```
Access: `http://localhost:5001/rally-sync.html`

### Python (Flask)
```bash
# Requirements
pip install flask

# Run
python app-auth.py
```
Access: `http://localhost:5000/rally-sync.html`

## Advanced Features

### Transfer Leadership
- Only in auth-enabled deployments
- Current leader generates token
- New leader accepts token
- Old leader becomes read-only

### Multi-Alliance Comparison
- View multiple rallies simultaneously
- Toggle comparison view
- Side-by-side timing comparison

### Session Management
- Create multiple named sessions
- Join existing sessions
- Read-only access when not leader

## API Endpoints (Self-Hosted)

```
GET  /                           - Health check
GET  /rally-sync.html            - Main app
POST /api/auth/login             - Player login (if enabled)
GET  /api/admin/login-history    - Login history (admin only)
GET  /api/admin/blocklist        - IP blocklist (admin only)
```

## Troubleshooting

**Times showing UTC instead of local?**
- The app displays UTC times for consistency
- Convert manually or use `new Date()` in console

**Offsets not applying?**
- Make sure values are ≥ 0 (negative values blocked)
- Group offset affects entire group
- Player offset adds to group offset

**Data not saving?**
- Check browser allows localStorage
- Not in private/incognito mode
- Browser storage not full

**Can't import session?**
- Ensure JSON file is valid
- Check file from same version of app

## Contributing

Found a bug? Have a feature request?
- Open an issue on GitHub
- Submit a pull request
- Provide calculation examples for issues

## License

MIT License - feel free to use, modify, and distribute

## Credits

Developed for mobile strategy game rally coordination.
Inspired by real-world alliance needs.

## Changelog

### v1.0
- Initial release
- Precise timing calculations
- Multi-group support
- Session management
- Export/import functionality
- Custom start delay (seconds)
- No login required (web version)

---

**Questions?** Check the calculation formula or test with example values.

**For Developers:** See `app-auth.py` and `Dockerfile` for self-hosting with authentication.
