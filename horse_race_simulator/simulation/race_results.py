# race_results.py - Work-in-progress version

# Here 'data' refers to the dataframe that has the simulated race data
# Here 'hist' refers to the dataframe that has the historical data from 'https://www.kaggle.com/datasets/gdaley/hkracing'

import pandas as pd

class RaceResults(RaceSimulator):

    hist = pd.read_csv('runs.csv')
    track_length = 50

    def __init__(self, race, track):
        RaceSimulator.__init__(self, race, track)
        self.race_id = race.race_id
        self.date = race.date
        self.horses = race.horses
        self.data = pd.DataFrame({})
        self.winning_horse_id = -1

    def getWinningHorseId(self):
        horse_timings = super().get_times()
        self.data = self.get_horse_timing_data_frame(horse_timings)
        return self.winning_horse_id

    def get_horse_timing_data_frame(self, horse_timings):
        min_finish_time_overall = min(horse_timings.items(), key=lambda item: item[1]['Overall Time'])[1]['Overall Time'];
        min_finish_time_first_leg = min(horse_timings.items(), key=lambda item: item[1]['Leg 1 Time'])[1]['Leg 1 Time'];
        min_finish_time_second_leg = min(horse_timings.items(), key=lambda item: item[1]['Leg 2 Time'])[1]['Leg 2 Time'];
        min_finish_time_third_leg = min(horse_timings.items(), key=lambda item: item[1]['Leg 3 Time'])[1]['Leg 3 Time'];
        
        horse_ids = []
        step1_location = []
        step2_location = []
        step3_location = []
        step4_location = []
        final_position = []
        finish_times = []
        for horse_id, timings in horse_timings.items():
            horse_ids.append(horse_id)
            step1_location.append(RaceResults.track_length * 0.25 * (min_finish_time_first_leg/timings['Leg 1 Time']))
            step2_location.append(RaceResults.track_length * 0.5 * (min_finish_time_second_leg/timings['Leg 2 Time']))
            step3_location.append(RaceResults.track_length * 0.75 * (min_finish_time_third_leg/timings['Leg 3 Time']))
            step4_location.append(RaceResults.track_length * (min_finish_time_overall/timings['Overall Time']))
            finish_times.append(timings['Overall Time'])
            final_position.append(self.get_horse_position(horse_timings, horse_id))

        self.winning_horse_id = min(horse_timings, key=lambda horse_id: horse_timings[horse_id]['Overall Time'])

        horse_timing_data_set = {'horse_id': horse_ids, 'steps1': step1_location, 'steps2': step2_location, 'steps3': step3_location, 'steps4': step4_location,'result': final_position, 'finish_time': finish_times}
        return pd.DataFrame(horse_timing_data_set)

    def get_horse_position(self, horse_timings, horse_id):
        sorted_horses = sorted(horse_timings.items(), key=lambda item: item[1]['Overall Time'])
    
        # Find the position of the specified horse
        for position, (current_horse_id, _) in enumerate(sorted_horses, start=1):
            if current_horse_id == horse_id:
                return position
    
        # If the horse_id is not found, return -1
        return -1
      
    def display_options(self):
        horse_timings = super().get_times()
        self.data = self.get_horse_timing_data_frame(horse_timings)
        
        while True:
            results_type = input(
            """
        
            Choose type of results to show:\n
            A: Leaderboard\n 
            B: Overall summary\n 
            C: Compare horse performance\n 
            D: Exit\n
            Enter your response:""")
            if results_type == 'A':
                self.display_leaderboard()
            elif results_type == 'B':
                self.generate_race_summary()
            elif results_type == 'C':
                self.get_horse_performance()
            elif results_type == 'D':
                return None

    def display_leaderboard(self):
        """creates a visual display for the horses and their corresponding performance after the race."""
           
        #Store in dataframe.
        sub_df = self.data[['result','horse_id','finish_time']].copy()
        sub_df = sub_df.sort_values(by='finish_time').copy().reset_index(drop=True)  
        position = sub_df['result']
        horse = sub_df['horse_id']
        finish_time = sub_df['finish_time']
        
        # Display the leaderboard
        print(f"🏇 Horse Race Leaderboard : {self.race_id}🏇")
        print("------------------------------------------------------------")
        print(f"{'Position':<10}{'Horse':<15}{'Time (s)':<10}")
        print("------------------------------------------------------------")
        for i in range(len(self.horses)):
            print(f"{position[i]:<10}{horse[i]:<15}{finish_time[i]:<10}")
    
        # Winner announcement
        print(f"\n🎉 Winner: {horse[0]} with a time of {finish_time[0]/100} seconds! 🎉")

    def generate_race_summary(self):
        """ Display the race summary in detail includes attributes previously defined."""
        
        # Display the Performance results
        print(f"🏇 Race summary : {self.race_id} 🏇")
        print("------------------------------------------------------------")
        
        # Display all race attributes
        print(f" Date : {self.date}")
        print(f" Number of horses : {len(self.horses)}")
        print(f" Finish time of winner: {self.data['finish_time'].min()/100} seconds")
        print(f" Finish time of last horse: {self.data['finish_time'].max()/100} seconds")
         
        # Add visualizations
        
        horses = self.data['horse_id']
        positions = [0]* len(horses) # Starting positions
        
        print("\n🏁 Race Snapshot 🏁")
        print("------------------------------------------------------------")
        # Print race for each stage
        print('\nStage 1:\n')
        # Update positions 
        step1 = self.data['steps1'].astype(int)
        for i in range(len(self.data)):
            positions[i] = step1[i] 
        
        # Display the race track
        for i, horse in enumerate(horses):
            print(f"{horse}: " + "-" * positions[i] + "🐎" + "-" * (RaceResults.track_length - positions[i]))
        
        print('\nStage 2:\n')
        step2 = self.data['steps2'].astype(int)
        for i in range(len(self.data)):
            positions[i] = step2[i]  
        
        # Display the race track
        for i, horse in enumerate(horses):
            print(f"{horse}: " + "-" * positions[i] + "🐎" + "-" * (RaceResults.track_length - positions[i]))
        
        
        print('\nStage 3:\n')
        step3 = self.data['steps3'].astype(int)
        for i in range(len(self.data)):
            positions[i] = step3[i]  
        
        # Display the race track
        for i, horse in enumerate(horses):
            print(f"{horse}: " + "-" * positions[i] + "🐎" + "-" * (RaceResults.track_length - positions[i]))
        
        print('\nStage 4:\n')
        step4 = self.data['steps4'].astype(int)
        for i in range(len(self.data)):
            positions[i] = step4[i]  
        
        # Display the race track
        for i, horse in enumerate(horses):
            print(f"{horse}: " + "-" * positions[i] + "🐎" + "-" * (RaceResults.track_length - positions[i]))
        
    def get_horse_performance(self):
        """ Retrieve performance summary for a specific horse, can be called for every horse in the race """
        sub_df = self.data[['result','horse_id']].copy()
        sub_df = sub_df.sort_values(by='result').copy().reset_index(drop=True)  
        position = sub_df['result']
        horse = sub_df['horse_id']
        
        print(f"🏇 Horse IDs 🏇")
        print("------------------------------------------------------------")
        print(f"{'Position':<10}{'Horse':<15}")
        print("------------------------------------------------------------")
        for i in range(len(self.horses)):
            print(f"{position[i]:<10}{horse[i]:<15}")
            
        horse_id_input = int(input("\nEnter a horse id to compare performance with past results: "))
        if horse_id_input == '':
            return None
        
        # Current race
        finish_time = self.data.loc[self.data['horse_id'] == horse_id_input,'finish_time'].iloc[0]
        rank = self.data.loc[self.data['horse_id'] == horse_id_input,'result'].iloc[0]
            
        # Historical data for comparison
        average_finish_time = RaceResults.hist[RaceResults.hist['horse_id'] == horse_id_input]['finish_time'].mean()
        win_count = RaceResults.hist[(RaceResults.hist['horse_id'] == horse_id_input) & (RaceResults.hist['won'] == 1)]['horse_id'].count()
        average_rank = round(RaceResults.hist[RaceResults.hist['horse_id'] == horse_id_input]['result'].mean())
        number_of_races = RaceResults.hist[RaceResults.hist['horse_id'] == horse_id_input]['race_id'].nunique()
        win_ratio = (win_count/number_of_races)*100
        
        # Display the Performance results
        print(f"🏇 Horse Performance : {horse_id_input} 🏇")
        print("------------------------------------------------------------")

        horse_age = 0
        horse_type = 0
        horse_weight = 0
        horse_jockey = ''
        for horse in self.horses:
            if horse.horse_id == horse_id_input:
                horse_age = horse.horse_age
                horse_type = horse.horse_type
                horse_weight = horse.actual_weight
                horse_jockey = horse.jockey_id
        
        # Display all horse attributes
        print(f" {'Horse age:':<20} {horse_age}")
        print(f" {'Horse type:':<20} {horse_type}")
        print(f" Weight: {horse_weight}")
        print(f" Jockey: {horse_jockey}")
        print(f" Historical Win count: {win_count} of {number_of_races} races [Win ratio of {win_ratio:.2f}%] ")
    
        # Display table
        print("------------------------------------------------------------")
        print(f"{'Metric':<20}{'Current race':<20}{'Past performance':<20}")
        print("------------------------------------------------------------")
        print(f"{'Finish time':<20}{round(finish_time,2):<20}{round(average_finish_time,2):<20}")
        print(f"{'Rank':<20}{rank:<20}{average_rank:<20}")
        
# Test code

if __name__ == "__main__":
    track = TrackData()
    track.create_track()
    track.weather_factor()
    
    race_details = Race(date="2024-12-01", venue=track.track_venue[0], distance=track.track_venue[1], prize=5000, num_horses=5)
    horses = Horse.create_horse("runs.csv", race_details.num_horses)
    race_details.horses = horses
    
    print(race_details.get_race_info())
    
    race = RaceResults(race_details, track) #race, track, horses
    race.start_race()
    turtle.mainloop()
    # print("\nRace Results:")
    # for horse_id, result in race.final_results.items():
    #     print(f"Horse {horse_id}: Position: {result['final_position']}, "
    #           f"Overall Time: {result['overall_time']}s, "
    #           f"Leg Times: {result['leg_times']}")
    print(race.getWinningHorseId())
    race.display_options()
   