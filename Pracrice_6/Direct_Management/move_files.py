# move_files.py
import shutil
from pathlib import Path

source = Path(r"C:\Users\Admin\Desktop\Pracrice_6\File_Handling\demofile.txt")  # adjust path if needed
destination = Path(r"C:\Users\Admin\Desktop\Pracrice_6\Directory_Management\test_dir\demofile.txt")

# Ensure the destination folder exists
destination.parent.mkdir(parents=True, exist_ok=True)

# Move the file
if source.exists():
    shutil.move(str(source), str(destination))
    print(f"Moved {source} -> {destination}")
else:
    print(f"Source file not found: {source}")