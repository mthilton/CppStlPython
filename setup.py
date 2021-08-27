import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CppStlPython-mthilton",
    version="0.1.0",
    author="Matthew Hilton",
    author_email="redacted@example.com",
    description="A port of the C++ Standard Template Library to Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mthilton/CppStlPython",
    project_urls={
        "Bug Tracker": "https://github.com/mthilton/CppStlPython/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "CppStlPython"},
    packages=setuptools.find_packages(where="CppStlPython"),
    python_requires=">=3.5",
)
