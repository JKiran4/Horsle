# betting.py

from horse_race_simulator.simulation.race_simulator import RaceSimulation
from horse_race_simulator.simulation.race_results import RaceResults
from horse_race_simulator.race_data.race_details import DelayedRace


class User:
    """A class representing a User object.
    Methods:
        __init__(): Initializes 'User' instance.
        race_welcome(): Opening prompt for the game.
        run_game(): Consolidate the betting, race results and simulation into one method.
        show_balance(): Show user balance for the instance.
        take_bet(): Takes bet from user.
        distribute_earnings(): Distribute earnings after the race is completed.
    """
    def __init__(self, start_balance=1000):
        """
        Initializes instance of the 'User' class.

        Args:
            start_balance (int): Start balance of user, with default value = 1000.
        """
        self.balance = start_balance

    def race_welcome(self):
        """
        Opening prompt for the game.

        Args:
            self : Instance of the class.
        """
        print("Welcome to Horsle, a horse race simulator with turtles!")
        while True:
            start_check = input("Type 'start' to begin the race or 'exit' to quit: ").lower()
            if start_check == "exit":
                print("Thank you for racing! Goodbye!")
                break
            elif start_check == "start":
                self.run_game()
                if self.balance <= 0:
                    print("You have run out of money! Goodbye!")
                    break
                else:
                    print("Thank you for playing! Goodbye!")
                    break

    def run_game(self):
        """
        Consolidate the betting, race results and simulation into one method.

        Args:
            self : Instance of the class.
        """
        race = DelayedRace()
        race.get_race_info()
        track = race.track

        print("+" + "-" * 105 + "+")
        print("|                                         Horses in Today`s race:                                         |")
        print("+" + "-" * 105 + "+")

        for horse in race.horses:
            horse.get_horse_info()

        print("+" + "-" * 105 + "+")

        selected_horse_id = None
        bet = None
        while bet is None:
            bet, selected_horse_id = self.take_bet(race.horses)
            if bet is None:
                return

        # Run the race
        try:
            race_simulation = RaceSimulation(race, track)
            race_simulation.start_race()
            winning_horse_id = race_simulation.get_winning_horse_id()
            horse_times = race_simulation.get_times()
        except Exception as e:
            print(f"Error during race simulation: {e}")
            return

        # Display results and distribute earnings
        self.distribute_earnings(bet, winning_horse_id, selected_horse_id)
        self.show_balance()
        results = RaceResults(race, race.horses, horse_times)
        results.display_options()


    def show_balance(self):
        """
        Show user's starting balance for the instance.

        Args:
            self : Instance of the class.
        """
        print(f"Your balance is: ${self.balance:.2f}")

    def take_bet(self, horses):
        """
        Takes bet from user.

        Args:
            self : Instance of the class.
            horses (list) : List of Horse IDs for the current race.

        Returns:
            bet (int) : Bet value.
            horse_choice (int) : Horse ID of horse selected by the user.

        """

        while True:
            try:
                horse_choice = int(input(f"Choose a horse to place a bet on for today's race: "))

                valid_horses = [horse for horse in horses if horse.horse_id == horse_choice]
                if not valid_horses:
                    print(f"Horse {horse_choice} is not in today's race. Please select a valid horse.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid horse ID.")
                continue

        self.show_balance()

        while True:
            try:
                bet = float(input("How much would you like to bet? $"))

                if bet > self.balance:
                    print("Insufficient funds to place bet. Please enter a valid amount.")
                    continue
                elif bet <= 0:
                    print("Bet amount must be greater than zero. Please enter a valid bet.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid numeric bet amount.")
                continue

        self.balance -= bet

        print(f"You have placed a bet of ${bet:.2f} on horse {horse_choice}. The race will start shortly, good luck!\n")

        return bet, horse_choice

    def distribute_earnings(self, bet, winning_horse_id, selected_horse_id, odds=2.0):
        """
        Distribute earnings after the race is completed.

        Args:
            self : Instance of the class.
            bet (int) : Bet value.
            winning_horse_id (int) : Horse ID of winner of the race.
            selected_horse_id (int) : Horse ID of horse selected by the user.
            odds (int) : Odds of winning, default value set to 2.0.

        """
        if winning_horse_id == selected_horse_id:
            winnings = bet * odds
            self.balance += winnings
            print(f"\nCongratulations! Horse ID {selected_horse_id} won. You earned ${winnings:.2f}.")
        else:
            print(f"\nSorry, Horse ID {selected_horse_id} did not win. Your balance will be reduced by ${bet:.2f}.")
