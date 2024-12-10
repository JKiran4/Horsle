# test_race_results.py

import unittest
from unittest.mock import patch
from datetime import datetime
from horse_race_simulator.race_data.horse_stats import Horse
from horse_race_simulator.simulation.race_results import RaceResults

#Mock class to use when testing RaceResults
class Race:
    def __init__(self):
        self.race_id = "race1"
        self.date = datetime.now().strftime("%Y-%m-%d")

# Assuming the Race class is already defined
class TestRaceResults(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #Setting up 3 mock Horse instances
        print("Setting up resources for the entire TestRaceResults class")
        cls.horse1 = Horse(1001, 25, 50, "White", 1, 50)
        cls.horse2 = Horse(2002, 30, 55, "Brown", 2, 60)
        cls.horse3 = Horse(3003, 35, 50, "Red", 3, 70)
        cls.horses = [cls.horse1, cls.horse2, cls.horse3]
        cls.race = Race()

        cls.horse_times = {
            cls.horse1.horse_id : {
                "Overall Time": 100.0,
                "Leg 1 Time": 25.0,
                "Leg 2 Time": 50.0,
                "Leg 3 Time": 75.0
            },
            cls.horse2.horse_id : {
                "Overall Time": 120.0,
                "Leg 1 Time": 30.0,
                "Leg 2 Time": 60.0,
                "Leg 3 Time": 90.0
            },
            cls.horse3.horse_id : {
                "Overall Time": 140.0,
                "Leg 1 Time": 35.0,
                "Leg 2 Time": 70.0,
                "Leg 3 Time": 105.0
            }
        }
        cls.race_results = RaceResults(cls.race, cls.horses, cls.horse_times)

    @classmethod
    def tearDownClass(cls):
        print("Tearing down shared resources")
        cls.horses = None
        cls.race = None
        cls.race_results = None

    def setUp(self):
        print("Setting up testcase")

    def tearDown(self):
        print("Tearing down testcase.")

    def test_constructor(self): # To check default values
        print("Running test_constructor")
        # Check member variables during the initialization of RaceResults
        self.assertIsNotNone(self.race_results.race_id)
        self.assertIsNotNone(self.race_results.date)
        self.assertIsNotNone(self.race_results.horses)
        self.assertIsNotNone(self.race_results.data)

        self.assertEqual(len(self.race_results.horses), len(self.horses))
        self.assertEqual(self.race_results.horses[1].horse_id, self.horses[1].horse_id)

    def test_get_horse_position(self):
        # Check position of each horse. Position is checked against horse_id
        print("Running test_get_horse_position")
        position = self.race_results.get_horse_position(self.horse_times, self.horses[0].horse_id)
        self.assertEqual(position, 1)
        position = self.race_results.get_horse_position(self.horse_times, self.horses[1].horse_id)
        self.assertEqual(position, 2)
        position = self.race_results.get_horse_position(self.horse_times, self.horses[2].horse_id)
        self.assertEqual(position, 3)
        # Check with invalid horse id
        invalid_horse_id = 11
        position = self.race_results.get_horse_position(self.horse_times, invalid_horse_id)
        self.assertEqual(position, -1)

    @patch('builtins.input', side_effect=['A', 'B', 'C', 2002, 'D'])  # Mock input to simulate inputs
    def test_display_options_and_getters(self, mock_input):
        print("Running test_display_options_and_getters")
        # Capture the return value of the method (Note display_options method does not return any value)
        result = self.race_results.display_options()
        self.assertIsNone(result)
        # Testing all the getters used in display_options method with given horse_id
        print("Running get_horse_age")
        horse_age = self.race_results.get_horse_age(self.horses[0].horse_id)
        self.assertEqual(horse_age, self.horses[0].horse_age)
        print("Running get_horse_type")
        horse_type = self.race_results.get_horse_type(self.horses[1].horse_id)
        self.assertEqual(horse_type, self.horses[1].horse_type)
        print("Running get_horse_weight")
        horse_weight = self.race_results.get_horse_weight(self.horses[2].horse_id)
        self.assertEqual(horse_weight, self.horses[2].actual_weight)
        print("Running get_horse_jockey")
        jockey_id = self.race_results.get_horse_jockey(self.horses[0].horse_id)
        self.assertEqual(jockey_id, self.horses[0].jockey_id)
    
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
