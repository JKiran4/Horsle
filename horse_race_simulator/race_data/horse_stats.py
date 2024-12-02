# Data used to generate information imported from 'https://www.kaggle.com/datasets/gdaley/hkracing'

class Horse:
    def __init__(self, horse_id, horse_age, actual_weight, horse_type, horse_rating, jockey_id):
        self.horse_id = horse_id
        self.horse_age = horse_age
        self.actual_weight = actual_weight
        self.horse_type = horse_type
        self.horse_rating = horse_rating
        self.jockey_id = jockey_id
        self.speed = self.update_horse_stats()

    def create_horse(csv_filename):
        horse_df = pd.read_csv(csv_filename)

        horses = []

        num_horses = Race.num_horses

        while len(horses) < num_horses:
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

    def update_horse_stats(self):
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
        print(f'Horse ID: {self.horse_id}, Age: {self.horse_age} years, Weight: {self.actual_weight} lbs, Type: {self.horse_type}, Rating: {self.horse_rating}, Speed: {self.speed}')


# Code Used to test
horses = create_horse('runs.csv')

# Print information for each horse
for horse in horses:
    horse.get_horse_info()
