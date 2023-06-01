import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s:')


project_name = "textSummarizer"

List_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init_.py",
    f"src/{project_name}/conponents/__init_.py",
    f"src/{project_name}/utils/__init_.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init_.py",
    f"src/{project_name}/config/__init_.py",
    f"src/{project_name}/config/congiguration.py",
    f"src/{project_name}/pipeline/__init_.py",
    f"src/{project_name}/entity/__init_.py",
    f"src/{project_name}/constants/__init_.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requriments.txt",
    "setup.py",
    "research/trials.ipnb",
]




for filepath in List_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open (filepath, 'w') as f:
            pass
            logging.info(f"Created empty file {filename}")

    else:
        logging.info(f"File {filename} already exists")