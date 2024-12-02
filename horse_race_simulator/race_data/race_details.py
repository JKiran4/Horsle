# race_details.py

from datetime import datetime
from random import choice
from track_data import Track

class Race:
    """A class representing a horse race (not the actual simulation)
    Methods:
        __init__(): Intializes race information
        set_date(): Change race date if required (delays, cancellations, etc.)
        get_race_info(): Prints details about the race
    """

    def __init__(self, num_horses = 5):
        """Initialize race with race details."""

        # call track information from the track module
        track = Track()
        track.create_track() 
        track.weather_factor()

        self.venue = track.track_venue[0]
        self.distance = track.track_venue[1]
        self.weather = track.track_weather[0]

        self.date = datetime.now().strftime("%Y-%m-%d") 
        self.prize = choice(range(5000, 25001, 5000)) 
        self.num_horses = num_horses
        self.race_id = Race.id

    def set_date(self, date):
        """Change the date for the race
        Parameters:
           self: the race object
           date: the date to change to
        Returns:
           None
        """
        self.date = date

    def get_race_info(self):
        """Get details about the race
        Parameters:
           self: the race object
        Returns:
           print statement: A set of information for the race
        """
        print(f"Race ID: {self.race_id}\n"
            f"Date: {self.date}\n"
            f"Venue: {self.venue}\n"
            f"Distance: {self.distance}m\n"
            f"Weather: {self.weather}\n"
            f"Prize: ${self.prize}\n"
            f"Number of horses: {self.num_horses}\n"
        )
