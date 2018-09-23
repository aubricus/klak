# -*- coding: utf-8 -*-

"""Console script for klak."""
import sys
import os
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader
import click
from path import Path


def import_module_from_file(module_name, path):
    """Load a modules from a raw file path."""
    loader = SourceFileLoader(module_name, path)
    spec = spec_from_loader(module_name, loader)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def import_clickfile():
    """Import a python file named Clickfile from os.getcwd()."""
    cwd = Path(os.getcwd())
    clickfile_path = Path(os.path.join(cwd, "Clickfile"))

    if clickfile_path.isfile():
        return import_module_from_file("clickfile_cmds", str(clickfile_path))
    else:
        raise click.exceptions.FileError(
            clickfile_path, hint="Error: Could not find Clickfile!"
        )


@click.group()
def root():
    """Click n' Klak."""
    return 0


def main():
    """Console script for klak."""
    try:
        import_clickfile()
    except click.exceptions.FileError as exception:
        click.secho("\n{error}\n".format(error=str(exception)), fg="red", bold=True)
        return 1
    return root()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
