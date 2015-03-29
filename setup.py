#try:
#    from setuptools import setup
#except ImportError:
#    from distutils.core import setup

from setuptools import setup, find_packages

setup(
    name='ag101',
    version='0.0.1dev',
    description='learning python agilely',
    author='AgilearningIO',
    author_email="dev@agilearning.io",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        "pandas"
    ],
)
