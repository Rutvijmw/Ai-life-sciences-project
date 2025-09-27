import sys, os
# Add project root (one level up from tests/) so `import src` works in CI and locally
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
