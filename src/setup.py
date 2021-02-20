
from setuptools import find_packages, setup

setup(
  name='src',
  packages=find_packages(include=['src']),
  version='0.1.0',
  description='Quantum computing sim library',
  license='MIT',
  install_requires=['typing'],
)
