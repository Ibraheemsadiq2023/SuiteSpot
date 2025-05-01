from setuptools import setup, find_packages

setup(
    name="SuiteSpot",
    version="1.0.0",
    author="Your Name",
    description="Hotel Management System using Tkinter & MySQL",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "mysql-connector-python",
        "Pillow"
    ],
    entry_points={
        "console_scripts": [
            "suitespot=main:main"
        ]
    },
)
