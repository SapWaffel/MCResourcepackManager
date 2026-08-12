from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import shutil
import zipfile
from pathlib import Path

import requests


# configuration
NAMESPACE = "custom"
PACK_DIR = Path("pack")
PACK_FORMAT = 55
ZIP_NAME = "pack.zip"

# 3. Zip
def build_zip():
    zip_path = PACK_DIR.parent / ZIP_NAME
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in PACK_DIR.rglob("*"):
            if file.is_file():
                zipf.write(file, file.relative_to(PACK_DIR))

    print(f"[OK] Created zip file: {zip_path}")
    return zip_path

build_zip()