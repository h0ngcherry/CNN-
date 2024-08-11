# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['demo.py'],
    pathex=['E:/code/deep/crnn.pytorch-master'],
    binaries=[],
    datas=[
        ('E:/code/deep/crnn.pytorch-master/data', 'data')
    ],
    hiddenimports=['torch','torch.autograd'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='crnn_pytorch',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='crnn_pytorch'
)