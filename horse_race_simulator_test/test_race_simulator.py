import unittest
from random import seed
from horse_race_simulator.simulation.race_simulator import RaceSimulation
from horse_race_simulator.race_data.race_details import Race
from horse_race_simulator.race_data.track_data import Track

class TestRaceSimulation(unittest.TestCase):

    def setUp(self):
        seed(0)
        self.track = Track()
        self.track.create_track()
        self.track.weather_factor()
        self.race = Race()
        self.simulation = RaceSimulation(self.race, self.track)

    def test_start_race(self): # covers race_setup and update_position
        print("Running test_start_race")
        self.simulation.start_race()
        self.assertIsNotNone(self.simulation.screen) # make sure the graphics screen opens
        self.assertGreater(self.track.track_venue[1] * 0.3, 0) # check that the scaled track is greater than 0
        self.assertEqual(self.simulation.finish_line, 0.3 * self.track.track_venue[1] / 2) # finish line calculation check
        self.assertEqual(len(self.simulation.leg_markers), 3) # making sure there are 3 legs in the race
        for i, (race_horse, horse) in enumerate(self.simulation.horse_objects):
            final_position = self.simulation.race_data[horse.horse_id]["final_position"]
            self.assertGreaterEqual(final_position, 1) # check the positions are greater than or equal to 1
            self.assertLessEqual(final_position, len(self.simulation.horse_objects)) # check that the positions aren't greater than the horses in the race

    def test_get_times(self):
        print("Running test_get_times")
        self.simulation.final_results = {
            3614: {
                "final_position": 1,
                "overall_time": 120.5,
                "leg_times": {"First Leg": 40.0, "Second Leg": 40.0, "Third Leg": 40.5}
            }
        }
        times = self.simulation.get_times()
        self.assertGreater(len(times), 0) # make sure time dictionary is not empty
        self.assertIn(3614, times) # make sure the correct horse id is returned
        self.assertEqual(times[3614]["Overall Time"], 120.5) # check the correct overall time is read
        self.assertEqual(times[3614]["Leg 1 Time"], 40.0) # check that the leg time is correctly read

    def test_get_winning_horse_id(self): # extra test to check if winning horse is selected correctly
        print("Running test_get_winning_horse_id")
        self.simulation.final_results = {
            3614: {"final_position": 1, "overall_time": 120.5, "leg_times": {"First Leg": 40, "Second Leg": 40, "Third Leg": 40.5}},
            3615: {"final_position": 2, "overall_time": 130.0, "leg_times": {"First Leg": 45, "Second Leg": 45, "Third Leg": 40}}
        }
        winning_horse_id = self.simulation.get_winning_horse_id()
        self.assertEqual(winning_horse_id, 3614)

if __name__ == "__main__":
    unittest.main()
