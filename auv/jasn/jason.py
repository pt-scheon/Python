import requests

id = "3b04be6f2cf34d3f9b49fff00ce40641"
secret = "104d13676de349e69981d06eba56805d"

auth_response = requests.post(
    "https://accounts.spotify.com/api/token",
    data={"grant_type": "client_credentials"},
    auth=(id, secret)
)

access_token = auth_response.json().get("access_token")

url = "https://api.spotify.com/v1/playlists/37i9dQZF1E8PdLwnw0SjKg"
headers = {"Authorization": f"Bearer {access_token}"}

response = requests.get(url, headers=headers)
playlist_data = response.json()

print(playlist_data)