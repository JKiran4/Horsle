# test_horse_stats.py

class TestHorse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass for testing.")
        cls.test_horse = Horse(horse_id=3614, horse_age=3, actual_weight=126, horse_type='Gelding', horse_rating=60, jockey_id=63)

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass for testing")
        del cls.test_horse

    def setUp(self):
        print("Setting up horse test")
        self.horse = Horse(horse_id=3614, horse_age=3, actual_weight=126, horse_type='Gelding', horse_rating=60, jockey_id=63)

    def tearDown(self):
        print("Tearing down after horse test.")
        del self.horse

    def test_horse_creation(self):
        print("Running test_horse_creation")
        self.assertEqual(self.horse.horse_id, 3614)
        self.assertEqual(self.horse.horse_age, 3)
        self.assertEqual(self.horse.actual_weight, 126)
        self.assertEqual(self.horse.horse_type, 'Gelding')

    def test_update_horse_stats(self):
        print("Running test_update_horse_stats")
        initial_speed = self.horse.speed
        race_speed = self.horse.update_horse_stats()
        self.assertNotEqual(initial_speed, race_speed)
        self.assertTrue(30.0 <= race_speed <= 55.0)
        if self.horse.horse_age < 3:
            self.assertLess(race_speed, initial_speed)
        if self.horse.actual_weight < 125:
            self.assertGreater(race_speed, initial_speed)

if __name__ == "__main__":
    unittest.main()
