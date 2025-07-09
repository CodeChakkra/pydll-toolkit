from setuptools import setup, find_packages

setup(
    name="pydlltoolkit",
    version="0.1.0",
    description="Python DLL Injection Toolkit",
    author="Your Name",
    author_email="ttenwi888@gmail.com",
    url="https://github.com/CodeChakkra/pydll-toolkit",
    packages=find_packages("src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
    install_requires=[
        "pywin32>=300",
    ],
)
