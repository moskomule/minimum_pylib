# minimum_pylib

[![CircleCI](https://circleci.com/gh/moskomule/minimum_pylib.svg?style=svg)](https://circleci.com/gh/moskomule/minimum_pylib)

[Documents](https://moskomule.github.io/minumum_pylib)

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
* Do not forget to add `index.html` in `docs` directory.
* Deployed to https://moskomule.github.io/PROJECT.

### Theme

ReadDoc's theme is awesome. Install it with `pip install sphinx_rtd_theme` and add the followings to `conf.py`.

```python
import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```