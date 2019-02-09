# minimum_pylib

[![CircleCI](https://circleci.com/gh/moskomule/minimum_pylib.svg?style=svg)](https://circleci.com/gh/moskomule/minimum_pylib)

**A quasi-minimum template for Python libraries**

## Package

Install with `python setup.py install` or `pip install git+https://github.com/moskomule/minimum_pylib`.

## Test

Use `pytest`.

## CI

* Go to  [CircleCI](https://circleci.com/)'s `Add Projects` page, select the repository and set up project.

## Documents

Use Sphinx. (`pip install Sphinx`)

```bash
mkdir docs
sphinx-quickstart -q --project=PROJECT --author=AUTHOR --ext-autodoc --makefile --sep docs

# fix conf.py and index.rst
sphinx-apidoc -f -o ./docs/source PROJECT
cd docs
touch .nojekyll
make html
```

* Go to the project page's `Settings/GitHub Pages`.