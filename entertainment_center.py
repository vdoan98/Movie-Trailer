import media #Import file containing Class Movie 
import fresh_tomatoes #Import file containing HTML and CSS
                      #for webpage

winter_soldier = media.Movie("Captain America: The Winter Soldier",
                             "Captain America encounters the"
                             "ghost of his past on a mission",
                             "https://upload.wikimedia.org/wikipedia"
                             "/en/thumb/e/e8/Captain_America_"
                             "The_Winter_Soldier.jpg"
                             "/220px-Captain_America_The_Winter_Soldier.jpg",
                             "https://www.youtube.com/watch?v=tbayiPxkUMM")

civil_war = media.Movie("Captain America: Civil War ",
                        "Cap vs Iron Man, the Avengers no more",
                        "https://upload.wikimedia.org/wikipedia"
                        "/en/thumb/5/53/Captain_America_"
                        "Civil_War_poster.jpg/220px-"
                        "Captain_America_Civil_War_poster.jpg",
                        "https://www.youtube.com/watch?v=uVdV-lxRPFo")

beauty_and_the_beast = media.Movie("Beauty and the Beast",
                                   "A fairy tale of a girl who fell "
                                   "in love with a beast",
                                   "https://upload.wikimedia.org/wikipedia"
                                   "/en/d/d6/Beauty_and_the_Beast_"
                                   "2017_poster.jpg",
                                   "https://www.youtube.com/"
                                   "watch?v=3PsUJFEBC74")

up = media.Movie("Up", "An old man journey to paradise",
                 "https://upload.wikimedia.org/wikipedia"
                 "/en/thumb/0/05/Up_%282009_film%29.jpg/"
                 "220px-Up_%282009_film%29.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")

rogue_one = media.Movie("Rogue One",
                        "Back before Luke Skywalker entered the story",
                        "https://upload.wikimedia.org/wikipedia"
                        "/en/thumb/d/d4/"
                        "Rogue_One%2C_A_Star_Wars_Story_poster.png"
                        "/220px-Rogue_One%2C_A_Star_Wars_Story_poster.png",
                        "https://www.youtube.com/watch?v=sC9abcLLQpI")

spiderman_homecoming = media.Movie("Spiderman: Homecoming",
                                   "Peter Parker learns to "
                                   "use his power for good",
                                   "https://upload.wikimedia.org/wikipedia"
                                   "/en/thumb/f/f9/"
                                   "Spider-Man_Homecoming_poster.jpg"
                                   "/220px-Spider-Man_Homecoming_poster.jpg",
                                   "https://www.youtube.com/"
                                   "watch?v=8wNgphPi5VM")

movies = [winter_soldier, civil_war, beauty_and_the_beast, up,
          rogue_one, spiderman_homecoming]
fresh_tomatoes.open_movies_page(movies)
