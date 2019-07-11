[gitflow]: https://github.com/nvie/gitflow/ "GitFlow source code."

# Contributing

## Table of Contents

-   [Types of Contributions](#types-of-contributions)
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

Klak could always use more documentation, whether as part of the
official Klak docs, in docstrings, or even on the web in blog posts,
articles.

### Submit Feedback

The best way to send feedback is to [submit an issue](https://github.com/aubricus/klak/issues).

If you are proposing a feature:

-   Explain in detail how it would work.
-   Keep the scope as narrow as possible, to make it easier to implement.
-   Remember that this is a volunteer-driven project, and that contributions
    are welcome.

## Getting Started

Ready to contribute? Here's how to setup `klak` for local development.

### Style

Developers must configure their editor to:

-   Support [EditorConfg](https://editorconfig.org/#download).
-   Auto-format with [Python Black](https://github.com/python/black) (installed via Poetry).

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

Once you've added your changes and run the test suite (successfully) [create a pull request](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork).

**Pull Request Guidelines**:

1. The pull request should include tests.
2. The pull request must pass all tests.
3. Check [Travis-CI](https://travis-ci.org/aubricus/klak/pull_requests) and make sure that the tests pass for all supported Python versions.
4. If necessary update the documentation.

## Create a Release

Create a release branch using `git flow release start <version_number>`.

### Release Checklist

-   [ ] Run tests and make any last minute fixes.
-   [ ] Bump the version in the `pyproject.toml` and `klak.py`
-   [ ] Update the [HISTORY.md](HISTORY.md)
-   [ ] Push branch to GitHub to trigger tests in [Travis-CI](https://travis-ci.org/aubricus/klak).
-   [ ] Finalize release (see below).

#### Finalize Release

To keep the commit history as clean as possible, re-write the release branch history (**note**: use `r` for first commit and `s` for all others during interactive rebase):

```bash
$ git rebase -i <earliest_commit_hash>^
```

The new commit message should look like:

```bash
# Release: v<version_number>
#
# * Original commit message 1
#
# * Original commit message 2
#
# * Original commit message 3

```

### Publish Release

**Note**: Git Flow mangles repo history, so we'll follow the model manually.

```bash
# NOTE: Update local to latest.
$ git fetch --all

$ git checkout master
$ git merge --ff-only release/<version_number>
$ git push

$ git tag -a v<version_number> -m "Release of v<version_number>"
$ git push --tags

# NOTE: Use Clickfile scripts to publish release to PyPI.
$ klak dist build
$ klak dist publish

# NOTE: Catch develop up as well
$ git checkout develop
$ git merge --ff-only release/<version_number>
$ git push

# NOTE: Delete release branch
$ git branch -D release/<version_number>
```

### Post-Publish

Check the [PyPI listing page](https://pypi.org/project/klak/) to verify publish was successful.
