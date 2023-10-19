from pathlib import Path
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

BASE_DIR = Path(os.path.realpath(Path(dir_path) / ".."))
