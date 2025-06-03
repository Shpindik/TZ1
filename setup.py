from setuptools import setup, find_packages

setup(
    name="TZ1",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.7',
    author="Shp1ndik",
    author_email="@Shp1ndik",
    description="Библиотека для вычисления площадей фигур",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Shpindik/TZ1",  # если хочешь выложить
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
