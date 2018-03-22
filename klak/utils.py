"""Klak Utils."""
import copy
import subprocess


def run(*args, **kwargs):
    """
    Wrap subprocess.run for compat and fun.

    Create a wrapper for subprocess.run thats compatible back to
    python 3.4 (will default to an equivalent call to check_call
    if subprocess.run does not exist).

    This method passes through *args and **kwargs
    so you can use it just like subprocess.run (py3.6)
    or subprocess.check_call (py3.4).

    Notes:
        * check=True ensures CalledProcessError is raised on non-zero
          exit codes.

    Returns:
        * subprocess.CompletedProcess

    Raises:
        * subprocess.CalledProcessError when encountering a
          non-zero returncode

    """
    copy_kwargs = copy.deepcopy(kwargs)
    copy_kwargs.setdefault("check", True)
    return subprocess.run(*args, **copy_kwargs)


def shell(args, **kwargs):
    """
    Wrap subprocess.run with shell=True set by default.

    `sh` short for "shell". Accepts a single cmd_str
    in lieu of the usual array.

    Use `run` instead of you want a to use subprocess
    in the standard way.

    Example:
        sh("uname -a")

    Notes:
        * shell=True eases calling arbitrary commandline,
          but should be used only when necessary.
          See: http://bit.ly/2pvxhFZ

    Returns:
        * subprocess.CompletedProcess

    Raises:
        * subprocess.CalledProcessError when encountering a
          non-zero returncode

    """
    kwargs.setdefault("shell", True)
    return run([args], **kwargs)
