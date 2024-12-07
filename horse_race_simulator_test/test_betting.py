# test_betting.py

class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass for testing.")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass after all testing")

    def setUp(self):
        print("setUp user for bet testing.")
        self.user = User(start_balance=1000)

    def tearDown(self):
        print("tearDown user after bet testing")
        del self.user

    def test_balance(self):
        print("Running initial balance testing")
        self.assertEqual(self.user.balance, 1000, "Initial balance should be 1000.")
        another_user = User(start_balance=500)
        self.assertEqual(another_user.balance, 500, "Initial balance should be 500 for another user.")

    def test_take_bet(self):
        print("Running bet testing")
        valid_bet = 50
        self.assertGreater(valid_bet, 0, "Bet should be a positive value")
        self.assertLessEqual(valid_bet, self.user.balance, "Bet cannot exceed balance")
        self.user.balance -= valid_bet
        self.assertEqual(self.user.balance, 950, "Balance should decrease by bet amount")

    def test_distribute_earnings_loss(self):
        print("Running loss testing")
        self.user.balance = 1000
        bet_amount = 100
        winning_horse_id = 2
        selected_horse_id = 1
        self.user.distribute_earnings(bet_amount, winning_horse_id, selected_horse_id)
        self.assertEqual(self.user.balance, 900, "Balance should be 900 after losing the bet.")

if __name__ == "__main__":
    unittest.main()
