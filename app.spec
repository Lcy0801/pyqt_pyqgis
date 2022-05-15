# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[('F:\\Program Files\\QGIS 3.16.14\\apps\\qgis-ltr\\plugins', 'qgis\\plugins'), ('F:\\Program Files\\QGIS 3.16.14\\apps\\Python39\\lib\\site-packages\\PyQt5\\*.pyd', 'PyQt5'), ('F:\\Program Files\\QGIS 3.16.14\\apps\\Qt5\\plugins\\styles', 'PyQt5\\Qt\\plugins\\styles'), ('F:\\Program Files\\QGIS 3.16.14\\apps\\Qt5\\plugins\\iconengines', 'PyQt5\\Qt\\plugins\\iconengines'), ('F:\\Program Files\\QGIS 3.16.14\\apps\\Qt5\\plugins\\imageformats', 'PyQt5\\Qt\\plugins\\imageformats'), ('F:\\Program Files\\QGIS 3.16.14\\apps\\Qt5\\plugins\\platforms', 'PyQt5\\Qt\\plugins\\platforms'), ('F:\\Program Files\\QGIS 3.16.14\\apps\\Qt5\\plugins\\platformthemes', 'PyQt5\\Qt\\plugins\\platformthemes')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='App.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
