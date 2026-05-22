from setuptools import setup, find_packages

setup(
    name="ayudante",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scipy"
        "scikit-learn "
    ],
    author="Arman Ghaziaskari",
    description="Librería personalizada para análisis EDA y regresiones",
)
