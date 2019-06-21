"""Tests for `klak` CLI."""

import os
import enum
import shutil
import tempfile
import pytest
import click
from pathlib import Path
from click.testing import CliRunner
from klak import klak, cli


def invoke(*args):
    """Provide convenience call to test klak cli."""
    runner = CliRunner()
    return runner.invoke(cli.cli, args)


class Paths(enum.Enum):
    """Test Paths."""

    FilePath = Path(__file__)
    FileDir = FilePath.parent
    MocksDir = FileDir.joinpath("mocks")
    MockClickfilePath = MocksDir.joinpath("Clickfile")

    @staticmethod
    def get_clickfile_path() -> Path:
        """Return MockClickfilePath.value."""
        return Paths.MockClickfilePath.value


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.cli)
    assert result.exit_code == 0


def test_import_clickfile():
    """Test Clickfile."""
    runner = CliRunner()
    with runner.isolated_filesystem() as temp_dir:
        _tmp = Path(temp_dir)

        shutil.copy(str(Paths.get_clickfile_path()), str(_tmp))

        _clickfile = _tmp.joinpath("Clickfile")
        assert _clickfile.is_file()

        # Call import_clickfile manually
        # since the CliRunner cannot use the runner to invoke
        # cli.main directly.
        klak.import_clickfile()

        # Our custom command hello_world should now be available
        result = invoke("hello-world")

        assert result.exit_code == 0
        assert "hi!" in result.output


def test_import_missing_clickfile():
    """Test import missing Clickfile."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        with pytest.raises(click.exceptions.FileError):
            klak.import_clickfile()

