# test_track_data.py

import unittest
from random import seed
from horse_race_simulator.race_data.track_data import Track

# Assuming the Track class is already defined
class TestTrack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass for testing Track.")
        seed(0) # seed for reproducibility
        cls.test_track = Track()  

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass for testing Track.")
        del cls.test_track

    def setUp(self):
        print("Setting up Track test")
        self.track = Track()

    def tearDown(self):
        print("Tearing down after Track test.")
        del self.track  # Clean up after each test

    def test_create_track(self):
        print("Running test_create_track")
        self.track.create_track()
        self.assertIsNotNone(self.track.track_venue) # check if venue exists
        venue_names = ["Pony Speedway", "Canter Canyon", "Saddle Summit", "Dusty Lanes", "Gallop Galley", "Riders Run"]
        self.assertIn(self.track.track_venue[0], venue_names) # check if venue name is in list
        self.assertGreater(self.track.track_venue[1], 0) # check if the distance is greater than 0
        self.assertLessEqual(self.track.track_venue[1], 2400)  # Check if the distance is less than or equal to 2400

    def test_weather_factor(self):
        print("Running test_weather_factor")
        self.track.weather_factor()
        self.assertIsNotNone(self.track.track_weather) # check if weather exists
        weather_conditions = ["Sunny", "Overcast", "Rainy", "Snowy"]
        self.assertIn(self.track.track_weather[0], weather_conditions) # check if weather is in list
        self.assertIsInstance(self.track.track_weather[1], int) # check if the factor associated with weather is an integer
        self.assertLessEqual(self.track.track_weather[1], 0) # check that the factor of weather is less than or equal to 0

    def test_get_track_info(self): # extra test, just making sure no exception raised when printing info
        print("Running test_get_track_info")
        self.track.create_track() # simply check methods are working here
        self.track.weather_factor()
        self.track.get_track_info() 

if __name__ == "__main__":
    unittest.main()
