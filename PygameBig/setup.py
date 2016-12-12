from cx_Freeze import setup, Executable

executables = [
    Executable('bigGame.py')
]

setup(name='bigGame',
      version='0.1',
      description='PygameBig script',
      executables=executables
      )
