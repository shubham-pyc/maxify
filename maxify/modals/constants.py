
from maxify.helpers.utils import get_platform
import os

platform = get_platform()

DESKTOP = "Desktop"
OPTIMIZATION_HOME = "OPTIMIZATION_HOME"


if platform == "windows":
    DEBUG_FOLDER_PATH = os.path.join(
        os.path.join(os.environ['USERPROFILE']), DESKTOP)
else:
    DEBUG_FOLDER_PATH = os.path.join(
        os.path.join(os.path.expanduser('~')), DESKTOP)


ORIGINAL_FOLDER_PATH = os.environ.get(OPTIMIZATION_HOME, DEBUG_FOLDER_PATH)