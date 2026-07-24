from datetime import datetime

now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

content = f"""# GitHub Actions Lab

## Last Update

{now}

This README is updated automatically by GitHub Actions.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("README updated.")
