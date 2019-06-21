"""Console script for klak."""

import sys
import logging
import click
from .klak import import_clickfile, get_version


log = logging.getLogger(__name__)


@click.group(invoke_without_command=True)
@click.option("-v", "--version", is_flag=True, help="Print current version.")
@click.pass_context
def cli(ctx, version):
    """Click n' Klak."""
    if ctx.invoked_subcommand is None and version:
        click.secho(get_version(), fg="green")

    return 0


def main():
    """Console script for klak."""
    try:
        import_clickfile()
    except click.exceptions.FileError as exception:
        click.secho("\n{error}\n".format(error=str(exception)), fg="red", bold=True)
        return 1
    return cli()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
