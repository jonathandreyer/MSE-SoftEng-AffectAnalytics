#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import github.github as gh
from github.emotions import Emotions

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", type=str, help="Path to token file for GitHub access")
    parser.add_argument("-u","--username", type=str, help="User name")
    parser.add_argument("-r","--repo", type=str, help="Repository name")
    parser.add_argument("-n", type=int, help="Quantity of pull request", default=10)
    args = parser.parse_args()

    gh = gh.GitHub(args.token)

    # print(gh.get_repositories('drakesinger'))
    #print(gh.get_repositories('jonathandreyer'))
    print(gh.get_pullrequest('jonathandreyer', 'test'))
    print (Emotions.parse(gh.get_emotions('jonathandreyer', 'test', 1)))

    exit(0)
