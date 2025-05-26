from setuptools import setup, find_packages

setup(
    name = "vdot",
    version = "0.1.0",
    description = "A Python component that reads .dat files and calculates"
                  "scalar products. If -f parameter is used, then the scalar"
                  "product is displayed in specified format.",
    author = "Danielė Stasiūnaitė",
    author_email = "danielestasiunaite@gmail.com",
    url = "https://github.com/dansta0804/component_scalars.git",
    packages = find_packages(),
    install_requires = [],
    entry_points = {
        "console_scripts": [
            "vdot = vdot.main:main",
        ],
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)