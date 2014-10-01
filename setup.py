#!python
# coding=utf-8
import os,sys
from cx_Freeze import setup, Executable

setup(
    name='SRun3K',
    description='SRun3K',
    executables=[
        Executable(
            script='SRun3K.py',
            )
        ],
    options=dict(
        build_exe=dict(
            #build_exe='build/SRun3K',
            optimize=2,
			base='Win32GUI',
			compressed=True,
            copy_dependent_files=True,
			create_shared_zip=False,
			append_script_to_exe=True,
            icon=os.path.expanduser('internet1.ico'),
            )
        )
    )
