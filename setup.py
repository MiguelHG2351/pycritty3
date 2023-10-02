from setuptools import setup, find_packages

setup(
    name='pycritty',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Toml',
    ],
    entry_points={
        'console_scripts': [
            'pycritty = pycritty.main:main'
    ]}
)