#race_details.py

# Creating Race class
class Race:
    """A class representing a horse race (not the actual simulation)
    Methods:
        __init__(): Intializes race information
        set_date(): Change race date if required (delays, cancellations, etc.)
        get_race_info(): Prints details about the race
    """

    id = 1 # start at race id 1, useful to track id if multiple races are run
    def __init__(self, date, venue, distance, prize, num_horses = 5):
        """Initialize race with race details."""
        self.date = date
        self.venue = venue
        self.distance = distance
        self.prize = prize
        self.num_horses = num_horses # Number of horses of the race
        self.race_id = Race.id
        Race.id += 1
                                 
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
        print(f"Race_id:{self.race_id}\nDate: {self.date}\nvenue: {self.venue}\ndistance: {self.distance}\nprize: {self.prize}\nNumber of horses: {self.num_horses}\n")


# Test code

# Initialize Race objects
# R1 = Race('2024-11-25','ST', 1400, 485000)
# R2 = Race('2024-11-26','HV', 1200, 625000,10)

# # Display race results
# R1.get_race_info()
# R2.get_race_info()

# # Change date for Race 2
# R2.set_date('2024-11-30')
# R2.get_race_info()

# # Get number of horses for retreiving data in the create_horse() method within the 'Horse' class
# print(R1.num_horses)
# print(R2.num_horses)

