import setuptools

long_description = open("README.md").read()

setuptools.setup(
    name="minima-test-zbyszek",
    version="0.0.1",
    author="Zbigniew Jędrzejewski-Szmek",
    author_email="zbyszek@in.waw.pl",
    description="A library to find function maxima",

    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/potsdam-python-workshop/testing",
    packages=['maxima'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
