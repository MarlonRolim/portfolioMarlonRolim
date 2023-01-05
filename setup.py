
import setuptools

setuptools.setup(
    name="notion",
    version="0.0.25",
    author="Jamie Alexandre",
    author_email="jamalex+python@gmail.com",
    description="Unofficial Python API client for Notion.so",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mathix420/notion-py",
    install_requires=open('requirements.txt').read().split('\n'),
    include_package_data=True,
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
