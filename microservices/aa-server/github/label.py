# -*- coding: utf-8 -*-
import requests
import json
import re

API_V3_URL = 'https://api.github.com'

LABEL_NAME = "Need check"
LABEL_COLOR = "ffa24c"

QUERY_CREATE = '''{
  "name": "%(label_name)s",
  "color": "%(label_color)s"
}'''


class Label(object):
    def __init__(self, token, owner, repo):
        self._token = token
        self._owner = owner
        self._repo = repo

    def add_warning(self, pr_no):
        if self._check_label():
            self._create_label()

        self._add_warning(pr_no)

    def remove_warning(self, pr_no):
        if self._check_present(pr_no):
            self._del(pr_no)

    # Check if label is present
    def _check_label(self):
        url_rel = '/repos/' + self._owner + '/' + self._repo + '/labels'

        labels = self._get(url_rel)

        for l in labels:
            if l['color'] == LABEL_COLOR and l['name'] == LABEL_NAME:
                return True

        return False

    # Create a label
    def _create_label(self):
        url_rel = '/repos/' + self._owner + '/' + self._repo + '/labels'
        query = QUERY_CREATE % dict(label_name=LABEL_NAME, label_color=LABEL_COLOR)
        self._post(url_rel, query)

    # Add warning to PR
    def _add_warning(self, pr_no):
        url_rel = '/repos/' + self._owner + '/' + self._repo + '/issues/' + str(pr_no) + '/labels'
        query = json.dumps([LABEL_NAME])
        self._post(url_rel, query)

    # Check if warning is present for PR
    def _check_present(self, pr_no):
        url_rel = '/repos/' + self._owner + '/' + self._repo + '/issues/' + str(pr_no) + '/labels'

        labels = self._get(url_rel)

        for l in labels:
            if l['color'] == LABEL_COLOR and l['name'] == LABEL_NAME:
                return True

        return False

    # Delete warning of PR
    def _del(self, pr_no):
        url_rel = '/repos/' + self._owner + '/' + self._repo + '/issues/' + str(pr_no) + '/labels/' + LABEL_NAME

        self._delete(url_rel)

    def _post(self, url_rel, data):
        header = 'bearer ' + str(self._token)
        headers = {'Authorization': header}

        url = API_V3_URL + url_rel

        query = data.replace('\n', '')
        q = re.sub(' +', ' ', query)

        r = requests.post(url, headers=headers, data=q)

        return json.loads(r.text)

    def _get(self, url_rel):
        header = 'bearer ' + str(self._token)
        headers = {'Authorization': header}

        url = API_V3_URL + url_rel

        r = requests.get(url, headers=headers)

        return json.loads(r.text)

    def _delete(self, url_rel):
        header = 'bearer ' + str(self._token)
        headers = {'Authorization': header}

        url = API_V3_URL + url_rel

        r = requests.delete(url, headers=headers)

        #return json.loads(r.text)
