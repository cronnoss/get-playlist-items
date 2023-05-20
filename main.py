import requests
import os
from dotenv import load_dotenv

load_dotenv()
playlist_id = os.getenv('PLAYLIST_ID')

url = "https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks"
headers = {
    'Authorization': f"Bearer {os.getenv('SPOTIFY_BEARER_TOKEN')}",
}

response = requests.get(url, headers=headers)
data = response.json()

# Print the name and artist of each track in the playlist
for item in data['items']:
    track = item['track']
    print(f"{track['name']} - {track['artists'][0]['name']}")

# Save the output to a file
with open('tracks.txt', 'w') as f:
    for item in data['items']:
        track = item['track']
        f.write(f"{track['name']} - {track['artists'][0]['name']}\n")
