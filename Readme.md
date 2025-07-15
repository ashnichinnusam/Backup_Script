# Automated Backup Script (Python)

A simple Python script to back up files from a source folder to a destination folder. Useful for creating daily or weekly backups of important files, and can be automated using cron (Linux/macOS) or Task Scheduler (Windows).

---

## 🔧 Features

- Recursively copies all files from the source to the backup folder.
- Preserves folder structure and file metadata (timestamps, permissions).
- Logs each copied file to the console.
- Easy to configure paths and schedule.

---

## 📦 Requirements

- Python 3.x

No external packages needed — uses Python's built-in libraries (`os`, `shutil`, `datetime`).

---

## 📁 Setup

1. Clone or download this repository:
2. Open backup_script.py and set the paths, Replace /path/to/source_folder and /path/to/backup_folder with your actual folders.
3. Run the Script

