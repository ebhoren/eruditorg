[![Build Status](https://secure.travis-ci.org/erudit/zenon.svg?branch=master)](https://secure.travis-ci.org/erudit/zenon?branch=master)
[![Coverage](https://codecov.io/github/erudit/zenon/coverage.svg?branch=master)](https://codecov.io/github/erudit/zenon?branch=master)
# Installation

## System dependencies

On Ubuntu 14.04 :

  python 3.4
  libx11-dev
=======
* libxml-devel
* libxslt-devel

## Local setup

On Ubuntu 14.04

1. Install the latest docker

  To install the latest docker-engine, follow the steps documented on the docker website:

  https://docs.docker.com/installation/ubuntulinux/

2. Add your user to the docker group

  ```
  $ sudo usermod -a -G docker $USER
  ```

3. Install docker-compose

  ```
  # curl -L https://github.com/docker/compose/releases/download/1.5.0rc2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
  # chmod +x /usr/local/bin/docker-compose
  ```

  Ref: https://docs.docker.com/compose/install/

4. Clone the git repository

  <pre>
  $ git clone https://github.com/erudit/zenon
  </pre>

5. Create a 'settings_env.py' file

  The settings_env.py file overrides the general settings with environment specific settings.The settings.py contains all the required settings to setup a local environment.

  <pre>
  $ touch erudit/erudit/settings_env.py
  </pre>

6. Build the images

  At this point, you have everything necessary to build

  ```
  $ docker-compose up
  ```

7. Apply the migrations

  ```
  $ docker-compose run python erudit/manage.py migrate auth
  $ docker-compose run python erudit/manage.py migrate
  ```

8. Create a superuser

  ```
  $ docker-compose run python erudit/manage.py createsuperuser
  ```

# Documentation

The project's documentation is built with [Sphinx](http://www.sphinx-doc.org/)

Building the documentation is optional. For this reason, `sphinx` is not listed in requirements.txt
If you wish to build the documentation, you must first install sphinx in your virtualenv.

  ```
  $ pip install sphinx
  ```

You will then be able to build the docoumentation using the `Makefile` in the `docs` directory:

  ```
  $ make html
  ```

# Deploying updates

```
$ ansible-playbook playbook.yml -i hosts -t update -l local --ask-vault-pass
```

Where `local` is the the target environment.

# Running the tests

You can run the tests with:

```
$ tox
```

# Developing the UI

All styling is done in the `sass` directory, which is based on the [7-1 architecture pattern](http://sass-guidelin.es/#architecture). Each subdirectory contains a `README.md` with further information regarding its proper use.
