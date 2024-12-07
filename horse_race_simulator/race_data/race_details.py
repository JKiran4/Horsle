# race_details.py
from datetime import datetime
from datetime import timedelta
from random import choice
from horse_race_simulator.race_data.track_data import Track
from horse_race_simulator.race_data.horse_stats import Horse

class Race:
    """A class representing a horse race (not the actual simulation)
    Methods:
        __init__(): Intializes race information
        set_date(): Change race date if required (delays, cancellations, etc.)
        get_race_info(): Prints details about the race
    """

    def __init__(self, num_horses=5):
        """Initialize race with race details."""
        self.track = Track()
        self.track.create_track() 
        self.track.weather_factor()

        self.venue = self.track.track_venue[0]
        self.distance = self.track.track_venue[1]
        self.weather = self.track.track_weather[0]

        self.date = datetime.now().strftime("%Y-%m-%d") 
        self.prize = choice(range(5000, 25001, 5000)) 
        self.num_horses = num_horses
        self.race_id = id(self)

        # Create horses based on the number of horses for this race
        self.horses = [Horse.create_horse("runs.csv") for _ in range(self.num_horses)]

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
        width = 40
        separator = "+" + "-" * (width - 2) + "+"

        print(
            f"\n{separator}\n"
            f"| {'      Overview of Today`s Race      '} |\n"  # Correctly centered title
            f"{separator}\n"
            f"| {'Race ID':<10} : {self.race_id:<23} |\n"
            f"| {'Date':<10} : {self.date:<23} |\n"
            f"| {'Venue':<10} : {self.venue:<23} |\n"
            f"| {'Distance':<10} : {f'{self.distance}m':<23} |\n"
            f"| {'Weather':<10} : {self.weather:<23} |\n"
            f"| {'Prize':<10} : {f'${self.prize:,}':<23} |\n"
            f"| {'Horses':<10} : {self.num_horses:<23} |\n"
            f"{separator}"
        )

class DelayedRace(Race):
    """A subclass of Race representing a race that has been delayed.
    Methods:
        __init__(): Initializes delayed race information
        set_delayed_date(): set the new delayed date for the race
        get_race_info(): get the race info with delay"""
    
    def __init__(self, num_horses = 5, delay_days = 3):
        """Initialize a delayed race, which inherits from the Race class and allows setting a new date."""
        super().__init__(num_horses)
        
        # Calculate the new date after applying the delay
        self.delay_days = delay_days
        self.set_delayed_date()

    def set_delayed_date(self):
        """Get details about the race
        Parameters:
           self: the race object
        Returns:
           new date: the new date base don the delay
        """
        current_date = datetime.strptime(self.date, "%Y-%m-%d")
        new_date = current_date + timedelta(days=self.delay_days)
        self.set_date(new_date.strftime("%Y-%m-%d"))

    def get_race_info(self):
        """Get details about the race
        Parameters:
           self: the race object
        Returns:
           print statement: A set of information for the race with the delay accounted for
        """
        print(f"\nDue to severe weather, the race was delayed by {self.delay_days} days")
        super().get_race_info()
