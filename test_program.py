
from horse_race_simulator.simulation.betting import User  # Import the User class from betting

# Create a user instance (starting balance of $1000)
user = User(start_balance=1000)

# Simulate the race welcome process where the user interacts
# Here, we're calling `race_welcome` method which runs the game logic
# In this case, we're assuming the user will select "start" to run the game/
user.race_welcome()  # Pass the list of horses from the race
