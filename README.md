# Horse-Race-Simulator

horse_race_simulator/ # package  
race_data/ #subpacakge1
- horse_stats.py
  - create_horse(name, age, speed, weight, favoured): create horse stats
  - update_horse_stats(horse, performance): update horses overall performance
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
     - show_balance(): shows users current balance
     - take_bet(amount, horse): user input for bet, if 0 does not accept bets
     - subtract_balance(): removes balance after taking a bet
     - winnings(): adds winnings if user's choice wins

