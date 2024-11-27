# IN PROGRESS - KS
# Data used to generate information imported from 'https://www.kaggle.com/datasets/gdaley/hkracing'

class User:
    def __init__(self, start_balance=1000):
        self.balance = start_balance
    # Show user's starting balance
    def show_balance(self):
        print(f"Current Balance: ${self.balance}")
    # Takes bet based on horse_id
    def take_bet(self, bet, horse_id, horses):
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
        # Reduces user's balanced based on betting amount
        self.balance -= bet
        print(f"Bet of ${bet} placed on horse ID {horse_id}.")
        return bet
    # Assesses if selected horse wins race, if wins - adds bet to balance
    def distribute_earnings(self, bet, winning_horse_id, selected_horse_id, odds=2.0):
        if winning_horse_id == selected_horse_id:
            winnings = bet * odds
            self.balance += winnings
            print(f"Congratulations! Horse ID {selected_horse_id} won. You earned ${winnings:.2f}.")
        else:
            print(f"Sorry, Horse ID {selected_horse_id} did not win. Your balance will be reduced by ${bet}.")

# Made temporary race class/methods to check the betting module - will remove
class TestRace:
    def __init__(self, horses):
        self.horses = horses

    def testing_race(self):
        winning_horse = random.choice(self.horses)
        return winning_horse.horse_id

# Included the test code here used to check functionality - will move
if __name__ == "__main__":
    horses = Horse.create_horse("runs.csv")

    user = User()

    user.show_balance()
    # Prompts user for bet amount
    bet = float(input("Enter bet amount: $"))
    horse_choice = int(input(f"Choose a horse from {[horse.horse_id for horse in horses]}: "))

    bet_amount_placed = user.take_bet(bet, horse_choice, horses)
    # Checks to make sure bet is valid 
    if bet_amount_placed is not None:
        race = TestRace(horses)

        winning_horse = testing_race.race()

        user.distribute_earnings(bet_amount_placed, winning_horse, horse_choice)

        user.show_balance()
