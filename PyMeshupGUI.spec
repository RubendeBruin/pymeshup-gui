# -*- mode: python ; coding: utf-8 -*-
import os
import sys

from PyInstaller.utils.hooks import collect_all, collect_submodules

sys.setrecursionlimit(sys.getrecursionlimit() * 5)

# ---- vedo fonts
from vedo import installdir as vedo_installdir
vedo_fontsdir = os.path.join(vedo_installdir, 'fonts')
print('vedo installation is in', vedo_installdir)
print('fonts are in', vedo_fontsdir)

vedo_added_files = [
    (os.path.join(vedo_fontsdir, '*'), os.path.join('vedo', 'fonts')),
]

# ---- casadi (binaries remapped so _casadi.pyd and its DLLs land in casadi/)
casadi_datas, casadi_binaries, casadi_hiddenimports = collect_all('casadi')
casadi_binaries = [(src, 'casadi') for src, _ in casadi_binaries]

# ---- pymeshlab
pymeshlab_datas, pymeshlab_binaries, pymeshlab_hiddenimports = collect_all('pymeshlab')

# ---- h5py / h5netcdf
h5py_datas, h5py_binaries, h5py_hiddenimports = collect_all('h5py')
h5netcdf_datas, h5netcdf_binaries, h5netcdf_hiddenimports = collect_all('h5netcdf')

# ---- vedo submodules
vedo_hiddenimports = collect_submodules('vedo')

datas = [
    ('src/pymeshup_gui/gui/examples', 'examples'),
    ('src/pymeshup_gui/resources', 'pymeshup_gui/resources'),
] + vedo_added_files + casadi_datas + pymeshlab_datas + h5py_datas + h5netcdf_datas

binaries = casadi_binaries + pymeshlab_binaries + h5py_binaries + h5netcdf_binaries

hiddenimports = (
    vedo_hiddenimports
    + casadi_hiddenimports
    + pymeshlab_hiddenimports
    + h5py_hiddenimports
    + h5netcdf_hiddenimports
    + ['casadi._casadi', 'h5py', 'h5netcdf']
    + [
        'vtkmodules.vtkCommonMath',
        'vtkmodules.vtkCommonTransforms',
        'vtkmodules.vtkCommonExecutionModel',
        'vtkmodules.vtkIOCore',
        'vtkmodules.vtkRenderingCore',
        'vtkmodules.vtkFiltersCore',
        'vtkmodules.vtkCommonMisc',
        'vtkmodules.vtkRenderingVolumeOpenGL2',
        'vtkmodules.vtkImagingMath',
        'vtkmodules.all',
        # capytaine
        'numpy',
        'logging',
        'capytaine',
        'matplotlib',
        'scipy',
        'capytaine.green_functions',
        'capytaine.green_functions.libs',
        'capytaine.green_functions.libs.Delhommeau_float64',
        'capytaine.green_functions.libs.Delhommeau_float32',
        'capytaine.green_functions.libs.XieDelhommeau_float64',
        'capytaine.green_functions.libs.XieDelhommeau_float32',
        'OCP',
    ]
)

hookconfig = dict()
hookconfig['matplotlib'] = {'backends': 'QtAgg'}

a = Analysis(
    ['PyMeshupGUI.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig=hookconfig,
    runtime_hooks=['pyi_rth_casadi.py'],
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
    name='PyMeshupGUI',
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
    icon='src/pymeshup_gui/resources/pymeshup_logo.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PyMeshupGUI',
)
