from github import Github

# Authentication is defined via github.Auth
from github import Auth
import os
from dotenv import load_dotenv

load_dotenv()

GH_ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')

# using an access token
auth = Auth.Token(GH_ACCESS_TOKEN)

# Public Web Github
g = Github(auth=auth)

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))