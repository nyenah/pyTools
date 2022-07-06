from setuptools import setup, find_packages

setup(
    name='pyToolsWaterGAP',
    version='0.1',
    author="TT,RR",
    packages=find_packages(),
    package_data={'': ['*.txt']},
    include_package_data=True,
    install_requires=['pandas', 'numpy', 'matplotlib', 'geopandas', 'xarray', 'cytoolz', 'dask', 'cartopy']
)
