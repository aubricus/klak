"""Tests for `klak` CLI."""

import os
import enum
import shutil
import tempfile
import pytest
import click
import typing
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
    ClickfileSimple = MocksDir.joinpath("Clickfile.simple")
    ClickfileModules = MocksDir.joinpath("Clickfile.modules")
    Tasks = MocksDir.joinpath("tasks")


def copy(src: Path, dest: Path) -> Path:
    assert src.exists()

    if src.is_file():
        shutil.copy(str(src), str(dest))
    if src.is_dir():
        shutil.copytree(str(src), str(dest))

    assert dest.exists()
    return dest


def import_clickfile(tmp_dir: Path) -> None:
    """Import Clickfile at tmp_dir."""

    with klak.append_path(tmp_dir):
        klak.import_clickfile()


def test_command_line_interface():
    """Test the CLI."""

    runner = CliRunner()
    result = runner.invoke(cli.cli)
    assert result.exit_code == 0


def setup_test_clickfile(tmp_dir: Path) -> None:
    """Setup def test_clickfile."""

    clickfile = Paths.ClickfileSimple.value
    copy(clickfile, tmp_dir.joinpath("Clickfile"))


def test_clickfile():
    """Test Clickfile."""

    runner = CliRunner()

    with runner.isolated_filesystem() as d:
        tmp_dir = Path(d)
        setup_test_clickfile(tmp_dir)

        import_clickfile(tmp_dir)

        result = invoke("hello-world")

        assert result.exit_code == 0
        assert "hi!" in result.output


def setup_test_modules(tmp_dir: Path) -> None:
    """Setup def test_modules."""

    clickfile = Paths.ClickfileModules.value
    tasks = Paths.Tasks.value

    copy(clickfile, tmp_dir.joinpath("Clickfile"))
    copy(tasks, tmp_dir.joinpath("tasks"))


def test_modules():
    """Test Clickfile with module."""

    runner = CliRunner()

    with runner.isolated_filesystem() as d:
        tmp_dir = Path(d)
        setup_test_modules(tmp_dir)

        import_clickfile(tmp_dir)

        result = invoke("ducks", "quack")
        assert result.exit_code == 0
        assert "Quack quack!" in result.output


def test_import_missing_clickfile():
    """Test import missing Clickfile."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        with pytest.raises(click.exceptions.FileError):
            klak.import_clickfile()

