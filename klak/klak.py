"""Main module."""

import os
import logging
import click
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader
from typing import MutableMapping
from pathlib import Path


log = logging.getLogger(__name__)
VERSION = "0.4.3"


def get_version() -> str:
    """Return current klak version."""
    return VERSION


def import_clickfile():
    """Import a python file named Clickfile from os.getcwd()."""
    cwd = Path.cwd()
    clickfile_path = cwd.joinpath("Clickfile")

    if clickfile_path.is_file():
        return import_module_from_file("Clickfile", str(clickfile_path))
    else:
        raise click.exceptions.FileError(
            str(clickfile_path), hint="Error: Could not find Clickfile!"
        )


def import_module_from_file(module_name, path):
    """Load a modules from a raw file path."""
    loader = SourceFileLoader(module_name, path)
    spec = spec_from_loader(module_name, loader)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    return module
