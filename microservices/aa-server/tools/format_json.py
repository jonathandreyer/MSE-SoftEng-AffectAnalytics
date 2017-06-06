# -*- coding: utf-8 -*-

import json


def indent(obj):
    return json.dumps(obj, indent=4, sort_keys=True)


def to_obj(obj_str):
    return json.loads(obj_str)
