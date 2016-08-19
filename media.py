import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

billy_cyrus = Parent("Cyrus", "blue")
billy_cyrus.show_info()
#miley_cyrus = Child("Cyrus", "Blue", 5)
 
