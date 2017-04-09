#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import re


class GraphQL(object):
    def __init__(self, token, url):
        self._token = token
        self._url = url

    def execute(self, query):
        header = 'bearer ' + str(self._token)
        headers = {'Authorization': header}

        query = query.replace('\n', '')

        q = json.dumps({'query': query})

        q = re.sub(' +', ' ', q)

        r = requests.post(self._url, headers=headers, data=q)

        return json.loads(r.text)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", type=str, help="Token for GitHub access")

    args = parser.parse_args()

    gql = GraphQL(args.token)

    query = '''
    {
      viewer {
        login
      }
    }
    '''

    obj = gql.execute(query)

    print(obj)
