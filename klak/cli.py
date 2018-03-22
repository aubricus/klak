# -*- coding: utf-8 -*-

"""Console script for klak."""
import sys
import os
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader
import click


def import_module_from_file(module_name, path):
    """Load a modules from a raw file path."""
    loader = SourceFileLoader(module_name, path)
    spec = spec_from_loader(module_name, loader)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def import_clickfile():
    """Import a python file named Clickfile from os.getcwd()."""
    cwd = os.getcwd()
    clickfile_path = os.path.realpath(os.path.join(cwd, "Clickfile"))
    if os.path.isfile(clickfile_path):
        return import_module_from_file("usr_cmd", clickfile_path)


@click.group()
def root():
    """Click n' Klak"""
    return 0


def main():
    """Console script for klak."""
    import_clickfile()
    return root()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
