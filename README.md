# NLP Hints

This is a Docker build that creates a standalone Pybossa container for testing purposes.

Pybossa is installed from the master branch of https://github.com/Scifabric/pybossa
Supervisor is installed to run Pybossa and supporting processes.

Because the auto-build process is triggered by this repo and not by updates to the Pybossa repo, a new build in Pybossa can be built by tagging master with a version tag. `git tag v2.3.8` or `git tag v2.3.8-a` followed by `git push --tags` will result in a checkout of that tag from the Pybossa repo and then a push to Docker Hub using that tag as a docker image tag. Note that this may result in commits in this repo having multiple different version tags, but that's just an artifact of using tags here to trigger a build of the external Pybossa repo.

One external container is required, a PostgreSQL database.

Pybossa is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE. You can obtain the source for this container at the above URL.

The Dockerfile is dual-licensed as GNU AFFERO GENERAL PUBLIC LICENSE or Apache License Version 2.0, January 2004, at your option.
