import sys, os
from pathlib import Path

path = Path('/code')
path = os.getcwd() + str(path)
sys.path.append(path)

import platformer
platformer.run()
