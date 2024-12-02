# Data used to generate information imported from 'https://www.kaggle.com/datasets/gdaley/hkracing'

class User:
    def __init__(self, start_balance=1000):
        self.balance = start_balance

    def race_welcome(self, horses):
        print("Welcome to the Horse Race!")
        while True:
            start_check = input("Type 'start' to begin the race or 'exit' to quit: ").lower()
            if start_check == "exit":
                print("Thank you for racing! Goodbye!")
                break
            elif start_check == 'start':
                self.show_balance()
                bet_amount_placed = self.take_bet(horses)
                continue
            race = RaceSimulation.start_race(horses)
            winning_horse_id = RaceResults.getWinningHorseId()
            RaceResults.display_options()
            self.distribute_earnings(self, bet, winning_horse_id, selected_horse_id, odds=2.0)
            self.show_balance()
            if self.balance <= 0:
                print("You have run out of money!")
                break
            else:
                run_again = input("Would you like to run another race? (Y/N): ").lower()
                if run_again != 'n':
                    print("Thank you for playing! Goodbye.")
                    break

    def show_balance(self):
        print(f"Current Balance: ${self.balance}")

    def take_bet(self, bet, horse_id, horses):
        bet = float(input("Enter bet amount: $"))
        horse_choice = int(input(f"Choose a horse from {[horse.horse_id for horse in horses]}: "))
        if bet > self.balance:
            print("Insufficient funds to place bet")
            return None
        if bet <= 0:
            print("Bet amount must be greater than zero.")
            return None
        valid_horses = [horse for horse in horses if horse.horse_id == horse_id]
        if not valid_horses:
            print(f"Invalid horse ID: {horse_id}")
            return None
        self.balance -= bet
        print(f"Bet of ${bet} placed on horse ID {horse_id}.")
        return bet

    def distribute_earnings(self, bet, winning_horse_id, selected_horse_id, odds=2.0):
        if winning_horse_id == selected_horse_id:
            winnings = bet * odds
            self.balance += winnings
            print(f"Congratulations! Horse ID {selected_horse_id} won. You earned ${winnings:.2f}.")
        else:
            print(f"Sorry, Horse ID {selected_horse_id} did not win. Your balance will be reduced by ${bet}.")
