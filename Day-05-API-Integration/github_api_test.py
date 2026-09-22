import requests

response = requests.get("https://api.github.com", timeout=10)
response.raise_for_status()

print("Status:", response.status_code)
print("Content-Type:", response.headers["Content-Type"])

data = response.json()

print("Current User API:", data["current_user_url"])