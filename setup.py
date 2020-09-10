from setuptools import (
    setup,
    find_packages,
)


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='fuzzy-commitment',
    version='1.0.0',
    description='A fuzzy commitment scheme originally presented by Juels and Wattenberg',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author='Christian Burkert',
    url='https://github.com/abrararies/fuzzy-commitment',
    packages=find_packages(),
    install_requires=[
        'bchlib',
        'BitVector',
    ],
)
