# test_program.py

from horse_race_simulator.simulation.race_simulator import RaceSimulator
from horse_race_simulator.race_data.race_details import Race

def main():
    race = Race()
    simulator = RaceSimulator(race, race.track)
    simulator.start_race()

if __name__ == "__main__":
    main()
