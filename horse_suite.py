import unittest

from horse_race_simulator_test.test_horse_stats import TestHorse
from horse_race_simulator_test.test_betting import TestUser

def horse_suite(): # temporary name, please feel free to change if you have a preference
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(TestHorse('test_horse_creation'))
    suite.addTest(TestHorse('test_update_horse_stats'))
    suite.addTest(TestUser('test_balance_horse_id'))
    suite.addTest(TestUser('test_take_bet'))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

horse_suite()