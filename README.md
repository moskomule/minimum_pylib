# minimum_pylib

![](https://github.com/moskomule/minimum_pylib/workflows/pytest/badge.svg) [![CircleCI](https://circleci.com/gh/moskomule/minimum_pylib.svg?style=svg)](https://circleci.com/gh/moskomule/minimum_pylib)
[![document](https://img.shields.io/static/v1?label=doc&message=minimum_pylib&color=blue)](https://moskomule.github.io/minimum_pylib)

This repository contains minimum Python library with tests and documentations.

## Package

Package can be installed by cloning and `python setup.py install`, or `pip install git+https://github.com/USERNAME/REPOSITORY.git`.

## Tests

[`tests`](./tests) contains tests using `pytest`.

Tests are run automatically using GitHub Actions (see `.github/wokflows/action.yml`) and CircleCI (see `.circleci/config.yml`). To enable CicleCI, login and add repository in `Add project` page.


## Documents

[`docs`](./docs) contains documents using `Sphinx`. Documents are automatically generated using Github Actions (see `.github/workflows/ghpage.yml`) and deployed to `https://USERNAME.github.io/REPOSITORY`. First configure in the repository's `Settings/GitHub Pages`.
