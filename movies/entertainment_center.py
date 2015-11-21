import media
import fresh_tomatoes

toy_story = media.Movie("Toy Stroy",
						"A boy and his toys that come to life.",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"http://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
					"A Marine on an alien planet.",
					"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					"http://www.youtube.com/watch?v=uZNHIU3uHT4")

#print(avatar.storyline)
#avatar.show_trailer()
princess_bride = media.Movie("Princess Bride",
									"A farmhand's journey from priate to happpy",
									"https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
									"https://www.youtube.com/watch?v=VYgcrny2hRs")
#princess_bride.show_trailer()
mission_impossible = media.Movie ("Mission Impossible - Rogue Nation",
										"A series of increasingly impossible missions",
										"https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg",
										"https://www.youtube.com/watch?v=pXwaKB7YOjw")
fantastic_four = media.Movie("Fantastic Four",
								"Friends create a teleporter",
								"https://upload.wikimedia.org/wikipedia/en/f/f4/Fantastic_Four_2015_poster.jpg",
								"https://www.youtube.com/watch?v=POBI7OhGB18")

trainwreck = media.Movie("Trainwreck",
						"Another crappy romantic comedy",
						"https://upload.wikimedia.org/wikipedia/en/c/c5/Trainwreck_poster.jpg",
						"https://www.youtube.com/watch?v=lrwsY2JxWM8")
movies = [toy_story, avatar, princess_bride, mission_impossible, fantastic_four, trainwreck]

fresh_tomatoes.open_movies_page(movies)
