try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


setup(
    name = 'my_first_python_app',
    version = '0.0.1',
    packages=['roboter', 'roboter.models', 'roboter.controller', 'roboter.views'],
    package_data={ 'roboter': ['templates/*.txt'] },
    url='',
    license='',
    author='masatoshi0929',
    author_email='',
    long_description=open('README.txt').read(),
)
