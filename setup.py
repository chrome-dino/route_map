from setuptools import setup, find_packages

setup(
    name = "route_map",
    py_modules=['route_map'],
    packages=find_packages(where='src'),
    package_dir={'':'src'},
)
