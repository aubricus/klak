"""Klak Utils."""
import copy
import subprocess


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


def shell(cmd, **kwargs):
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

    Returns:
        * subprocess.CompletedProcess

    Raises:
        * subprocess.CalledProcessError when encountering a
          non-zero returncode

    """
    kwargs.setdefault("shell", True)
    return run([cmd], **kwargs)
