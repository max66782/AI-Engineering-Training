import requests


def get_github_repositories(username: str):
    """Get public GitHub repositories for a given username."""
    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url, timeout=10)

    if response.status_code == 404:
        return {"error": f"GitHub user '{username}' not found."}

    response.raise_for_status()

    return [
        {
            "name": repo["name"],
            "url": repo["html_url"],
            "description": repo["description"]
        }
        for repo in response.json()
    ]