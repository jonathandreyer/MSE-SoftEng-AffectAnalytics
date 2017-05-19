#!/bin/bash

if [ -z ${AA_TOKEN+x} ]; then echo "Token is unset"; exit 1; else echo "Token is set to '$AA_TOKEN'"; fi
if [ -z ${AA_REPOS+x} ]; then echo "Repos is unset"; exit 1; else echo "Repos is set to '$AA_REPOS'"; fi

echo TOKEN=$AA_TOKEN > .env
echo REPOS=$AA_REPOS >> .env
if ! [ -z ${AA_DELAY+x} ]; then echo DELAY=$AA_DELAY >> .env; fi
