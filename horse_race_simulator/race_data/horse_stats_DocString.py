#IN PROGRESS - KS

# Creating temporary Race class - will be supplied by Amali
class Race:
    num_horses = 10

class Horse:
     """A class representing a Horse object.
    Methods:
        __init__(): Initializes 'Horse' instance.
        create_horse(): Retreives a subset of horses from the Kaggle data set.
        update_horse_stats(): Updates speed of a horse.
        get_horse_info(): Displays horse details.
    """
    def __init__(self, horse_id, horse_age, actual_weight, horse_type, horse_rating, jockey_id):
        """
        Initializes instance of the 'Horse' class.
    
        Args:
            horse_id (int): Horse ID.
            horse_age (int): Horse age.
            actual_weight (int): Actual weight of horse.
            horse_type (str): Horse type such as Colt, Mare, Gelding etc.
            horse_rating (int): Horse rating.
            jockey_id (int): Jockey ID.
        """
        self.horse_id = horse_id
        self.horse_age = horse_age
        self.actual_weight = actual_weight
        self.horse_type = horse_type
        self.horse_rating = horse_rating
        self.jockey_id = jockey_id
        self.speed = self.update_horse_stats()

    def create_horse(csv_filename):
        """
        Retreives a subset of horses from the given data set 'csv_filename'.
    
        Args:
            csv_filename: Kaggle data set containing horse data.
        """
        horse_df = pd.read_csv(csv_filename)

        horses = []

        # Update requested by group member to incorportate number of horses instead of hard-coding
        num_horses = Race.num_horses

        while len(horses) < num_horses: # instead of 10 > use an attribute defined in Race Class
            horse_selection = horse_df.sample(n=1).iloc[0]

            horse_id = horse_selection['horse_id']
            horse_age = horse_selection['horse_age']
            actual_weight = horse_selection['actual_weight']
            horse_type = horse_selection['horse_type']
            horse_rating = horse_selection['horse_rating']
            jockey_id = horse_selection['jockey_id']

            horse_object = Horse(horse_id, horse_age, actual_weight, horse_type, horse_rating, jockey_id)

            if horse_object not in horses:
                horses.append(horse_object)
        return horses

    # Will incorporate randomization to ensure that values will be different every time?
    def update_horse_stats(self):
        """
        Updates speed of a horse based on factors;horse rating, horse age, actual weight of a horse and uses randomization to ensure that values vary with each simulation.
    
        Args:
            self: Instance of the class.
        """
        random_speed = random.uniform(30.0, 50.0)
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
        """
        Displays horse details.
        
        Args:
            self: Instance of the class.
        """
        print(f'Horse ID: {self.horse_id}, Age: {self.horse_age} years, Weight: {self.actual_weight} lbs, Type: {self.horse_type}, Rating: {self.horse_rating}, Speed: {self.speed}')


# Code Used to test
horses = create_horse('runs.csv')

# Print information for each horse
for horse in horses:
    horse.get_horse_info()
