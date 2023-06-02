from bs4 import BeautifulSoup
import spotipy, requests
from spotipy.oauth2 import SpotifyOAuth

url = "http://example.com/?code=AQAAvp_2BhzMfpPCNEEdGsawSgJmTxcxz9nrme4hHbasz9B7nUCeGTzzlX4Z3LbDtH4r_mjPLSldgPHZGf3klVj1UwPrf3vExl00biiBRGmP01vHhMEP-3xq9dQREdm2PZCvOQDililRWvQ3QKVl1GtMy6pRed6EbKQnCHrG9smRgz7LoV5xlnHOR4g9jRs"

client_secret = "94130a6d161a4158b5fc47a69c56cf03"
client_id = "39322be59fd3412c8081e8b16b73c2bc"

id = "31cgaf4shvseox7qjs5cmloukwsa"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

song_uris = []
year = date.split("-")[0]

soup = BeautifulSoup(response.text, "html.parser")
songs = soup.find_all("h3", "a-no-trucate")
song_names = [song.getText(strip=True) for song in songs]
print(song_names)

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)