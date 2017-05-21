#!/bin/sh
docker build --no-cache --build-arg SOURCE_BRANCH=${SOURCE_BRANCH:-master} -f docker/pybossa/Dockerfile docker/
