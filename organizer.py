#!/usr/bin/env python3
import os
import sys
import shutil
src = sys.argv[1]
types = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".py": "Scripts"
}
count = {
    "Images": 0,
    "Documents": 0,
    "Scripts": 0,
    "Misc": 0
}
for f in os.listdir(src):
    full = os.path.join(src, f)
    if os.path.isfile(full):
        ext = os.path.splitext(f)[1].lower()
        folder = types.get(ext, "Misc")
        dest = os.path.join(src, folder)
        os.makedirs(dest, exist_ok=True)
        new_path = os.path.join(dest, f)
        shutil.move(full, new_path)
        count[folder] += 1

print("Summary:")
for k, v in count.items():
    print(k, ":", v)
