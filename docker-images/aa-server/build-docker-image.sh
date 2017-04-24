#!/bin/bash

mkdir tmp

cp -r ../../microservices/aa-server/* ./tmp/

docker build -t affectanalytics/server .

rm -rf ./tmp/
