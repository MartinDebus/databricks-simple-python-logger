from setuptools import setup, find_packages

setup(
    name="DatabricksLogger",
    version="0.1",
    author="Martin Debus",
    author_email="martin.debus@snowglobe.ai",
    description="A simple Databricks Logger",
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    packages=find_packages(),
)