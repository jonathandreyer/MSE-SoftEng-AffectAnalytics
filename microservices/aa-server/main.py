# -*- coding: utf-8 -*-
import sys
import argparse
import logging

from github.github import GitHub
from github.emotions import Emotions, BalanceEmotions
from github.label import Label
from tools.periodic import TaskThread


def polling_github(token, repos):
    gh = GitHub(token)

    for repo in repos:
        # split owner & repo. name
        r = repo.split('/')
        repo_owner = r[0]
        repo_name = r[1]

        logging.info('Owner:' + repo_owner + ' repo:' + repo_name)

        # Get the pull requests.
        pull_requests, nb_pull_requests = gh.get_pullrequest(repo_owner, repo_name)

        if pull_requests:
            logging.info('We have PRs:' + str(pull_requests))
        else:
            logging.info("There are no Pull Requests %s!" % repo_name)

        # Check status of every PR in rep
        for pr in pull_requests:
            pr_no = pr[2]
            emotions = gh.get_emotions(repo_owner, repo_name, pr_no)
            bal, bal_emo = Emotions.parse(emotions)

            logging.info('Balance emotions: ' + str(bal) + ', Emotions: ' + str(bal_emo))

            # If bad status, add label
            gh_lbl = Label(token, repo_owner, repo_name)

            if BalanceEmotions.is_bad_emotions(bal):
                logging.info('Add a warning for this PR')

                # Add label
                gh_lbl.add_warning(pr_no)
            else:
                logging.info('Remove warning if it is present')

                # Remove label
                gh_lbl.remove_warning(pr_no)


def print_and_log(msg=''):
    print(msg)
    logging.info(msg)


class PollingGithub(TaskThread):
    def task(self, **kwargs):
        logging.debug('Task wake up!')
        logging.info('Start polling with ' + str(kwargs['token']) + ', repos: ' + str(kwargs['repos']))
        polling_github(kwargs['token'], kwargs['repos'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Argument not valid!')
    parser.add_argument('-t', '--token', type=str, help='github token of repos')
    parser.add_argument('-r', '--repos', type=str, nargs='*', help='user/repos')
    parser.add_argument('-d', '--delay', type=int, help='time between polling', default=10)
    parser.add_argument('-l', '--log', help='Enable debug log', action='store_true')
    args = parser.parse_args()

    if args.token is None:
        raise Exception('Github token is not set!')

    if args.repos is None:
        raise Exception('Repository information is not set!')

    if args.log:
        logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(asctime)s %(message)s')

    print_and_log()
    print_and_log('-------------------------------')
    print_and_log('-  Start polling service      -')
    print_and_log('-------------------------------')
    print_and_log()
    print_and_log('Parameters:')
    print_and_log(' # TOKEN: ' + str(args.token))
    print_and_log(' # REPOS: ' + str(args.repos))
    print_and_log(' # DELAY: ' + str(args.delay))
    if args.log:
        print_and_log(' # LOG:   enable')
    print_and_log()

    kwargs = {"token": args.token, "repos": args.repos}

    periodic_polling = PollingGithub(**kwargs)
    periodic_polling.set_interval(args.delay)
    periodic_polling.run()

    sys.exit()
