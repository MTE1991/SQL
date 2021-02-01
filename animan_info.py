import sqlite3
import animan_lib as AniMan

print("---: AniMan infos ver 1.1 :--- \n")

# Connect to database:
conn = sqlite3.connect("AniMan.db") # Infos from myanimelist

while True:
	prompt_1 = int(input("1. Anime infos.\n2.Manga infos.\nYour choice ? : "))
	if prompt_1 == 1:
		print("""Choose one of the following:
			1. Search for info about an anime series/movie
			2. Search for top animes of a genre
			3. Get info directly from MyAnimeList website (uid needed)
				""")
		prompt_2 = int(input("Your choice ? : "))

		if prompt_2 == 1:
			query_1 = str(input("Enter anime name: "))
			AniMan.anime_info(query_1)
		elif prompt_2 == 2:
			query_2 = str(input("Enter a genre name: "))
			AniMan.top_animes(query_2)
		else:
			query_3 = int(input("Enter uid: "))
			AniMan.open_mal(query_3)

		prompt_3 = str(input("Do you want to search again? (Y/N) : "))

		if prompt_3 == "Y" or prompt_3 == "y":
			continue
		else:
			print("Thank you for using the program.")
			break
	else:
		print("""Choose one of the following:
			1. Search for info about a manga/manhwa/webtoon/novel
			2. Search for top manga/manhwa/webtoon/novel of a genre
			3. Get info directly from MyAnimeList website (uid needed)
				""")
		prompt_4 = int(input("Your choice ? : "))

		if prompt_4 == 1:
			query_4 = str(input("Enter name: "))
			AniMan.manga_info(query_4)
		elif prompt_4 == 2:
			query_5 = str(input("Enter a genre name: "))
			AniMan.top_mangas(query_5)
		else:
			query_6 = int(input("Enter uid: "))
			AniMan.open_mal(query_6)

		prompt_6 = str(input("Do you want to search again? (Y/N) : "))

		if prompt_6 == "Y" or prompt_6 == "y":
			continue
		else:
			print("Thank you for using the program.")
			break
		conn.close()