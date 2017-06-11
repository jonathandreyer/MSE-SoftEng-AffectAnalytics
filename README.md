# MSE-SoftEng-AffectAnalytics

Master Software Engineering Project.

[![Build Status](https://travis-ci.org/Drakesinger/MSE-SoftEng-AffectAnalytics.svg?branch=master)](https://travis-ci.org/Drakesinger/MSE-SoftEng-AffectAnalytics)


## How do I build, validate and deploy the server?

Since version with microservices, we provide a CI/CD pipeline for the server, directly in this repo. The pipeline is built on top of Jenkins and Docker. The following process allows you to start the CI/CD server, to build the code, to run unittest and to have a running server on your machine:

1. Start the CI/CD server
  * `cd docker-topologies/cdpipeline/`
  * `export TOKEN="XXX"`
  * `export REPOS="user/repository"`
  * `export DELAY=60` (optional)
  * `export DEBUG=1`  (optional)
  * `docker-compose up`
  * wait until Jenkins has fully started
  * Open a web browser on [http://localhost:1080](http://localhost:1080)
  * Start the **build, validate and deploy affect analytics** job
  * Check the results in the Jenkins UI
2. At the end of the process, you should have a running docker topology
  * AffectAnalytics will run in background


## Legacy instructions (prior to version with CI/CD service)

### How do I run the server by docker-compose?

1. Build the docker image
  * `cd docker-images/aa-server/`
  * `./build-docker-image.sh`
2. Start the docker topology
  * `cd ../../docker-topologies/runtime/`
  * `export TOKEN="XXX"`
  * `export REPOS="user/repository"`
  * `export DELAY=60` (optional)
  * `export DEBUG=1`  (optional)
  * `docker-compose up`
3. At the end of the process, you should have a running docker container
  * AffectAnalytics will run in background


### How do I run the server by docker image?

1. Build the docker image
  * `cd docker-images/aa-server/`
  * `./build-docker-image.sh`
2. Start the docker image
  * `docker run -d -e TOKEN="XXX" -e REPOS="user/repository" -e DELAY=60 -e DEBUG=1 --name aa-server affectanalytics/server`
