# Jul-31-2025
# dir_support.py

import shutil
from pathlib import Path


# Reseting directory
def reset_directory(dir_name):

    path_dir = Path.cwd() / dir_name

    if path_dir.is_dir():
        for item in path_dir.iterdir():
            if item.is_file():
                item.unlink()           # Remove file
            elif item.is_dir():
                shutil.rmtree(item)     # Remove directory
    else:
        path_dir.mkdir()
