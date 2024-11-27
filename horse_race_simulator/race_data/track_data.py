from random import choice

class track_data:

    def __init__(self):
        self.track_venue = None
        self.track_weather = None

    def create_track(self):

        # key-value pairs of venues and corresponding distances (in m)
        venues = {
            "Pony Speedway": 1000,
            "Canter Canyon": 1200, 
            "Saddle Summit" : 1600, 
            "Dusty Lanes": 1800, 
            "Gallop Galley": 2200,
            "Riders Run": 2400
            }
        
        self.track_venue = choice(list(venues.items())) 
    
    def weather_factor(self):

        # key-value pairs for weather and impact on the horse speed
        weather = {
            "Sunny": 0,
            "Overcast": 0,
            "Rainy": -10,
            "Snowy": -5,
        }

        self.track_weather = choice(list(weather.items()))
    
    def get_track_info(self):
        print(f"Track: {self.track_venue[0]}, Distance: {self.track_venue[1]}m")
        print(f"Weather: {self.track_weather[0]}")

# test, make sure to remove later
# track = track_data()
# track.create_track()
# track.weather_factor()
# track.get_track_info()