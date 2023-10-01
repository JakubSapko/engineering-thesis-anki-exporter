from setuptools import setup

setup(
    name="engineering-thesis-cli",
    version="0.1",
    py_modules=["main"],
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            "etae = main:cli",
        ],
    },
)
