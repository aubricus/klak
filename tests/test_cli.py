#!/usr/bin/env python
# pylint: disable=no-member
# -*- coding: utf-8 -*-

"""Tests for `klak` CLI."""

import os
import enum
import shutil
import tempfile
import pytest
import click
from click.testing import CliRunner
from path import Path
from klak import klak
from klak import cli


def invoke(*args):
    """Provide convenience call to test klak cli."""
    runner = CliRunner()
    return runner.invoke(cli.root, args)


class Paths(enum.Enum):
    """Test Paths."""

    FilePath = Path(__file__)
    FileDir = FilePath.dirname()
    MocksDir = Path(os.path.join(FileDir, "mocks"))
    MockClickfilePath = Path(os.path.join(MocksDir, "Clickfile"))

    @staticmethod
    def get_clickfile_path() -> Path:
        """Return MockClickfilePath.value."""
        return Paths.MockClickfilePath.value


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.root)
    assert result.exit_code == 0


def test_clickfile():
    """Test Clickfile."""
    runner = CliRunner()
    with runner.isolated_filesystem() as temp_dir:
        _tmp = Path(temp_dir)
        _clickfile = Paths.get_clickfile_path().copy(_tmp)

        assert _clickfile.isfile()

        # Call import_clickfile manually
        # since the CliRunner cannot use the runner to invoke
        # cli.main directly.
        cli.import_clickfile()

        # Our custom command hello_world should now be available
        result = invoke("hello_world")

        assert result.exit_code == 0
        assert "hi!" in result.output


def test_import_missing_clickfile():
    """Test import missing Clickfile."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        with pytest.raises(click.exceptions.FileError):
            cli.import_clickfile()


def test_missing_clickfile():
    """Test missing Clickfile."""
    returncode = cli.main()
    assert returncode == 1
