.. _Click: http://click.pocoo.org/6/
.. _Issues: https://github.com/aubricus/klak/issues

=====
Usage
=====

Create a `Clickfile`
--------------------

If you run `klak` without a `Clickfile` in the current working directory, you will probably see this:

.. code-block:: bash

    Error: Could not find Clickfile!

The minimum to resolve that error would be:

.. code-block:: bash

    touch Clickfile


Klak CLI
--------

`klak` doesn't ship with any commands, but you can run the standard `--help` flag or just `klak` just the same.

.. code-block:: bash

    # See available commands
    klak --help


Adding Commands
---------------

Here's a simple `Clickfile` as an example. Head on over to the `Click`_ documentation to learn more about how to use `Click`_.

**Note:** This package is still new, and I have not tested it with *every aspect of Click*. Report bugs on GitHub `Issues`_ and don't forget to read the guide to `Contributing <https://klak.readthedocs.io/en/latest/contributing.html>`_.

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


    # `klak` also ships with two tiny wrappers around
    # subprocess; `run` and `shell`
    # `run` simply calls `subprocess.run` with `check=True` by default
    # `shell` delegates to `run` but also sets `shell=True` by default
    @root.command()
    def ls():
        """Example utils.shell` usage."""
        shell("ls -la")

    @root.command()
    def ls2():
        """Example `utils.run` usage."""
        run(["ls", "-la"])

Enable Bash Completions
-----------------------

You can enable Bash Completions in the standard `Click`_ way:

.. code-block:: bash

    eval "$(_KLAK_COMPLETE=source klak)"

* See `Click Bash Complete Docs <http://click.pocoo.org/6/bashcomplete/>`_
