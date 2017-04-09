# AffectAnalytics as a micro service

## Creating and packaging the micro service
* We want to run AffectAnalytics as a micro service, integrated with other services of the Probe Dock platform (main Probe Docker server, data stores such as Redis, Postgres, etc.).

* In other words, we want to package AffectAnalytics in a Docker image and then run a Docker container based on this image.

* To create the Docker image, we need the Dockerfile in this directory. It is very simple. It needs to extends a base image which provides a python runtime environment.

* We have created the `build-docker-image.sh` script to automate this process. In the script, we first do a copy source file, and finally run `docker build -t affectanalytics/server .`. This will update the affectanalytics/server:latest image on the current machine.

* Warning: to run the script, you must be in a "Docker environment" (in other words, on Mac OS and Windows, you must have all environment variables defined so that you can use Docker machine).
