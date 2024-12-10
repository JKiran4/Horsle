# test_betting.py

import unittest
from horse_race_simulator.simulation.betting import User

class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass for testing.")
        cls.test_user = User()

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass after all testing")
        del cls.test_user

    def setUp(self):
        print("setUp user for betting testing.")
        self.user = User(start_balance=1000)

    def tearDown(self):
        print("tearDown user after betting testing")
        del self.user

    def test_balance_horse_id(self):
        print("Running balance and horse testing")
        another_user = User(start_balance=500)
        self.user.selected_horse_id = 3614
        self.assertEqual(self.user.balance, 1000, "Initial balance should be 1000")
        self.assertEqual(another_user.balance, 500, "Initial balance should be 500 for another user")
        self.assertIsInstance(self.user.selected_horse_id, int, "Horse choice must be horse_id")
        self.assertGreater(self.user.selected_horse_id, 0, "Horse choice should be greater than 0")

   def test_take_bet(self):
        print("Running bet testing")
        valid_bet = 50
        horse_choice = 3614
        self.user.get_horse_info = [3614, 3615, 3917]
        self.assertGreater(valid_bet, 0, "Bet should be a positive value")
        self.assertLessEqual(valid_bet, self.user.balance, "Bet cannot exceed balance")
        self.user.balance -= valid_bet
        self.assertEqual(self.user.balance, 950, "Balance should decrease by the bet amount")
        self.assertIn(horse_choice, self.user.get_horse_info, "Chosen horse not a valid horse")

if __name__ == "__main__":
    unittest.main()
