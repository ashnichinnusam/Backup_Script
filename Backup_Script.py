import os
import shutil
from datetime import datetime

# Set source and backup directories
source_dir = "/path/to/source_folder"
backup_dir = "/path/to/backup_folder"

def backup_files(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)

    for foldername, subfolders, filenames in os.walk(src):
        # Calculate relative path to preserve folder structure
        rel_path = os.path.relpath(foldername, src)
        dest_folder = os.path.join(dest, rel_path)

        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        for filename in filenames:
            src_file = os.path.join(foldername, filename)
            dest_file = os.path.join(dest_folder, filename)
            
            shutil.copy2(src_file, dest_file)  # copy2 to preserve metadata
            print(f"Copied {src_file} to {dest_file}")

if __name__ == "__main__":
    print(f"Backup started at {datetime.now()}")
    backup_files(source_dir, backup_dir)
    print(f"Backup completed at {datetime.now()}")
