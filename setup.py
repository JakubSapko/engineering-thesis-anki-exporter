from setuptools import find_packages, setup

setup(
    name="engineering-thesis-cli",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            "etae = etae.main:cli",
        ],
    },
)
