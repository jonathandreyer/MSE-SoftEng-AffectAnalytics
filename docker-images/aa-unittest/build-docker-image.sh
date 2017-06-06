#!/bin/bash

mkdir tmp
rm -fr tmp/*

cp -r ../../microservices/aa-unittest/* ./tmp/

docker build -t affectanalytics/unittest .

rm -rf ./tmp/
