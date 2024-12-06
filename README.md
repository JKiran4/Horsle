# Horsle
Required libraries: turtle, time, pandas, random, datetime

Executing the test file should run the whole program. Make sure runs.csv is in the downlaoded package.

Note that the race will only run once, but for added functionality, we may change the simulation library (turtle) so we can run games repeatedly without closing the program. Also, note that Macs have issues with the turtle library displaying the race, but it should still execute the program.

horse_race_simulator/ # package  

race_data/ #subpackage1
- horse_stats.py
  - __init__(self, horse_id, horse_age, actual_weight, horse_type, horse_rating, jockey_id): initialization
  - create_horse(csv_filename): creates horse stats from data set
  - update_horse_stats(self): updates horse speed based on horse stats
  - get_horse_info(self): display horses stats
- track_data.py
  - __init__(self): initialization
  - create_track(self): randomly selects track venue and corresponding race distance
  - weather_factors(self): randomly selects weather factors to apply to race, which adjusts horse speed 
  - get_track_info(self): displays track information
- race_details.py
  - __init__(self num_horses = 5): initialization
  - set_date(self, date): adjusts race date
  - get_race_info(self): displays race_id, date, venue, distance, prize, and number of horses


simulation/ #subpackage2  
- race_simulator.py
  - __init__(self, race, track): initialization
  - draw_track(self, scaled_length): creates track imagery used for race simulation
  - race_setup(self): sets up race environment - prepares screen, scales track and initializes horses.
  - update_position(self): updates horse position during race, tracks progress and checks for finish. starts time and applies weather factors.
  - start_race(self): starts race via race_setup and update_position methods
  - get_times(self): returns a dictionary of race times for each horse.
  - get_winning_horse_id(self): returns winning horse ID
- race_results.py
  - __init__(self, race, horses, horse_timings): initialization
  - get_horse_timing_data_frame(self, horse_timings): retrieves data frame with horse times
  - get_horse_position(self, horse_timings, horse_id): finds a horse's position at race stage
  - display_options(self): options for displaying results
  - display_leaderboard(self): displays leaderboard of race results
  - generate_race_summary(self): display the race summary
  - get_horse_performance(self): retrieves performance details for specific horse
  - various supplementary methods were included in this module for ease of functionality in the methods
- betting.py
  - __init__(self, start_balance=1000): initialization
  - race_welcome(self): issues user prompts in order to begin race and proceed
  - run_game(self): consolidates the betting, race results and simulation
  - show_balance(self): shows users current balance
  - take_bet(self, bet, horse_id, horses): user input for bet - if 0 or horse_id invalid, does not accept bets
  - distribute_earnings(self, bet, winning_horse_id, selected_horse_id, odds=2.0): Assesses if selected horse wins race, if wins - adds bet to balance