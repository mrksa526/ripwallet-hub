# Contributing to Rally Sync

Thank you for your interest in contributing! Here's how you can help.

## Getting Started

### Fork & Clone

```bash
git clone https://github.com/YOUR-USERNAME/rally-sync.git
cd rally-sync
git checkout -b feature/your-feature-name
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
python app-auth.py
# Visit http://localhost:5000/rally-sync.html
```

## How to Contribute

### Report Bugs

**Create an issue with:**
- Title: Clear description of the bug
- Description: What happened, what should happen
- Steps to reproduce: Exact steps to trigger the bug
- Expected vs actual behavior
- Screenshots (if visual issue)

**Example:**
```
Title: Rally times show in wrong timezone

Description: Launch times display as UTC but should show local timezone

Steps:
1. Set local timezone to EST
2. Create a rally
3. Click Calculate
4. See times in UTC instead of EST
```

### Request Features

**Create an issue with:**
- Title: Feature description
- Use case: Why you need it
- Expected behavior: How it should work
- Examples: Mock-ups or similar features

**Example:**
```
Title: Save rally templates

Use case: Players want to reuse common group setups

Expected behavior:
- Click "Save as Template"
- Enter template name
- Later, click "Load Template" to restore

This would save time for recurring rallies.
```

### Submit Code

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature
   ```

2. **Make your changes:**
   - Keep commits small and focused
   - Write clear commit messages
   - Test thoroughly

3. **Test before submitting:**
   ```bash
   # Test calculations with various offset combinations
   # Test export/import functionality
   # Test on mobile browsers
   # Check console for errors (F12)
   ```

4. **Commit with clear messages:**
   ```bash
   git commit -m "Fix: Prevent negative offsets in calculations"
   git commit -m "Feature: Add custom start delay in seconds"
   git commit -m "Docs: Update README with new features"
   ```

5. **Push to your fork:**
   ```bash
   git push origin feature/your-feature
   ```

6. **Open a Pull Request:**
   - Reference any related issues (#123)
   - Describe what changed and why
   - Include test results
   - Link to before/after if visual changes

## Coding Standards

### JavaScript

```javascript
// Clear variable names
const rallyStartTime = new Date(now.getTime() + state.startDelay * 1000);

// Add comments for complex logic
// Calculate spacing: longest march - player's march
const spacing = longestMarch - (player.march || 0);

// Use const/let (not var)
// Keep functions under 50 lines
// Test edge cases (zero offsets, large numbers)
```

### Python

```python
# Follow PEP 8
# Clear function names
def calculate_launch_time(rally_start, spacing, offsets):
    """Calculate exact player launch time."""
    return rally_start + spacing + offsets

# Add docstrings
# Type hints where possible
def init_db() -> None:
    """Initialize SQLite database with required tables."""
    pass
```

## Testing Checklist

Before submitting, test:

- [ ] All calculations correct with various offsets
- [ ] Export/import preserves data
- [ ] Works on mobile (iOS Safari, Chrome Mobile)
- [ ] Works on desktop (Chrome, Firefox, Safari, Edge)
- [ ] No console errors (F12 → Console)
- [ ] localStorage works (not in private mode)
- [ ] Responsive layout on small screens
- [ ] Negative offsets prevented
- [ ] Start delay >= 30 seconds

## Documentation

### Update README if:
- [ ] Adding new features
- [ ] Changing how features work
- [ ] Adding new deployment options

### Update DEPLOYMENT.md if:
- [ ] Changing Docker setup
- [ ] Adding new deployment method
- [ ] Changing environment variables

### Add comments if:
- [ ] Complex calculations
- [ ] Unusual workarounds
- [ ] Browser-specific code

## Git Workflow

```
main (stable)
 ↑
 ├── feature/custom-delays (your feature)
 ├── bugfix/negative-offsets (bug fix)
 └── docs/update-readme (documentation)
```

1. Always branch from `main`
2. Keep branches focused (one feature/fix per branch)
3. Rebase before merging if needed
4. Use clear branch names

## Pull Request Process

1. Update documentation
2. Add/update tests if applicable
3. Ensure all tests pass
4. Request review from maintainers
5. Address feedback
6. Once approved, maintainer will merge

## Code Review

When reviewing others' code:
- ✅ Check logic is correct
- ✅ Test with different values
- ✅ Ensure no console errors
- ✅ Verify responsive design
- ✅ Check documentation updated
- ✅ Look for security issues

Be respectful and constructive!

## Issue Labels

- `bug` - Something broken
- `enhancement` - Feature request
- `documentation` - Docs improvement
- `good first issue` - Good for newcomers
- `help wanted` - Need community help
- `wontfix` - Won't be addressed

## Getting Help

- Check existing issues/discussions
- Ask in GitHub Discussions
- Open an issue with your question

## Release Process

Maintainers will:
1. Review and test PRs
2. Merge to `main`
3. Tag version (v1.0.1, v1.1.0)
4. Push to DockerHub
5. Update release notes

## License

By contributing, you agree your code is licensed under MIT License.

---

**Thank you for helping make Rally Sync better!** 🎯
