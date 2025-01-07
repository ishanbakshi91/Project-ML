import os
from pathlib import Path
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter your project name: ")
    if project_name !='':
        break

logging.info(f"Creating project by name: {project_name}")
