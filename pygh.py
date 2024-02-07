from github import Github

# Authentication is defined via github.Auth
from github import Auth
import os
from dotenv import load_dotenv

load_dotenv()

GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')

# using an access token
auth = Auth.Token("access_token")

# Public Web Github
g = Github(auth=auth)