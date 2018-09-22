.. _Click: http://click.pocoo.org/6/
.. _Issues: https://github.com/aubricus/klak/issues
.. _Python 3 Subprocess Docs: https://docs.python.org/3/library/subprocess.html
.. _Replacing Bash With Python: https://github.com/ninjaaron/replacing-bash-scripting-with-python#replacing-sed-grep-awk-etc-python-regex
.. _Delegator - Subprocess for Humans: https://github.com/kennethreitz/delegator.py

=====
Usage
=====

Create a `Clickfile`
--------------------

If you run `klak` without a `Clickfile` in the current working directory, you will probably see this:

.. code-block:: console

    Error: Could not find Clickfile!

The minimum to resolve that error would be:

.. code-block:: console

    # In the current directory
    touch Clickfile

Notes:

- `Clickfile` naming is required
- `klak` currently only supports looking for the `Clickfile` in the current directory.


Klak Command-line Interface
---------------------------

`klak` doesn't ship with any commands, but you can run the standard `--help` flag or just `klak` just the same.

.. code-block:: console

    # See available commands
    klak --help


What is a Clickfile
--------------------

A `Clickfile` is an allegory to the classic `Makefile` and is the intended destination for your project automation commands.


How to Use a Clickfile
----------------------

There's really zero magic going on here:

1. Leverage `Click`_ to build your project automation command-line interface.
2. Script Python as you normally would.

If you're unfamiliar with Python scripting, here are some resources:

- `Click`_ Docs
- `Python 3 Subprocess Docs`_
- `Replacing Bash With Python`_
- `Delegator - Subprocess for Humans`_

Example Clickfile
-----------------

Here's a simple `Clickfile` as an example. Head on over to the `Click`_ documentation to learn more about how to use `Click`_.

.. code-block:: python

    """My Project's Clickfile!"""

    from klak.cli import root
    from klak.utils import run, shell
    import click


    # `root` is provided by the `klak` package and you must
    # _at least_ append a command to it to make it available.
    @root.command()
    def hello_world():
        """Hello world."""
        click.echo("hi")


    # Create a nested command group.
    @root.group()
    def greetings():
        """Greeting commands"""
        pass


    # Add a new command to the new group.
    @greetings.command()
    @click.option("--name", help="Who are you greeting?", required=True)
    def say_hello(name):
        """Say hello to someone."""
        click.echo("Hello, " + name)


    # Add another command!
    @greetings.command()
    @click.option("--name", help="Who are you wishing farewell?", required=True)
    def say_goodbye(name):
        """Say goodbye to someone."""
        click.echo("Goodbye, " + name)

This file results in the following help string:

.. code-block:: console

    Usage: klak [OPTIONS] COMMAND [ARGS]...

    Click n' Klak.

    Options:
    --help  Show this message and exit.

    Commands:
    hello_world  Hello World
    greetings    Greeting commands

Enable Bash Completions
-----------------------

You can enable Bash Completions in the standard `Click`_ way:

.. code-block:: console

    eval "$(_KLAK_COMPLETE=source klak)"

* See `Click Bash Complete Docs <http://click.pocoo.org/6/bashcomplete/>`_
