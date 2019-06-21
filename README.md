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

> Klak provides the ergonoics of a project Makefile with the ease of Python and power of [Click].

## Table of Contents

-   [Background](#background)
-   [Install](#install)
-   [Usage](#usage)
-   [Maintainers](#maintainers)
-   [Contributing](#contributing)
-   [License](#license)

## Background

Automating project tasks with Makefiles is convenient and the simple interface, `make <command>`, is _very ergonomic_. Unfortunately, Make syntax is archaic and ill-suited for self-documenting, full-featured command-line interfaces.

Python—however—is built for scripting and paired with [Click] it's easy great command-line interfaces!

Enter Klak.

Klak provides a _very minimal_ wrapper around Click allowing the import of a local **Clickfile** providing the ergonomics of a project Makefile—`klak <command>`—but also provides the ease of Python and power of Click.

### Features

-   Exposes a global interface, `klak`.
-   Auto-loads a local **Clickfile** (form the current working directory)
-   Easily append commands to the CLI root
-   Easily append sub-command groups
-   [Click Bash completions]
-   Ships with [Click] already setup using the recommended [Click Setuptools Integration]

## Install

### Stable Release

```bash
# NOTE: This is the recommended method of installation.
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

To get started with Klak you must add a **Clickfile**. Here's an example **Clickfile** to get started:

```python
"""Example Clickfile."""

import logging
import click
from klak.cli import cli


log = logging.getLogger("Clickfile")


# -------------------------------------
# Examples
# -------------------------------------


# Example: Add a command
@cli.command()
@click.argument("name")
def greet(name):
    """Greet someone."""
    click.secho(f"Hello, {name}")


# Example: Add a group and sub-command.
@cli.group()
def humans():
    """Humans command group."""
    pass


@humans.command(name="count")
def humans_count():
    """Count all the humans."""
    click.secho("Over 9000!!!")

```

Once your **Clickfile** is ready you can access commands through `klak`.

```bash
$ klak --help
```

## Support

This project is a hobby/passion project which I maintain in my own time.

### Python

-   Python 3.5+

### OS

-   Linux ✓
-   MacOS ✓
-   Windows ✘ (any volunteers?)

## Maintainers

[@aubricus](https://github.com/aubricus)

## Contributing

See [the contributing file](CONTRIBUTING.md)!

PRs accepted!

Please note, if editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

[MIT © 2018, 2019 aubricus@gmail.com](./LICENSE)
