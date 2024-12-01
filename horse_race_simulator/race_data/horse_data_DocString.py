# horse_stats.py
import pandas as pd

class Horse:
    """A class representing horse
    Methods:
        __init__(): Intializes horse information
        create_horses(): Creates horse objects based on specified number of horses
        update_horse_stats(): Provides ability to update horse performance based on dataset
        get_horse_info(): Prints details about a given horses information
    """
    def __init__(self, horse_id, horse_age, actual_weight, horse_type, horse_rating, jockey_id):
        """Initializes horse information which will be stored"""
        self.horse_id = horse_id
        self.horse_age = horse_age
        self.actual_weight = actual_weight
        self.horse_type = horse_type
        self.horse_rating = horse_rating
        self.jockey_id = jockey_id
        self.speed = self.update_horse_stats()

    def create_horse(csv_filename):
        """Creates a horse based on a data file input
        Parameters:
           csv_filename: the data file (in csv format) used to read horse data
        Returns:
           horses: the information for the horses
        """
        horse_df = pd.read_csv(csv_filename)

        horses = []

        # hard-coded value for simplicity, but may be changed so user can set number of race horses
        num_horses = 5

        while len(horses) < num_horses: # only create horses up to the maximum of 5 (for now)
            horse_selection = horse_df.sample(n=1).iloc[0]

            horse_id = horse_selection['horse_id']
            horse_age = horse_selection['horse_age']
            actual_weight = horse_selection['actual_weight']
            horse_type = horse_selection['horse_type']
            horse_rating = horse_selection['horse_rating']
            jockey_id = horse_selection['jockey_id']

            horse_object = Horse(horse_id, horse_age, actual_weight, horse_type, horse_rating, jockey_id)

            # add horses to the collection
            if horse_object not in horses:
                horses.append(horse_object)
        return horses

    def update_horse_stats(self):
        """Updates a horses stats related to speed specifically
        Parameters:
           self: the horse object
        Returns:
           random_speed: the calcualted (semi-random) speed of the horse
        """
        random_speed = random.uniform(30.0, 50.0) # generate a random speed and add modifiers
        if self.horse_rating > 50:
            random_speed += 5
        if self.horse_age < 3:
            random_speed -= 2
        elif self.horse_age > 5:
            random_speed -= 5
        elif self.actual_weight < 125:
            random_speed += 5
        return round(random_speed, 2)

    def get_horse_info(self):
        """Prints horse information
        Parameters:
           self: the horse object
        Returns:
           print statement: A set of information related to a given horse
        """
        print(f'Horse ID: {self.horse_id}, Age: {self.horse_age} years, Weight: {self.actual_weight} lbs, Type: {self.horse_type}, Rating: {self.horse_rating}, Speed: {self.speed}')


# Testing code
# horses = create_horse('runs.csv')

# # Print information for each horse
# for horse in horses:
#     horse.get_horse_info()
