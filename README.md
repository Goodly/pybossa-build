# Unofficial Pybossa build for testing

This is a Docker build that creates a fat container running Pybossa for testing purposes.

The container is 'fat' because Supervisor is used to run additional supporting processes besides the core Flask web server.

A PostgreSQL database is required. The `docker-compose.yml` configures a Postgres container from Docker Hub, but you can provide a connection string to any network accessible PostgreSQL instance.

To build a specific branch or tag, use:
```bash
export SOURCE_BRANCH=v2.5.2
docker-compose build
```

If you don't specifiy `SOURCE_BRANCH`, it defaults to building current master.

Pybossa is installed directly from https://github.com/Scifabric/pybossa

The Pybossa container built accepts several environment variables for configuration, most notably PYBOSSA_DATABASE_URL. Check the `docker-compose.yml` for the others currently supported by this container.

## Notes specific to Goodly's use of the Docker Cloud auto-build process

(This note is not applicable if you are building the image on your own dev machine or infrastructure.)

Because our Docker Cloud auto-build process is triggered by this repo and not by updates to the Pybossa repo, a new build in Pybossa can be triggered by tagging master with a version tag. For example: `git tag v2.5.2` or `git tag v2.5.2-a` followed by `git push --tags` will result in a build.

Ideally our Docker Cloud config would checkout the same tag that triggers the build from the Pybossa repo. Unfortunately, Docker Cloud doesn't accept per build rule environment variables, nor does it accept regex substitions in environment variables the way it does in tags. So for now, when the version tag is detected, it is used for the docker registry tag. However, the actual commit built is specified and updated manually in the Docker Cloud build config page under environment variables.

# Licensing
Pybossa is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE. You can obtain the source for this container at the above URL.

The Dockerfile and scripts not provided originally by Scifabric are dual-licensed as GNU AFFERO GENERAL PUBLIC LICENSE or Apache License Version 2.0, January 2004, at your option.
