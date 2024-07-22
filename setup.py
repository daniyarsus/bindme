from setuptools import setup, find_packages

setup(
    name="bindme",
    version="0.1.0",
    author="daniyarsus",
    author_email="daniyar.kanu@mail.ru",
    description="Simple DI Framework for Python 3.x 🐍",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/daniyarsus/bindme",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
