import sqlite3
import webbrowser

print("---: Anime infos ver 1.01 :--- \n")

# Connect to database:
try:
	conn = sqlite3.connect("AnimeInfo.db") # Infos from myanimelist
except:
		raise Exception("Sorry, connection to database failed.")

# Query functions:
def anime_info(anime):
	"""Show info about a specific anime series/movie"""		
	cursor = conn.execute("""
		SELECT uid, title, episodes, genre, synopsis FROM Animes_main
		WHERE title LIKE '%{anime}%' """.format(anime=anime))

	for row in cursor:
		print("-" * 50)
		print("uid: ", row[0])
		print("Anime name: ", row[1])
		print("Episodes: ", row[2])
		print("Genre: ", row[3])
		print("Synopsis: \n", row[4])
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

def open_mal(uid):
	"""Open MAL url for the requested uid"""
	webbrowser.open(f"https://myanimelist.net/anime/{uid}")

while True:
	print("""Choose one of the following:
		1. Search for info about an anime series/movie
		2. Search for top animes of a genre
		3. Get info directly from MyAnimeList website (uid needed)
			""")
	prompt_1 = int(input("Your choice ? : "))

	if prompt_1 == 1:
		query_1 = str(input("Enter anime name: "))
		anime_info(query_1)
	elif prompt_1 == 2:
		query_2 = str(input("Enter a genre name: "))
		top_animes(query_2)
	else:
		query_3 = int(input("Enter uid: "))
		open_mal(query_3)

	prompt_2 = str(input("Do you want to search again? (Y/N) : "))

	if prompt_2 == "Y" or prompt_2 == "y":
		continue
	else:
		print("Thank you for using the program.")
		conn.close()
		break