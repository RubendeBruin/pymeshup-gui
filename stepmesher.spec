# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all, collect_submodules

hidden = ["vedo"]
vedo_hiddenimports = collect_submodules("vedo")

casadi_datas, casadi_binaries, casadi_hiddenimports = collect_all("casadi")
casadi_binaries = [(src, "casadi") for src, _ in casadi_binaries]


a = Analysis(
    ['stepmesher.py'],
    pathex=[],
    binaries=casadi_binaries,
    datas=casadi_datas,
    hiddenimports=hidden + vedo_hiddenimports + casadi_hiddenimports + ["casadi._casadi"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=["pyi_rth_casadi_path.py"],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='stepmesher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='stepmesher',
)
