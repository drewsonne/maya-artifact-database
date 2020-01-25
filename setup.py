from setuptools import setup

setup(
    name='maya-artifact-database',
    version='0.1.0',
    packages=[''],
    url='https://github.com/drewsonne/maya-artifact-database',
    license='LGLPv3',
    author='Drew J. Sonne',
    author_email='drew.sonne@gmail.com',
    description='A machine-readable database of maya artifact metadata',
    install_requires=[
        'pandas',
        'beautifulsoup4',
        'click'
    ]
)
