# -*- coding: utf-8 -*-

from tools.graphql import GraphQL

GITHUB_URL = 'https://api.github.com/graphql'
GITHUB_DEFAULT_QUERY = 100

QUERY_REPOSITORIES = '''{
  repositoryOwner(login: "%(user)s") {
    repositories(last: %(last_element)s) {
      edges {
        node {
          id
          name
          url
        }
      }
      totalCount
    }
  }
}'''

QUERY_PULLREQUEST = '''{
  repositoryOwner(login: "%(user)s") {
    repository(name: "%(repository)s") {
      pullRequests(states: [OPEN], last: %(last_element)s) {
        nodes {
          id
          number
          title
          author {
            login
          }
        }
        totalCount
      }
    }
  }
}'''

QUERY_EMOTIONSONPULLREQUEST = '''{
  repositoryOwner(login: "%(user)s") {
    repository(name: "%(repository)s") {
      pullRequest(number: %(pr_number)s)
      {
        reactions(last:%(last_element)s) {
          edges {
            node {
              id
              content
            }
          }
          totalCount
        }
        comments(last:%(last_element)s) {
          edges {
            node {
              reactions(last:100) {
                nodes {
                  id
                  content

                }
                totalCount
              }
            }
          }
        }
      }
    }
  }
}'''


class Repository(object):
    def __init__(self, owner, name, url, id, github=None):
        self.owner = owner
        self.name = name
        self.url = url
        self.id = id
        self.gh = github

    def get_pull_requests(self):
        # TODO get_pull_requests
        print "get_pull_requests not implemented"

    def get_number_of_pull_requests(self):
        # TODO get_number_of_pull_requests
        print "get_number_of_pull_requests not implemented"


class Pull_Request(object):
    """
    pr_id = pullrequest['id']
    pr_title = pullrequest['title']
    pr_number = int(pullrequest['number'])
    """

    def __index__(self,owner, title, id, number):
        self.owner = owner
        self.title = title
        self.id = id
        self.number = number


class GitHub(object):
    def __init__(self, token):
        # Instead of providing the token directly, we provide a path to the token file.
        self._token = ""
        token_file_path = token
        with open(token) as token_file:
            self._token = token_file.read()
            print ("Token has been read.")

    # Get repository ID & name
    def get_repositories(self, user_name, n=GITHUB_DEFAULT_QUERY):
        query = QUERY_REPOSITORIES % dict(user=user_name, last_element=str(n))

        gql = GraphQL(self._token, GITHUB_URL)
        result = gql.execute(query)
        # Get the repositories
        repositories = result['data']['repositoryOwner']['repositories']['edges']
        repos = []

        for repo in repositories:
            repo_name = repo['node']['name']
            repo_id = repo['node']['id']
            repo_url = repo['node']['url']
            repos.append(Repository(owner=user_name,name=repo_name, url=repo_url, id=repo_id))
            #repos.append([repo_name, repo_id, repo_url])

        return repos

    # Get pull request of repository, return id, title and number
    def get_pullrequest(self, user_name, repository_name, n=GITHUB_DEFAULT_QUERY):
        query = QUERY_PULLREQUEST % dict(user=user_name, repository=repository_name, last_element=str(n))

        gql = GraphQL(self._token, GITHUB_URL)
        result = gql.execute(query)

        pullrequests = result['data']['repositoryOwner']['repository']['pullRequests']['nodes']
        count = result['data']['repositoryOwner']['repository']['pullRequests']['totalCount']

        pr = []

        for pullrequest in pullrequests:
            pr_id = pullrequest['id']
            pr_title = pullrequest['title']
            pr_number = int(pullrequest['number'])

            pr.append([pr_id, pr_title, pr_number])

        return pr, count

    def get_emotions(self, user_name, repository_name, pullrequest_number, n=100, splited=False):
        query = QUERY_EMOTIONSONPULLREQUEST % dict(user=user_name, repository=repository_name,
                                                   pr_number=pullrequest_number, last_element=str(n))

        gql = GraphQL(self._token, GITHUB_URL)
        result = gql.execute(query)

        # parse emotions in pullrequest
        pullrequest = result['data']['repositoryOwner']['repository']['pullRequest']['reactions']['edges']
        pullrequest_emotions = []

        for pullrequest_emotion in pullrequest:
            pr_emotion = pullrequest_emotion['node']
            pullrequest_emotions.append(pr_emotion)

        # parse emotions in comments of pullrequest
        comments = result['data']['repositoryOwner']['repository']['pullRequest']['comments']['edges']

        comments_emotions = []

        for node_comment in comments:
            nodes = node_comment['node']['reactions']['nodes']

            if len(nodes) > 0:
                for node in nodes:
                    comments_emotions.append(node)

        # return splited list between emotion of pullrequest and emotions of comments (pullrequest)
        if splited:
            return pullrequest_emotions, comments_emotions
        else:
            for emotion in comments_emotions:
                pullrequest_emotions.append(emotion)

            return pullrequest_emotions
