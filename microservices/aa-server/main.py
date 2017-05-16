# -*- coding: utf-8 -*-
import sys
import argparse

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

        # Get the pull requests.
        pull_requests, nb_pull_requests = gh.get_pullrequest(repo_owner, repo_name)

        #if pull_requests:
        #    print("We have PRs:\n", pull_requests)
        #else:
        #    print("There are no Pull Requests %s!" % repo_name)
        #print("Owner:", repo_owner, " repo:", repo_name)

        # Check status of every PR in rep
        for pr in pull_requests:
            pr_no = pr[2]
            emotions = gh.get_emotions(repo_owner, repo_name, pr_no)
            bal, bal_emo = Emotions.parse(emotions)

            #print(bal, bal_emo)

            # If bad status, add label
            gh_lbl = Label(token, repo_owner, repo_name)

            if BalanceEmotions.is_bad_emotions(bal):
                #print('It is necessary to add warning label!')

                # Add label
                gh_lbl.add_warning(pr_no)
            else:
                # Remove label
                gh_lbl.remove_warning(pr_no)


class PollingGithub(TaskThread):
    def task(self, **kwargs):
        print('wake up, execute polling!')
        #print(kwargs['token'], kwargs['repos'])
        polling_github(kwargs['token'], kwargs['repos'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Argument not valid!')
    parser.add_argument('-t', '--token', type=str, help='github token of repos')
    parser.add_argument('-r', '--repos', type=str, nargs='*', help='user/repos')
    parser.add_argument('-d', '--delay', type=int, nargs='*', help='time between polling', default=10)
    args = parser.parse_args()

    if args.token is None:
        raise Exception('Github token is not set!')

    if args.repos is None:
        raise Exception('Repository information is not set!')

    #print(args.token)
    #print(args.repos)
    #print(args.delay)

    kwargs = {"token": args.token, "repos": args.repos}

    periodic_polling = PollingGithub(**kwargs)
    periodic_polling.set_interval(args.delay)
    periodic_polling.run()

    sys.exit()
