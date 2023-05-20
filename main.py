import requests

url = "https://api.spotify.com/v1/playlists/5PzmUOcfEsyHMADFUxm555/tracks"
headers = {
    'Authorization': 'Bearer BQD-AbJwf8a7qRRGf9NqmH9-hmhO61wOLbgyDrTeCdz-kaO3SCKE8eXuyObl9fyzu7Nmz0JkmRBTd9-GB88y0WzIKK0MCjFcpTos8dJpLewZySHFh555',
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

