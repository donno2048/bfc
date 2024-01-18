from setuptools import setup, find_packages
setup(
    name='bfcc',
    version='1.0.0',
    license='MIT',
    author='Elisha Hollander',
    author_email='just4now666666@gmail.com',
    description="A brainfuck compiler for 64-byte arm linux",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/bfc',
    project_urls={
        'Documentation': 'https://github.com/donno2048/bfc#readme',
        'Bug Reports': 'https://github.com/donno2048/bfc/issues',
        'Source Code': 'https://github.com/donno2048/bfc',
    },
    python_requires='>=3.0',
    packages=find_packages(),
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [ 'bfc=bfc.__main__:main' ] }
)
