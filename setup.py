from setuptools import setup, find_packages

setup(
    name="jsonplaceholder-client",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'python-dotenv>=0.19.0',
    ],
)
