import islamic_movies
import media

The_Massage = media.Movie("The Massage(1977)",
                        "The new trailer for the 1977 film, "The Message", a historical epic directed by Moustapha Akkad and starring Anthony Quinn, which chronicles the life of the prophet Mohammed and the birth of Islam.",
                        "http://ia.media-imdb.com/images/M/MV5BMjE0OTY0ODk2MF5BMl5BanBnXkFtZTcwNjQ5NjIzMQ@@._V1_.jpg",
                        "https://www.youtube.com/watch?v=rO_Ml_eYED4")
#print(toy_story.storyline)
Omar = media.Movie("Omar",
                     ""Omar", the most important drama series produced in recent TV history in the region, chronicles the life and achievements of one of the most important icons in Islam. (MBC).",
                     "http://2.bp.blogspot.com/-CZ2x6aMG1oM/UArd5V63plI/AAAAAAAAACE/D1VqZ8I_m6Q/s1600/4.jpg",
                     "http://www.youtube.com/watch?v=LmoLdgbazBU")
#print(avatar.storyline)
#avatar.show_trailer()
Salahuddin_Al_Ayoubi = media.Movie("Salahuddin Al Ayoubi",
                     "Salahuddin Al Ayoubi.",
                     "http://www.tarakucha.com/saladin/2011_print01.jpg",
                     "https://www.youtube.com/watch?v=QIJD2jaAfBg")


Motivated_People = media.Movie("Motivated People",
                              "Are you feeling lazy? Need motivation and an Imaan boost? - Shaykh Zahir Mahmood of the As-Suffa Institue gives an inspiring reminder on the legends of Islam. These were people who were motivated, it is an example we need to follow and become people of substance.",
                              "https://i.ytimg.com/vi/ZJkjR_Lnkxg/maxresdefault.jpg",
                              "http://www.youtube.com/watch?v=ZJkjR_Lnkxg")

The_Untold_History_How_Islam_Spread= media.Movie("The Untold History - How Islam Spread",
                              "The Untold History - How Islam Spread.",
                              "https://yt3.ggpht.com/-B-qffEHEM3s/AAAAAAAAAAI/AAAAAAAAAAA/ej_Atu-ZkkM/s900-c-k-no-rj-c0xffffff/photo.jpg",
                              "https://www.youtube.com/watch?v=a8CbEzcOX3M")

Islam_and_minor_signs_of_the_day_of_judgement= media.Movie("Islam and minor signs of the day of judgement",
                              "When fornication becomes widespread among your leaders (The Prophet, peace be upon him, said that this will happen when the people stop forbidding evil) (Ibn Majah).",
                              "https://i.ytimg.com/vi/W0vvOh59bAQ/hqdefault.jpg",
                              "https://www.youtube.com/watch?v=W0vvOh59bAQ")

movies = [The_Massage, Omar, Salahuddin_Al_Ayoubi, Motivated_People, The_Untold_History_How_Islam_Spread, Islam_and_minor_signs_of_the_day_of_judgement]

#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
