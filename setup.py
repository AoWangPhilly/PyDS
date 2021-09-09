from setuptools import setup, find_packages

setup(
    name='PyDS',
    version='0.0.1',
    description='Python Data Structures',
    py_modules=['PyDS'],
    package_dir={'':'src'},
    packages=find_packages(where="src"),
    python_requires=">=3.9.1",
)

# python setup.py bdist_wheel
# pip install -e .