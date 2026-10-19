#!/usr/bin/env python3
import os
import shutil

# Paths
WORKSPACE_LABS = r"C:\Users\Zeetha Robotics\Documents\Vectra-Automation\IOTB-TECH-PROJECTS\phase3\labs"
EXTERNAL_LABS = r"C:\Users\Zeetha Robotics\Documents\Vectra-Automation\zeetafin-phase3-labs"

os.makedirs(WORKSPACE_LABS, exist_ok=True)
os.makedirs(EXTERNAL_LABS, exist_ok=True)

from generate_labs import COMMON_CSS, COMMON_SCRIPT, generate_navbar

def write_lab(filename, content):
    p1 = os.path.join(WORKSPACE_LABS, filename)
    p2 = os.path.join(EXTERNAL_LABS, filename)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(content)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {filename} to both directories ({len(content)} bytes).")

print("Generator helper loaded.")
