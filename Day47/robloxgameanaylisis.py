from bs4 import BeautifulSoup
import requests

game = input("Enter a roblox game ID to check data: ")

response = requests.get(f"https://roblox.com/games/{game}")

soup = BeautifulSoup(response.text, "html.parser")
favorites = soup.find(name="span", class_="game-favorite-count")
players = soup.find(name="p", class_="text-lead")
visits = soup.find(name="p", id="game-visit-count").get("title")
print(f"Favorites: {favorites.text}\nPlayers: {players.text}\nVisits: {visits}")