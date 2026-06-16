# Changelog

All notable changes to Rally Sync will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-05-07

### Added
- Initial public release
- Web-based rally timing calculator
- Real-time launch time calculations with offsets
- Multi-group and multi-member support
- Per-group and per-player offset configuration (minutes + seconds)
- Global start delay configuration (seconds, minimum 30)
- Automatic march time detection
- Export/import functionality for rally sessions
- localStorage persistence (no server required)
- Offline-capable web app
- Optional backend authentication system
- Login history tracking
- IP blocklist with auto-expire (5 days)
- Server whitelist/blacklist management
- Admin dashboard for session management
- Session transfer/leadership handoff
- Multi-alliance rally comparison
- Responsive design (mobile + desktop)
- Zero negative offset enforcement
- Rally start time validation (never before current time)

### Features
- Calculation formula: Launch Time = Rally Start + Spacing + Group Offset + Player Offset
- Spacing = Longest March - Player's March
- Supports unlimited groups and members
- Customizable rally times (1/5/10/15 minutes)
- Session save/load as JSON
- Import/export for sharing sessions

### Security
- No authentication required for web version
- Optional backend login system
- Password-protected admin dashboard
- Rate limiting on failed attempts
- No external data transmission
- All calculations done locally

### Documentation
- Comprehensive README with usage guide
- Deployment guide for multiple platforms
- Contributing guidelines
- Code of Conduct
- Security policy
- This changelog

### Deployment Options
- Standalone HTML file (no installation)
- Docker container
- Python Flask backend (optional)
- Docker Compose orchestration
- TrueNAS SCALE support
- Cloudflare Tunnel compatible
- Nginx reverse proxy compatible

---

## Future Releases (Planned)

### [1.1.0] - Planned
- [ ] Timezone conversion helpers
- [ ] Player save templates
- [ ] Bulk import from CSV
- [ ] Rally history/analytics
- [ ] Discord webhook integration
- [ ] Mobile app wrapper

### [1.2.0] - Planned
- [ ] Alliance-wide rally coordination
- [ ] Real-time collaboration (multiple leaders)
- [ ] Voice callout integration
- [ ] Advanced scheduling
- [ ] Performance optimizations

---

## Version History

### Initial Development (2025)
- Started as internal alliance tool
- Refined calculations through gameplay
- Added offset validation
- Expanded to multi-group support
- Built optional authentication backend
- Public release preparation

---

## Notes

### Breaking Changes
None yet.

### Known Issues
- Times displayed in UTC (not local timezone)
- localStorage limited to ~5MB per browser
- No undo/redo (export before major changes)

### Migration Guide
N/A for v1.0.0 (initial release)

---

## Contributing

Want to contribute? See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## Support

- **Bug Reports**: [GitHub Issues](https://github.com/gentoonix/rally-sync/issues)
- **Feature Requests**: [GitHub Discussions](https://github.com/gentoonix/rally-sync/discussions)
- **Security Issues**: security@gentoonix.com (don't open public issues)

---

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

Made with ❤️ for rally coordinators everywhere. 🎯
