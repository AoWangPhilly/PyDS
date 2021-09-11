from setuptools import setup, find_packages

setup(
    name='PyDS',
    url='https://github.com/AoWangPhilly/PyDS',
    author='Ao Wang',
    author_email='aw3338@drexel.edu',
    version='0.0.1',
    description='Python Data Structures',
    py_modules=['PyDS'],
    package_dir={'':'src'},
    packages=find_packages(where="src"),
    python_requires=">=3.9.1",
)
