"""Main module."""

import os
import logging
import toml
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader
from typing import MutableMapping
from pathlib import Path


log = logging.getLogger(__name__)


def get_version() -> str:
    """Return current klak version."""
    pyproject_path = Path(__file__).parent.parent.joinpath("pyproject.toml")
    if pyproject_path.exists():
        pyproject = toml.load(str(pyproject_path))
        version = pyproject["tool"]["poetry"]["version"]
    else:
        log.error("Could not read pyproject.toml to determine version.")
        version = "Unknown"

    return version


def import_clickfile():
    """Import a python file named Clickfile from os.getcwd()."""
    cwd = Path.cwd()
    clickfile_path = cwd.joinpath("Clickfile")

    if clickfile_path.is_file():
        return import_module_from_file("Clickfile", str(clickfile_path))
    else:
        raise click.exceptions.FileError(
            clickfile_path, hint="Error: Could not find Clickfile!"
        )


def import_module_from_file(module_name, path):
    """Load a modules from a raw file path."""
    loader = SourceFileLoader(module_name, path)
    spec = spec_from_loader(module_name, loader)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    return module
