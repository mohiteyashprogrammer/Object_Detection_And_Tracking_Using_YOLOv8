#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   @File Name:     config.py
   @Author:        yash mohite
   @Date:          2023/5/16
   @Description: configuration file
-------------------------------------------------
"""
from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())


# Source
SOURCES_LIST = ["Image", "Video", "Webcam"]


# DL model config
DETECTION_MODEL_DIR = ROOT / 'weights' / 'detection'
YOLOv8n = DETECTION_MODEL_DIR / "yolov8n-oiv7.pt"
YOLOv8s = DETECTION_MODEL_DIR / "yolov8s-oiv7.pt"
YOLOv8m = DETECTION_MODEL_DIR / "yolov8m-oiv7.pt"
YOLOv8l = DETECTION_MODEL_DIR / "yolov8l-oiv7.pt"
YOLOv8x = DETECTION_MODEL_DIR / "yolov8x-oiv7.pt"
# If You Want To Use This Pre Train Model Then UnComment It and  uplode in your weights/detection dir and Use Them All

DETECTION_MODEL_LIST = [
    "yolov8n-oiv7.pt",
    "yolov8s-oiv7.pt",
    "yolov8m-oiv7.pt",
    "yolov8l-oiv7.pt",
    "yolov8x-oiv7.pt",
]
