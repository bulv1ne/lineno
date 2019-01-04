#!/usr/bin/env python
from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

setup(
    name="lineno",
    version="0.2.1",
    description="",
    long_description=readme + "\n\n" + history,
    author="Niels Lemmens",
    author_email="draso.odin@gmail.com",
    url="https://github.com/bulv1ne/lineno",
    packages=find_packages(include=["lineno"]),
    entry_points={"console_scripts": ["lineno=lineno.cli:main"]},
    include_package_data=True,
    license="MIT license",
    zip_safe=False,
    keywords="lineno",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    test_suite="tests",
)
