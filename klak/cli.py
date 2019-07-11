"""Console script for klak."""

import sys
import logging
import click
from pathlib import Path
from .klak import import_clickfile, get_version, append_path


log = logging.getLogger(__name__)


@click.group(invoke_without_command=True)
@click.option("-v", "--version", is_flag=True, help="Print current version.")
@click.pass_context
def cli(ctx, version: bool) -> None:
    """Click n' Klak."""
    if ctx.invoked_subcommand is None and version:
        click.secho(get_version(), fg="green")
    elif ctx.invoked_subcommand is None:
        click.secho(ctx.get_help())


def main() -> None:
    """Console script for klak."""

    with append_path(Path.cwd()):
        run()


def run() -> None:
    try:
        import_clickfile()
    except click.exceptions.FileError as exception:
        click.secho("\n{error}\n".format(error=str(exception)), fg="red", bold=True)
        sys.exit(1)

    sys.exit(cli())


if __name__ == "__main__":
    main()  # pragma: no cover
