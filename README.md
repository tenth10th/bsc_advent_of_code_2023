# Boston Software Crafters
# Advent of Code 2023

A project for collaboratively working on challenges from the Advent Of Code 2023 edition

## Setup

**GitPod:** This project should set itself up automatically in GitPod.

**Local Pipenv:** In a local environment, you can set up automatically using `pipenv` by running
```
pipenv sync
```

**Local (Manual)** If you prefer not to use Pipenv,  create and activating a new virtual environment using your preferred approach, then install the current set of packages directly, using pip:
```
pip install -r requirement.txt
```

## Development

A `Makefile` has been provided to help use the provided development tools. Most notably:

* `make build` to validate your code and run tests

* `make run` to run the current main() method
