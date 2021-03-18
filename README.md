# Democritus Dates

[![PyPI](https://img.shields.io/pypi/v/d8s-dates.svg)](https://pypi.python.org/pypi/d8s-dates)
[![CI](https://github.com/democritus-project/d8s-dates/workflows/CI/badge.svg)](https://github.com/democritus-project/d8s-dates/actions)
[![codecov](https://codecov.io/gh/democritus-project/d8s-dates/branch/main/graph/badge.svg?token=V0WOIXRGMM)](https://codecov.io/gh/democritus-project/d8s-dates)
[![The Democritus Project uses a form of calendar versioning in the form: `MAJOR.YYYY.0M.0D`](https://img.shields.io/badge/calver-MAJOR.YYYY.0M.0D-22bfda)](https://calver.org/)
[![The Democritus Project uses black to format code](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Democritus functions<sup>[1]</sup> for working with and using dates and times.

[1] Democritus functions are <i>simple, effective, modular, well-tested, and well-documented</i> Python functions.

## Usage

Coming soon...

## Development

If you want to contribute to this project, make sure you have [docker][docker] and [docker-compose][docker-compose] installed (if you don't see: [installing docker][docker-install]).

Once you do this, you should follow the Democritus Project's [contribution guide][contribution-guide].

Then you can both *test* and *lint* this project using the docker-compose commands below!

### Testing

To test this project, run the following command from the root directory of the repository:

```shell
docker-compose run --rm test
```

To see what this command does, take a look at the `test` service in [`docker-compose.yml`][docker-compose-file].

### Linting

To lint this project, run the following command from the root directory of the repository:

```shell
docker-compose run --rm lint
```

To see what this command does, take a look at the `lint` service in [`docker-compose.yml`][docker-compose-file].

### Dev

To drop into a "dev" environment which is an [IPython][ipython] shell with the project and all its requirements loaded, run the following command from the root directory of the repository:

```shell
docker-compose run --rm dev
```

To see what this command does, take a look at the `dev` service in [`docker-compose.yml`][docker-compose-file].

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and Floyd Hightower's [Python project template](https://github.com/fhightower-templates/python-project-template).

[docker-compose]: https://docs.docker.com/compose/
[docker-install]: https://docs.docker.com/get-docker/
[docker]: https://www.docker.com/get-started
[linting-intro]: https://dbader.org/blog/python-code-linting
[ipython]: https://ipython.org/
[contribution-guide]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md
[docker-compose-file]: ./docker-compose.yml
