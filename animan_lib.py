import sqlite3
import webbrowser

# Connect to database:
conn = sqlite3.connect("AniMan.db") # Infos from myanimelist

# Query functions:
def anime_info(anime):
	"""Show info about a specific anime series/movie"""	
	cursor = conn.execute("""
		SELECT uid, title, episodes, genre, score, synopsis FROM Animes_main
		WHERE title LIKE '%{anime}%' """.format(anime=anime))

	for row in cursor:
		print("-" * 50)
		print("uid: ", row[0])
		print("Anime name: ", row[1])
		print("Episodes: ", row[2])
		print("Genre: ", row[3])
		print("Score: ", row[4])
		print("Synopsis: \n", row[5])
		print("-" * 50)

def top_animes(genre):
	"""Show the top 10 anime series/movies of a specific genre"""
	cursor = conn.execute("""
		SELECT title, genre, episodes, score FROM Animes_main
		WHERE genre LIKE '%{genre}%'
		ORDER BY score DESC LIMIT 10 """.format(genre=genre))

	for row in cursor:
		print("-" * 50)
		print("Score: ", row[3])
		print("Anime name: ", row[0])
		print("Genre: ", row[1])
		print("Episodes: ", row[2])
		print("-" * 50)

def manga_info(manga):
	"""Show info about a specific manga/manhwa/webtoon"""	
	cursor = conn.execute("""
		SELECT name, type, quantity, genres, status, date, rank, popularity FROM Manga_main
		WHERE name LIKE '%{manga}%' """.format(manga=manga))

	for row in cursor:
		print("-" * 50)
		print("Name: ", row[0])
		print("Type: ", row[1])
		print("Quantity: ", row[2])
		print("Genre: ", row[3])
		print("Status: ", row[4])
		print("Date: ", row[5])
		print("Rank: ", row[6])
		print("Popularity: ", row[7])
		print("-" * 50)


def top_mangas(genres):
	"""Show the top 10 anime series/movies of a specific genre"""
	cursor = conn.execute("""
		SELECT popularity, name, genres, quantity FROM Manga_main
		WHERE genres LIKE '%{genres}%'
		ORDER BY popularity ASC LIMIT 10 """.format(genres=genres))

	for row in cursor:
		print("-" * 50)
		print("Popularity: ", row[0])
		print("Name: ", row[1])
		print("Genre: ", row[2])
		print("Quantity: ", row[3])
		print("-" * 50)

def open_mal(uid):
	"""Open MAL url for the requested uid"""
	webbrowser.open(f"https://myanimelist.net/anime/{uid}")