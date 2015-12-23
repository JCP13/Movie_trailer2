import media
import fresh_tomatoes

# this will provide a collection of movie objects
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_story.storyline)
avatar = media.Movie("Avatar 2",
                     "A marine on an alian planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=PQo8Csj0k_c")
# print(avatar.storyline)

hulk = media.Movie("Hulk",
                   "a man who became a monster",
                   "http://www.firstshowing.net/img/incredible-hulk-poster-big.jpg",
                   "https://www.youtube.com/watch?v=xbqNb2PFKKA")

school_of_rock = media.Movie("School of Rock",
                             "story line",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "story line",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "story line",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger games",
                           "story line",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

# add a collection of movies objects to an array
movies = [toy_story, hulk, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
# create the HTML page that will display the collection of movies
fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.VALID_RATINGS)

# print(media.Movie.__doc__)
