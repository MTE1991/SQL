import sqlite3

print("Anime infos ver 1.01 (press q to quit) \n")

while True:
	try:
		query = str(input("Enter Anime name (must be accurate) : "))
		conn = sqlite3.connect("AnimeInfo.db") # MyAnimeList dataset
		cursor = conn.execute("""
			SELECT title, episodes, genre, synopsis
			FROM Animes_main
			WHERE title LIKE '{query}%'""".format(query=query))

		for row in cursor:
			print("Anime name: ", row[0])
			print("Episodes: ", row[1])
			print("Genre: ", row[2])
			print("Synopsis: \n", row[3])

		prompt = str(input("Do you want to search again? (Y/N) : "))

		if prompt == "Y" or prompt == "y":
			continue
		else:
			conn.close()
			break
	except:
		raise Exception("Sorry, connection to database failed.")
