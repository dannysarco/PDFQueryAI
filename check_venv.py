import sys

if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("Inside a virtual environment")
else:
    print("Not inside a virtual environment")
