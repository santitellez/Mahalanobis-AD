import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mahala_ad", # Replace with your own username
    version="0.0.2",
    author="Santi Tellez",
    author_email="tellezsanti@gmail.com",
    description="Mahalanobis Anomaly Detection for Multivariate Time Series",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tellezsanti/Mahalanobis-AD",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)