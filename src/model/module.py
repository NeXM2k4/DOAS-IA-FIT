import sys
from pathlib import Path

def module(directory):
    base = Path(directory)
    root = base.resolve().parents[2]
    #print(base)
    if str(base) not in sys.path:
        sys.path.append(str(root))