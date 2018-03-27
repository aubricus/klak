"""Klak Utils."""
import copy
import subprocess
import click


def run(*args, **kwargs):
    """
    Wrap subprocess.run for compat and fun.

    This method passes through `*args` and `**kwargs`
    so you can use it just like `subprocess.run`.

    Notes:
        * `check=True` ensures CalledProcessError is raised on non-zero
          exit codes.

    Returns:
        * subprocess.CompletedProcess

    Raises:
        * subprocess.CalledProcessError when encountering a
          non-zero returncode.

    """
    copy_kwargs = copy.deepcopy(kwargs)
    copy_kwargs.setdefault("check", True)
    return subprocess.run(*args, **copy_kwargs)


def shell(cmd, handle_errors=True, **kwargs):
    """
    Wrap subprocess.run for compat and fun.

    Sets `shell=True` by default and accepts a
    single cmd_str in lieu of the usual array.

    Use `utils.run` instead of you want a to use subprocess
    in the standard way.

    Example::

        shell("uname -a")

    Notes:
        * `shell=True` eases calling arbitrary commandline,
          but should be used only when necessary.
          See: http://bit.ly/2pvxhFZ
        * Will forward stderr to console if handle_errors=True

    Returns:
        * subprocess.CompletedProcess

    Raises:
        * subprocess.CalledProcessError when encountering a
          non-zero returncode and handle_errors=False

    """
    kwargs.setdefault("shell", True)

    if handle_errors:
        kwargs["stderr"] = subprocess.PIPE

    try:
        return run([cmd], **kwargs)
    except subprocess.CalledProcessError as exception:
        if handle_errors:
            return echo_stderr(exception)
        else:
            raise


def echo_stderr(exception):
    """Echo stderr instead of returning a non-zero exitcode."""
    if exception.stderr:
        return click.echo(exception.stderr.decode("utf-8"))
    else:
        return click.echo(str(exception))
