# History

## 0.4.3 (2019-07-10)

-   Fixed bug when running `klak --version`
-   Clickfile can now import modules from packages in the same directory

## 0.4.2 (2019-06-21)

-   Add missing toml dependency

## 0.4.1 (2019-06-21)

-   Revised README.md copy
-   Fix typos in README.md
-   Revised CONTRIBUTING.md copy
-   Add additional information to pyproject.toml

## 0.4.0 (2019-06-21)

-   Refactor Klak distribution
-   Refactor docs structure and content
-   Renamed `cli.root` to `cli.cli`. Users should now import `from klak.cli import cli` (this is a breaking change)
-   Added a `-v/--version` flag to print the current version
-   Removed dependency on path.py

## 0.3.3 (2018-09-23)

-   Forgot to update HISTORY.rst!

## 0.3.2 (2018-09-23)

-   Fix bumpversion config

## 0.3.1 (2018-09-23)

-   Fix version formatting causing PyPi upload to fail

## 0.3.0 (2018-09-22)

-   Removed klak.utils.run
-   Removed klak.utils.shell
-   Refactored to use Python Black formatting
-   Updated docs

## 0.2.4 (2018-09-22)

-   Fix pylint errors in setup.py
-   Fix license in setup.py
-   Fix klak spelling in CONTRIBUTING.md
-   Update pytest from 3.5.0 to 3.8.1
-   Update sphinx from 1.7.2 to 1.8.1
-   Update tox from 2.9.1 to 3.4.0
-   Update mypy from 0.580 to 0.630
-   Update autopep8 from 1.3.5 to 1.4
-   Update watchdog from 0.8.3 to 0.9.0
-   Update pylint from 1.8.3 to 2.1.1
-   Update pip from 9.0.3 to 18.0
-   Update wheel from 0.30.0 to 0.31.1
-   Update README.rst

## 0.2.3 (2018-03-30)

-   Convert LICENSE to MIT
-   Update autopep8 from 1.3.4 to 1.3.5

## 0.2.2 (2018-03-26)

-   Make `utils.shell` a little nicer to use

## 0.2.1 (2018-03-26)

-   Fix missing `path.py` dependency
-   Update mypy from 0.570 to 0.580
-   Update pytest from 3.4.2 to 3.5.0

## 0.2.0 (2018-03-22)

-   Add `Clickfile` loading
-   Add `utils.run`, `utils.shell`
-   Update docs

## 0.1.0 (2018-03-21)

-   First release on PyPI.
