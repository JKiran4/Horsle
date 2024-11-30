# Horse-Race-Simulator

horse_race_simulator/ # package  
race_data/ #subpacakge1
- horse_stats.py
  - create_horse(csv_filename): creates horse stats from data set
  - update_horse_stats(self): updates horse speed based on horse stats
  - get_horse_info(self): display horses stats
- track_data.py
  - create_track(length, condition, surface, hurdles, location): sets up the track for racing
  - weather_factors(self, weather_factors): applies random weather to the track (will impact the race)
  - get_track_info(self): display track information
- race_details.py
  - create_jockey(name, age, weight, favoured, horse_name): sets up race jockey data
  - generate_race_id(): race id
  - assign_data(): assigns race date
  - get_info(): displays jockey, race, and date info  
simulation/ #subpackage2  
  - race_simulation.py
    - simulate_race(horses, track): method to start race
    - update_position(self): update horse's position on the track with a visual representation of the race
    - determine_winner(horses): output winner of the race
  - race_results.py
    - generate_race_summary(race, data): outputs race results in detail
    - get_horse_performance(horse): returns performance summary for a specific horse
    - show_leaderboard(leaders): displays a leaderboard for all horses
   - betting.py
     - show_balance(self): shows users current balance
     - take_bet(self, bet, horse_id, horses): user input for bet - if 0 or horse_id invalid, does not accept bets
     - distribute_earnings(self, bet, winning_horse_id, selected_horse_id, odds=2.0): Assesses if selected horse wins race, if wins - adds bet to balance

