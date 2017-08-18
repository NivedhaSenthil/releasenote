from setuptools import setup

setup(name='releasenote',
      version='1.0',
      description='Gives release note using git commit message and mingle cards',
      url='https://github.com/NivedhaSenthil/releasenote',
      author='Nivedha Senthil',
      author_email='nivedhasenthil@gmail.com',
      license='MIT',
      packages=['releasenote'],
      install_requires=[
          'Click','requests',
      ],
      entry_points='''
        [console_scripts]
        releasenote=releasenote:get_release_note
    ''',
      zip_safe=False)
