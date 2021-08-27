import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CppStlPython",
    version="0.1.1",
    author="@mthilton",
    description="A port of the C++ Standard Template Library to Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Source": "https://github.com/mthilton/CppStlPython",
        "Bug Tracker": "https://github.com/mthilton/CppStlPython/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "CppStlPython"},
    packages=setuptools.find_packages(where="CppStlPython"),
    python_requires=">=3.5",
    license='GPL-3.0'
)
