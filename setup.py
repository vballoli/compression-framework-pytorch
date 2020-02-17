import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="compression-framework-vballoli", # Replace with your own username
    version="0.0.1",
    author="Vaibhav Balloli",
    author_email="balloli.vb@gmail.com",
    description="Reproducing An End-to-End Compression Framework Based on Convolutional Neural Networks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vballoli/compression-framework-pytorch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)