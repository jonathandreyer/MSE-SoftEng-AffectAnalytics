# MSE-SoftEng-AffectAnalytics

Master Software Engineering Project.

[![Build Status](https://travis-ci.org/jonathandreyer/MSE-SoftEng-AffectAnalytics.svg?branch=dev-test-fail-unittest)](https://travis-ci.org/jonathandreyer/MSE-SoftEng-AffectAnalytics)

## How do I build, validate and deploy the server?

Since version with microservices, we provide a CI/CD pipeline for the server, directly in this repo. The pipeline is built on top of Jenkins and Docker. The following process allows you to start the CI/CD server, to build the code, to run unittest and to have a running server on your machine:

1. Start the CI/CD server
  * `cd docker-topologies/cdpipeline/`
  * `docker-compose up`
  * wait until jenkins has fully started
  * Open a web browser on [http://localhost:1080](http://localhost:1080)
  * Start the **build, validate and deploy affect analytics** job
  * Check the results in the jenkins UI
2. At the end of the process, you should have a running docker topology
  * Open a web browser on [http://localhost:5000](http://localhost:5000)

## Legacy instructions (prior to version with CI/CD service)

### How do I run the server?

1. Build the docker image
  * `cd docker-images/aa-server/`
  * `./build-docker-image.sh`
2. Start the docker topology
  * `cd ../../docker-topologies/runtime/`
  * `docker-compose up`
3. Check that the server is running
  * Open a web browser on [http://localhost:5000](http://localhost:5000)
