# betting.py

from horse_race_simulator.simulation.race_simulator import RaceSimulation
from horse_race_simulator.simulation.race_results import RaceResults
from horse_race_simulator.race_data.race_details import Race  


class User:
    def __init__(self, start_balance=1000):
        self.balance = start_balance

    def race_welcome(self):
        """
        Opening prompt for the game
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
                    print("You have run out of money!")
                    break
                run_again = input("Would you like to run another race? (Y/N): ").lower()
                if run_again == "n":
                    print("Thank you for playing! Goodbye.")
                    break

    def run_game(self):
        """
        Consolidate the betting, race results and sim into one method
        """
        self.show_balance()


        race = Race()
        race.get_race_info()
        track = race.track
        race_simulation = RaceSimulation(race, track)  # Pass both race and track to simulation

        print("\nHorses in today's race:")
        for horse in race.horses:
            horse.get_horse_info()

        bet, selected_horse_id = self.take_bet(race.horses)
        if bet is None:
            return

        # Run the race
        race_simulation.start_race()
        winning_horse_id = race_simulation.get_winning_horse_id()
        horse_times = race_simulation.get_times()

        # Display results and distribute earnings
        results = RaceResults(race, race.horses, horse_times)
        results.display_options()
        self.distribute_earnings(bet, winning_horse_id, selected_horse_id)

        # Show updated balance
        self.show_balance()

    def show_balance(self):
        print(f"Current Balance: ${self.balance}")

    def take_bet(self, horses):

        horse_choice = int(input(f"Choose a horse from {[horse.horse_id for horse in horses]}: "))
        valid_horses = [horse for horse in horses if horse.horse_id == horse_choice]
        if not valid_horses:
            print(f"Invalid horse ID: {horse_choice}")
            return None
        
        bet = float(input("Enter bet amount: $"))
        if bet > self.balance:
            print("Insufficient funds to place bet")
            return None
        if bet <= 0:
            print("Bet amount must be greater than zero.")
            return None
        
        self.balance -= bet
        
        print(f"Bet of ${bet} placed on horse ID {horse_choice}.")

        return bet, horse_choice

    def distribute_earnings(self, bet, winning_horse_id, selected_horse_id, odds=2.0):
        if winning_horse_id == selected_horse_id:
            winnings = bet * odds
            self.balance += winnings
            print(f"Congratulations! Horse ID {selected_horse_id} won. You earned ${winnings:.2f}.")
        else:
            print(f"Sorry, Horse ID {selected_horse_id} did not win. Your balance will be reduced by ${bet}.")