# test_race_details.py

import unittest
from datetime import timedelta
from datetime import datetime
from horse_race_simulator.race_data.race_details import Race
from horse_race_simulator.race_data.race_details import DelayedRace

class TestRace(unittest.TestCase):
    today_date = datetime.now()
    num_horses = 10
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass for testing Race.")
        cls.test_race = DelayedRace()  

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass for testing Race.")
        del cls.test_race

    def setUp(self):
        print("Setting up Race test")
        self.race = DelayedRace(num_horses = TestRace.num_horses)

    def tearDown(self):
        print("Tearing down after Race test.")
        del self.race  # Clean up after each test

    def test_constructor(self): # To check deafult values
        print("Running test_constructor")
        # Check below variables are assigned
        self.assertIsNotNone(self.race.track) 
        venue_names = ["Pony Speedway", "Canter Canyon", "Saddle Summit", "Dusty Lanes", "Gallop Galley", "Riders Run"]
        self.assertIn(self.race.venue, venue_names) # check if venue name is in list
        venue_distances = [1000, 1200, 1600, 1800, 2200, 2400]
        self.assertIn(self.race.distance, venue_distances) # check if venue distance is in list
        weather_conditions = ["Sunny", "Overcast", "Rainy", "Snowy"]
        self.assertIn(self.race.weather, weather_conditions) # check if weather is in list

        current_date = (TestRace.today_date + timedelta(days=self.race.delay_days)).strftime("%Y-%m-%d")
        self.assertEqual(self.race.date, current_date)
        self.assertGreater(self.race.prize, 4999)
        self.assertLessEqual(self.race.prize, 25000)
        self.assertEqual(self.race.num_horses, TestRace.num_horses)
        self.assertIsNotNone(self.race.race_id)
        self.assertEqual(len(self.race.horses), TestRace.num_horses)

        delay_days = 3
        self.assertEqual(self.race.delay_days, delay_days)

    def test_set_delayed_date(self):
        print("Running test_set_delayed_date")
        # Check values before calling the function
        delay_days = 3 # Default value
        current_date = (TestRace.today_date + timedelta(days=delay_days)).strftime("%Y-%m-%d")
        self.assertEqual(self.race.date, current_date)
        self.assertEqual(self.race.delay_days, delay_days)
        delay_days = 5
        self.race.delay_days = delay_days
        self.race.set_delayed_date()
        # Check values after calling the function
        self.assertEqual(self.race.delay_days, delay_days)
        new_date = datetime.strptime(current_date, "%Y-%m-%d") + timedelta(days=(delay_days))
        new_date_str = (new_date).strftime("%Y-%m-%d")
        self.assertEqual(self.race.date, new_date_str)

    def test_set_date(self):
        print("Running test_set_date")
        # Check values before calling the function
        current_date = (TestRace.today_date + timedelta(days=self.race.delay_days)).strftime("%Y-%m-%d") 
        self.assertEqual(self.race.date, current_date)
        new_date = (TestRace.today_date + timedelta(days=10)).strftime("%Y-%m-%d")
        self.race.set_date(new_date)
        # Check values after calling the function
        self.assertEqual(self.race.date, new_date)

    def test_get_race_info(self): # extra test, just making sure no exception raised when printing info
        print("Running test_get_race_info")
        self.race.get_race_info() 

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)