# Learning Docker ENTRYPOINT & CMD.

The Docker instructions, `CMD` and `ENTRYPONT`, are used in Dockerfiles and Docker Compose files to configure the commands used to run a container. This tutorial will explain the differences between them and how to use them in Dockerfiles.

# Entrypoint

**Entrypoint sets the command and parameters that will be executed first when a container is run.**

Any command line arguments passed to `docker run <image>` will be appended to the entrypoint command, and will override all elements specified using `CMD`. For example, `dokcer run <image> bash` will add the command argument `bash` to the end of the entrypoint.

There are several ways you can define this entrypoint in dockerfiles.

## The exec syntax

The `exec` form is where you specify commands and arguments as a JSON array. You need use the double quotes to represent it. Like `ENTRYPOINT ["executable", "param1", "param2"]`, using this syntax, Docker will not use a command shell, this command will no use the command shell in docker. If you need to use the docker command in shell, you can write shell command in the JSON array like `ENTRYPOINT ["sh", "-c", "echo $HOME" ]`.

## Using an entrypoint script

Except using the docker commands, a script also be allowed in the dockerfile. By convention, it often includes `entrypoint` in the name. In your script, you can setup the app as well as load any configuration and environment variables. Here is an example of how you can write dockerfile refer to script.
```bash
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["postgres"]
```
And use the script from the [Postgres Official Image](https://hub.docker.com/_/postgres/) as its `ENTRYPOINT`:

```bash
#! /bin/bash
set -e 

if [ "$1" = 'postgres' ]; then

    chown -R postgres "$PGDATA"
    if [ -z "$(ls -A "$PGDATA")" ]; then
        gosu postgres initdb
    fi
    exec gosu postgres "$@"
fi
exec "$@"
```
# Docker Compose entrypoint

The entrypoint in the Docker compose file can be like:
```bash
entrypoint: /code/entrypoint.sh
```
You can also define the entrypoint with lists in your docker-compose.yml.
```bash
entrypoint:
    - php
    - -d
    - zend_extension=/usr/local/lib/php/xdebug.so
    - -d
    - memory_limit=-1
    - vendor/bin/phpunit
```

# Overriding Entrypoint

Use the `--entrypoint` flag in the `docker run` command or `docker-compose run` can override the `entrypoint` instructions.

# CMD / command

This main purpose of a `CMD` (Dockerfile) / `command` (Docker Compose files) is to provide **defaults** when executing a container. These will be executed after the entrypoint.

For example, if you run the `docker run <image>` cmd, then the commands and parameters specified by `CMD` / `command` in your Dockerfile would be executed.

# Dockerfiles

Define the `CMD` defaults that include an executable. `CMD ["executable", "param1", "param2"]`.

Add default parameters to ENTRYPOINT `CMD ["param1", "param2"]`. In the dockerfile there only can be one `CMD`, If you list more that one, then only the last one will take effect.

# Docker Compose command
When using Docker Compose, you can define the samoe instruction in you docker-compose.yml, but it is written in lowercase as the full word `command`.
```bash
command: ["bunld", "exec", "thin", "-p", "3000"]
```
# Overriding CMD

You can override the commands specified by CMD when you run a container.
```bash
docker run python_app python run_server.py
```
