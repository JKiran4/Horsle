# test_race_details.py

import unittest
from datetime import timedelta
from datetime import datetime
from horse_race_simulator.race_data.race_details import DelayedRace

class TestRace(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Setting up resources for the entire TestRace class")
        cls.today_date = datetime.now()
        cls.today_date_str = datetime.now().strftime("%Y-%m-%d")
        cls.num_horses = 10
        cls.race = DelayedRace(num_horses = cls.num_horses)  

        cls.venue_names = ["Pony Speedway", "Canter Canyon", "Saddle Summit", "Dusty Lanes", "Gallop Galley", "Riders Run"]
        cls.venue_distances = [1000, 1200, 1600, 1800, 2200, 2400]
        cls.weather_conditions = ["Sunny", "Overcast", "Rainy", "Snowy"]

    @classmethod
    def tearDownClass(cls):
        print("Tearing down shared resources.")
        cls.race = None   

    def setUp(self):
        print("Setting up testcase.")

    def tearDown(self):
        print("Tearing down testcase.")
    
    def test_constructor(self): # To check deafult values
        print("Running test_constructor")
        # Check below variables are assigned
        self.assertIsNotNone(self.race.track)
        self.assertIn(self.race.venue, self.venue_names) # check if venue name is in list
        self.assertIn(self.race.distance, self.venue_distances) # check if venue distance is in list
        self.assertIn(self.race.weather, self.weather_conditions) # check if weather is in list

        current_date = (self.today_date + timedelta(days=self.race.delay_days)).strftime("%Y-%m-%d")
        self.assertEqual(self.race.date, current_date)
        self.assertGreater(self.race.prize, 4999)
        self.assertLessEqual(self.race.prize, 25000)
        self.assertEqual(self.race.num_horses, self.num_horses)
        self.assertIsNotNone(self.race.race_id)
        self.assertEqual(len(self.race.horses), self.num_horses)

        delay_days = 3
        self.assertEqual(self.race.delay_days, delay_days)

    def test_set_delayed_date(self):
        print("Running test_set_delayed_date")
        delay_days = 5
        self.race.delay_days = delay_days
        current_date = datetime.strptime(self.race.date, "%Y-%m-%d")
        self.race.set_delayed_date()
        # Check values after calling the function
        self.assertEqual(self.race.delay_days, delay_days)
        new_date = (current_date + timedelta(days=(delay_days))).strftime("%Y-%m-%d")
        self.assertEqual(self.race.date, new_date)

    def test_set_date(self):
        print("Running test_set_date")
        # Check values before calling the function
        self.assertNotEqual(self.race.date, self.today_date_str, "It should not match today's date since set_delayed_date was called in the earlier test case.")
        self.race.set_date(self.today_date_str)
        # Check values after calling the function
        self.assertEqual(self.race.date, self.today_date_str)

    def test_get_race_info(self): # extra test, just making sure no exception raised when printing info
        print("Running test_get_race_info")
        self.race.get_race_info() 

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)