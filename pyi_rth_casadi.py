"""
PyInstaller runtime hook for casadi.

On Windows, Python 3.8+ changed DLL loading so that only directories
explicitly registered via os.add_dll_directory() are searched.
The casadi package keeps _casadi.pyd and all its dependent DLLs together
in the same directory.  When frozen, that directory is a subdirectory of
sys._MEIPASS, so we must register it before the import machinery tries
to load _casadi.pyd.
"""
import os
import sys

if sys.platform == "win32" and hasattr(os, "add_dll_directory"):
    _bundle_dir = getattr(sys, "_MEIPASS", None)
    if _bundle_dir:
        _casadi_dir = os.path.join(_bundle_dir, "casadi")
        if os.path.isdir(_casadi_dir):
            os.add_dll_directory(_casadi_dir)

