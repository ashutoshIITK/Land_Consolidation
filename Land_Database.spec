# -*- mode: python -*-

block_cipher = None


a = Analysis(['Land_Database.py'],
             pathex=['C:\\Users\\Ashutosh\\Desktop\\CE491A\\My_GUI-master'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Land_Database',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
