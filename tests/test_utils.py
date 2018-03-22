#!/usr/bin/env python
# pylint: disable=no-member
# -*- coding: utf-8 -*-

"""Tests for `klak` Utils."""
from klak.utils import run, shell


def test_run():
    """Test subprocess.run wrapper."""
    completed = run(["uname", "-a"])
    assert completed.returncode == 0


def test_shell():
    """Test subprocess.run with shell=True wrapper."""
    completed = shell("uname -a")
    assert completed.returncode == 0
