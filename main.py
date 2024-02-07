import argparse
import sys
from github import api, repo_settings, branch_protection

def main(organization, action):
    # Authenticate GitHub API
    api.authenticate()

    # List all repositories for the organization
    repositories = api.list_repositories(organization)
    
    for repo in repositories:
        print(f"Processing {repo['name']}...")
        
        # Based on the action, import or export data
        if action == "export":
            settings = repo_settings.export_settings(repo['name'])
            protections = branch_protection.export_protections(repo['name'])
            print(f"Exported settings and protections for {repo['name']}")
        
        elif action == "import":
            # Import actions would be defined here
            print(f"Import functionality not implemented yet for {repo['name']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Import or export data from GitHub repositories.')
    parser.add_argument('organization', type=str, help='The GitHub organization name.')
    parser.add_argument('--action', choices=['import', 'export'], required=True, help='The action to perform: import or export.')
    
    args = parser.parse_args()

    try:
        main(args.organization, args.action)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
