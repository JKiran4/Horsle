# track_data.py

from random import choice

class Track:
    """A class representing horse race track with venue options and weather factors
    Methods:
        __init__(): Intializes track data
        create_track(): Establishes track venues
        weather_factor(): Selects weather factor and corresponding impact on race
        get_track_info(): Displays details about venue, distance, and weather
    """

    def __init__(self):
        """Initializes track data
        Methods:
            track_venue: Contains track venues and distances
            track_weather: Contains weather factors and speed impact
        """        
        self.track_venue = None
        self.track_weather = None
        self.track_color = "DarkGreen" 

    def create_track(self):
        """Randomly selects track venue and corresponding race distance.
        Stores details in track_venue.
        Args:
           self: track_data
        Returns:
           None
        """

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
        """Randomly selects weather factors to apply to horse race and
        corresponding impact the selected factor has on horse speed.
        Stores details in track_weather.
        Args:
           self: track_data
        Returns:
           None
        """

        # key-value pairs for weather and impact on the horse speed
        weather = {
            "Sunny": 0,
            "Overcast": 0,
            "Rainy": -10,
            "Snowy": -5,
        }

        self.track_weather = choice(list(weather.items()))
    
    def get_track_info(self):
        """Prints details about the track venue, distance and track weather
        Args:
           self: track_data
        Returns:
           None
        """        
        print(f"Track: {self.track_venue[0]}, Distance: {self.track_venue[1]}m")
        print(f"Weather: {self.track_weather[0]}")
