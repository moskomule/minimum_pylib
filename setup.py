from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("requirements.txt") as f:
    requirements = f.read().split()

setup(name="foo",
      version="0.0.1",
      author="moskomule",
      author_email="hataya@nlab.jp",
      packages=find_packages(exclude=["test"]),
      url="https://github.com/moskomule/minimum_pylib",
      description="A quasi minimum template for Python libraries",
      long_description=readme,
      license="BSD",
      install_requires=requirements,
      )
