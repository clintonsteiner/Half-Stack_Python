import os
import sys
import subprocess

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
VENV_PATH = os.path.join(BASE_PATH, "venv")
RAN = False
BUILD_DIR = os.path.join(BASE_PATH, "build")
SOURCE_DIR = os.path.join(BASE_PATH, "source")


def create_venv():
    if not sys.prefix != sys.base_prefix:
        if not os.path.exists(VENV_PATH):
            subprocess.check_call([sys.executable, "-m", "venv", VENV_PATH])
        python = os.path.join(VENV_PATH, "bin", "python")
        os.execv(python, [python] + sys.argv)

    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    sphinx = os.path.join(VENV_PATH, "bin", "sphinx-build")
    subprocess.check_call([sphinx, SOURCE_DIR, BUILD_DIR])

create_venv()
