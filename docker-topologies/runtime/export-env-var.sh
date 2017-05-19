#!/bin/bash

echo TOKEN=$AA_TOKEN > .env
echo REPOS=$AA_REPOS >> .env
echo DELAY=$AA_DELAY >> .env

more .env
