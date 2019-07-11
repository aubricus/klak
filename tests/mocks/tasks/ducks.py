"""Ducks commands."""

import logging
import click
from klak.cli import cli


log = logging.getLogger(__name__)


@cli.group()
def ducks() -> None:
    """Ducks commands!"""


@ducks.command()
def quack() -> None:
    """Quack quack!"""
    click.echo("Quack quack!")
