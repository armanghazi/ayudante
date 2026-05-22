from setuptools import setup, find_packages

setup(
    name="ayudante",
    version="0.2.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scipy",
        "scikit-learn"
    ],
    author="Arman Ghaziaskari",
    description="Paquete para EDA, regresiones y evaluación automática de modelos.",
    url="https://github.com/armanghazi/ayudante",
)
