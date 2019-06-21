[gitflow]: https://github.com/nvie/gitflow/ "GitFlow source code."

# Contributing

## Table of Contents

-   [Types of Contributions](#types-of-contributions)
    -   [Report Bugs](#report-bugs)
    -   [Fix Bugs](#fix-bugs)
    -   [Implement Features](#implement-features)
    -   [Write Documentation](#write-documentation)
    -   [Submit Feedback](#submit-feedback)
-   [Getting Started](#getting-started)
-   [Create and Publish a Release](#create-and-publish-a-release)

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/aubricus/klak/issues.

If you are reporting bugs, please follow the [.gihub/ISSUE_TEMPLATE.md](.github/ISSUE_TEMPLATE.md)

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

klak could always use more documentation, whether as part of the
official klak docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/aubricus/klak/issues.

If you are proposing a feature:

-   Explain in detail how it would work.
-   Keep the scope as narrow as possible, to make it easier to implement.
-   Remember that this is a volunteer-driven project, and that contributions
    are welcome :)

## Getting Started

Ready to contribute? Here's how to setup `klak` for local development.

### System Setup

-   [Install Brew (OSX only)](https://docs.brew.sh/Installation)
-   [Install Pyenv](https://github.com/pyenv/pyenv#installation)
-   [Install Poetry](https://poetry.eustace.io/docs/#installation)
-   [Install GitFlow](https://github.com/nvie/gitflow/wiki/Installation)

#### Install Required Pyenv, Python Versions

```bash
# Install the latest versions of Python 3.5, 3.6, 3.7
pyenv install 3.5.<latest-patch>
pyenv install 3.6.<latest-patch>
pyenv install 3.7.<latest-patch>
```

### Fork The Repository

Open the [Klak GitHub repository](https://github.com/aubricus/klak/) and [fork it](https://help.github.com/en/articles/fork-a-repo).

### Clone The Repository

Once you've forked the repository go a head and [clone it](https://help.github.com/en/articles/cloning-a-repository) locally.

### Install for Devleopment

```bash
# NOTE: Enter the repo root; if you haven't already.
cd klak

# NOTE: Set/verify local pyenv, Python versions (see .python-version)
pyenv local

# NOTE: Create a virtualenv; if you haven't already.
virtualenv .venv

# NOTE: Activate the virtualenv
source ./.venv/bin/activate

# NOTE: Finally, install app under development mode
poetry install --develop=DEVELOP
```

### Creating Branches

This repository is managed with [GitFlow] and GitHub pull requests. If you're not familiar with GitFlow please read [this blog post](https://nvie.com/posts/a-successful-git-branching-model/) first.

First:

```bash
# NOTE: Always update develop, master to the latest before branching
$ git fetch --all
$ git checkout develop
$ git merge --ff-only origin/develop

$ git fetch --all
$ git checkout master
$ git merge --ff-only origin/master
```

Then:

```bash
# NOTE: We use pull requests to review and merge code. As such using the GitFlow branch "finish" commands is not allowed.

# NOTE: Create a feature/ branch
git flow feature start <branch_name>

# NOTE: Create a hotfix/ branch
git flow hotfix start <branch_name>

# NOTE: Create a release/ branch
git flow release start <branch_name>
```

### Test Changes

```bash
# NOTE: Runs the test suite in all supported Python versions:
$ tox
```

### Submit a Pull Request

Once you've added your changes, run the test suite (successfully), [create a pull request](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork).

**Pull Request Guidelines**:

1. The pull request should include tests.
2. The pull request must pass all tests.
3. Check [Travis-CI](https://travis-ci.org/aubricus/klak/pull_requests) and make sure that the tests pass for all supported Python versions.
4. If necessary update the documentation.

## Create and Publish a Release

> A reminder for the maintainers.

1. Create a release branch using GitFlow.
2. Run tests and make any last minute fixes.
3. Update the [HISTORY.md](HISTORY.rst) changelog!
4. Bump the version in the `pyproject.toml`
5. Create a pull request
6. Once the pull request is merged into master:

```bash
# NOTE: Update local to latest
$ git fetch --all
$ git merge --ff-only origin/master

# NOTE: Create a new tag
$ git tag -a v<version_number> -m "Release of version v<version_number>"
$ git push --tags

# NOTE: Use Clickfile scripts to publish release to PyPI
$ klak dist build
$ klak dist publish
```

7. Finally, Check the [PyPI listing page](https://pypi.org/project/klak/) to verify publish was successful.