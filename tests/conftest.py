import sys
from pathlib import Path

# Add the 'src' directory to sys.path
src_path = Path(__file__).resolve().parent.parent / "src"
sys.path.append(str(src_path))
