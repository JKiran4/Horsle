# test_track_data.py

import unittest
from random import seed
from track_data import Track

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
        self.assertGreater(self.track.track_venue[1], 0) # check if the distance is greater than 0

    def test_weather_factor(self):
        print("Running test_weather_factor")
        self.track.weather_factor()
        self.assertIsNotNone(self.track.track_weather) # check if weather exists
        self.assertIsInstance(self.track.track_weather[1], int) # check if the factor associated with weather is an integer

    def test_get_track_info(self):
        print("Running test_get_track_info")
        self.track.create_track() # simply check methods are working here
        self.track.weather_factor()
        self.track.get_track_info() 

if __name__ == "__main__":
    unittest.main()
