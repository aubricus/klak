[click]: https://click.palletsprojects.com/en/master/
[poetry]: https://github.com/sdispater/poetry
[click setuptools integration]: https://click.palletsprojects.com/en/master/setuptools/
[click bash completions]: https://click.palletsprojects.com/en/master/bashcomplete/#activation

# Klak

[![pypi](https://img.shields.io/pypi/v/klak.svg)](https://pypi.python.org/pypi/klak)
[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![travis-ci](https://img.shields.io/travis/aubricus/klak.svg)](https://travis-ci.org/aubricus/klak)
[![docs](https://readthedocs.org/projects/klak/badge/?version=latest)](https://klak.readthedocs.io/en/latest/?badge=latest)
[![docs](https://readthedocs.org/projects/klak/badge/?version=latest)](https://klak.readthedocs.io/en/latest/?badge=latest)

<!-- NOTE: If you update this line, update pyproject.toml -->

> `klak` provides the ergonoics of a project Makefile with the easy of Python and power of [Click].

## Table of Contents

-   [Background](#background)
-   [Install](#install)
-   [Usage](#usage)
-   [Maintainers](#maintainers)
-   [Contributing](#contributing)
-   [License](#license)

## Background

Automating project tasks with Makefiles is simple and `make <command>` is _very ergonomic_. Unfortunately, Make syntax is archaic and ill-suited for self-documenting, full-featured command-line interfaces.

Python, however, is built for scripting and paired with [Click] it's easy great command-line interfaces!

This is where Klack comes in. Klak provides a _very minimal_ wrapper around Click which allows it to import a local **Clickfile** providing the ergonomics of a project Makefile, i.e., `klak <command>`, but also provides the ease of Python and power of Click.

## Features

-   Exposes a global interface, `klak`.
-   Auto-loads a local **Clickfile** (form the curren working directory)
-   Allows users to easily append commands to the default, Klak CLI root
-   Allows users to easily append sub-command groups
-   Compatible with [Click Bash completions]
-   Ships with [Click] setup using the recommended [Click Setuptools Integration]

## Install

### Stable Release

```bash
# NOTE: This is the recommended method of install
pip install klak
```

### From Source

> Klak uses [Poetry] to manage depdencies and distribution (in lieu of setuptools).

```bash
# NOTE: Clone the public repository
git clone git://github.com/aubricus/klak

# NOTE: or download the tarball
curl  -OL https://github.com/aubricus/klak/tarball/master

# NOTE: Once the source is downloaded
poetry install
```

## Usage

Klak provides a simple global entry point `klak`. What happens next is up to you!

```bash
# See full usage
klak --help
```

## Maintainers

[@aubricus](https://github.com/aubricus)

## Contributing

See [the contributing file](CONTRIBUTING.md)!

PRs accepted!

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

[MIT © 2018, 2019 aubricus@gmail.com](./LICENSE)
