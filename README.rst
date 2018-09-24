.. _Python: http://www.python.org/
.. _Click: http://click.pocoo.org/6/
.. _Click Setuptools Integration: http://click.pocoo.org/6/setuptools/
.. _Documentation: https://klak.readthedocs.io
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _Bash completions: https://klak.readthedocs.io/en/latest/usage.html#enable-bash-completions
.. _Python 3 Subprocess Docs: https://docs.python.org/3/library/subprocess.html
.. _Replacing Bash With Python: https://github.com/ninjaaron/replacing-bash-scripting-with-python#replacing-sed-grep-awk-etc-python-regex
.. _Delegator - Subprocess for Humans: https://github.com/kennethreitz/delegator.py


=====
Klak
=====

.. image:: https://img.shields.io/pypi/v/klak.svg
        :target: https://pypi.python.org/pypi/klak

.. image:: https://img.shields.io/travis/aubricus/klak.svg
        :target: https://travis-ci.org/aubricus/klak

.. image:: https://readthedocs.org/projects/klak/badge/?version=latest
        :target: https://klak.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/aubricus/klak/shield.svg
     :target: https://pyup.io/repos/github/aubricus/klak/
     :alt: Updates

---------------------------------------

Support
-------

* Python 3.6.x
* Python 3.5.x

Documentation
--------------
* See the full `Documentation`_

About
-----

*"Clak [klak]: A sharp sound or series of sounds."*

**Click n' Klak**!

`klak` is a minimal-wrapper around `Click`_ to enhance the simplicity of a project `Makefile` with Python.

Features
========

* Ship with `Click`_ setup with the recommended `Click Setuptools Integration`_.
* Provide a global CLI interface, `klak`.
* Auto-load a `Clickfile` in the current working directory.
* Easily append commands to the available `cli.root` group, `klak` (through `Click`_).
* Easily append nested groups and commands as well (through `Click`_).
* Easily provide `Bash completions`_ (through `Click`_).

License
--------

MIT License

Credits
-------

* This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.


