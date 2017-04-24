# -*- coding: utf-8 -*-
import unittest
from tools.format_json import to_obj
from github.emotions import Emotions

UNITTEST_PARSE_1 = """[
    {
        "content": "THUMBS_DOWN",
        "id": "MDg6UmVhY3Rpb243ODk4MTQz"
    },
    {
        "content": "HEART",
        "id": "MDg6UmVhY3Rpb244MzIyMzAw"
    },
    {
        "content": "THUMBS_DOWN",
        "id": "MDg6UmVhY3Rpb244MzIyODQz"
    },
    {
        "content": "CONFUSED",
        "id": "MDg6UmVhY3Rpb243ODk1MDk2"
    },
    {
        "content": "HOORAY",
        "id": "MDg6UmVhY3Rpb243OTAwNTcz"
    },
    {
        "content": "HOORAY",
        "id": "MDg6UmVhY3Rpb244MzIyMjk1"
    },
    {
        "content": "THUMBS_DOWN",
        "id": "MDg6UmVhY3Rpb244MzIyMzc2"
    },
    {
        "content": "CONFUSED",
        "id": "MDg6UmVhY3Rpb244MzIyMzk2"
    }
]"""
UNITTEST_PARSE_1_RESULT = """[
    [
        3,
        5
    ],
    [
        [
            "HEART",
            "HOORAY",
            "HOORAY"
        ],
        [
            "THUMBS_DOWN",
            "THUMBS_DOWN",
            "CONFUSED",
            "THUMBS_DOWN",
            "CONFUSED"
        ]
    ]
]"""

UNITTEST_PARSE_2 = """[
    {
        "content": "LAUGH",
        "id": "MDg6UmVhY3Rpb245MjQyNjM1"
    },
    {
        "content": "THUMBS_DOWN",
        "id": "MDg6UmVhY3Rpb245MjQyNjM3"
    },
    {
        "content": "HOORAY",
        "id": "MDg6UmVhY3Rpb245MjQyNjQy"
    },
    {
        "content": "HEART",
        "id": "MDg6UmVhY3Rpb245MjQyNjQz"
    }
]"""
UNITTEST_PARSE_2_RESULT = """[
    [
        2,
        1
    ],
    [
        [
            "HOORAY",
            "HEART"
        ],
        [
            "THUMBS_DOWN"
        ]
    ]
]"""


def parse_emotions(unittest, usecase, ref):
    emotions_ref = to_obj(ref)
    emotions_parsed = Emotions.parse(to_obj(usecase))
    unittest.assertEqual(emotions_parsed[0], emotions_ref[0])
    unittest.assertEqual(emotions_parsed[1], emotions_ref[1])


class CheckEmotions(unittest.TestCase):
    def test_parse(self):
        parse_emotions(self, UNITTEST_PARSE_1, UNITTEST_PARSE_1_RESULT)
        parse_emotions(self, UNITTEST_PARSE_2, UNITTEST_PARSE_2_RESULT)

    def test_split(self):
        pass


if __name__ == "__main__":
    unittest.main()
