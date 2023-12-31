from setuptools import setup, find_packages
setup(
name="androanalyzer",
version="1.0",
packages=find_packages(),
install_requires=[
"pandas", # Add other dependencies as needed
],
author="Hao Ho-Minh",
author_email="",
description="AndroAnalyzer Dataloader is a library installed to facilitate the quick download and loading of data for researchers, allowing them to access this data as swiftly as possible.",
long_description="AndroAnalyzer Dataloader is a compilation of four publicly available datasets that we used in our paper, including Bataci's dataset, AndroVul dataset, Drebin-215 dataset, Malgenome-215 dataset, and a feature dataset collected by our proposed framework (which includes CSV files and sha256 hashes).",
long_description_content_type="text/markdown",
url="https://github.com/HoMinhHao/AirQualityDataloader",
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
)