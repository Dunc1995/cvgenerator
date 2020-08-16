from setuptools import setup

setup(
    # Application name:
    name="Curriculum_Vitae_Generator",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Duncan Bailey",
    author_email="duncanbailey1995@gmail.com",

    # Packages
    packages=["cvgenerator"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/Dunc1995/cvgenerator",

    #
    license="LICENSE",
    description="A CV generator for those who only want to write their CV once.",
    #long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[ 'TinyDB' ],

    entry_points={
    'console_scripts': [
        'cvgenerator = cvgenerator.__main__:main'
    ]
    }
)