# -*- coding: utf-8 -*-

GITHUB_DICT = {'THUMBS_UP': 1, 'THUMBS_DOWN': -1, 'LAUGH': 0, 'HOORAY': 1, 'CONFUSED': -1, 'HEART': 1}


class Emotions(object):
    @staticmethod
    def parse(emotions):

        balance = [0, 0]
        emotions_balance = [[], []]

        for emotion in emotions:
            val = GITHUB_DICT[emotion['content']]

            if val > 0:
                balance[0] += abs(val)
                emotions_balance[0].append(emotion['content'])
            elif val < 0:
                balance[1] += abs(val)
                emotions_balance[1].append(emotion['content'])

        return balance, emotions_balance

    @staticmethod
    def parse_split(pr_emotions, comment_emotions):

        return Emotions.parse(pr_emotions), Emotions.parse(comment_emotions)
