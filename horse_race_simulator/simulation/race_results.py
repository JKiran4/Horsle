# race_results.py

import pandas as pd

class InvalidInputError(Exception):
    """Custom exception raised when input is not a valid input."""
    pass

class RaceResults:
    """A class representing the results of the race simulation
    Methods:
        __init__(): Intializes race result information
        get_horse_timing_data_frame(): retrieves the horse times during the race simulation (legs and overall time)
        get_horse_position(): finding the horse's position (used at various stages of the race)
        display_options(): gives users options to select the displaying of race results
        display_leaderboard(): displays a leaderboard of the race results
        generate_race_summary(): displays a detailed summary of the race
        get_horse_performance(): displays performance details for a specific horse
        get_horse_age(): retrieve horse age
        get_horse_type(): retrieve horse type (breed)
        get_horse_weight(): retrieve horse weight
        get_horse_jockey(): retrieve horse jockey (the person riding the horse)
    """
    
    hist = pd.read_csv('runs.csv')
    track_length = 50 # solely for display purposes

    def __init__(self, race, horses, horse_timings):
        """Initializes race results information"""
        self.race_id = race.race_id
        self.date = race.date
        self.horses = horses
        self.data = self.get_horse_timing_data_frame(horse_timings)

    def get_horse_timing_data_frame(self, horse_timings):
        """retrieves a data frame with the horse times across the race simulation
        Parameters:
           self: the race results object
           horse_timings: the dictionary of timing from the race simulation
        Returns:
           data frame: data frame of the horse ids witht their times
        """
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
        poisition = 1;

        for horse_id, timings in horse_timings.items():
            horse_ids.append(horse_id)
            step1_location.append(RaceResults.track_length * 0.25 * (min_finish_time_first_leg/timings['Leg 1 Time']))
            step2_location.append(RaceResults.track_length * 0.5 * (min_finish_time_second_leg/timings['Leg 2 Time']))
            step3_location.append(RaceResults.track_length * 0.75 * (min_finish_time_third_leg/timings['Leg 3 Time']))
            step4_location.append(RaceResults.track_length * (min_finish_time_overall/timings['Overall Time']))
            finish_times.append(timings['Overall Time'])
            final_position.append(self.get_horse_position(horse_timings, horse_id))
            poisition += 1

        horse_timing_data_set = {'horse_id': horse_ids, 'steps1': step1_location, 'steps2': step2_location, 'steps3': step3_location, 'steps4': step4_location,'result': final_position, 'finish_time': finish_times}
        return pd.DataFrame(horse_timing_data_set)

    def get_horse_position(self, horse_timings, horse_id):
        """retrieves a horses position
        Parameters:
           self: the race results object
           horse_timings: the set of horse times from the simulation 
           horse_id: a specific horse id (that was in the race)
        Returns:
           position: the horse's position, or -1 if the horse id is not found
        """

        sorted_horses = sorted(horse_timings.items(), key=lambda item: item[1]['Overall Time'])
    
        # Find the position of the specified horse
        for position, (current_horse_id, _) in enumerate(sorted_horses, start=1):
            if current_horse_id == horse_id:
                return position
    
        # If the horse_id is not found, return -1
        return -1
    
    def display_options(self):
        """retrieves a horses position
        Parameters:
           self: the race results object
        Returns:
           method calls: calls specific methods depending on user input
        """
        while True:
            try:
                results_type = input(
            """
        
If you would like to see an overview of race, please select one of the options below, otherwise select 'D':\n
A: Leaderboard
B: Overall summary
C: Compare horse performance
D: Exit\n
Enter your selection: """)
                if results_type == 'A':
                    self.display_leaderboard()
                elif results_type == 'B':
                    self.generate_race_summary()
                elif results_type == 'C':
                    self.get_horse_performance()
                elif results_type == 'D':
                    return None

                if results_type != 'A' and results_type != 'B' and results_type != 'C' and results_type != 'D':
                    raise InvalidInputError("\nInvalid input! please enter a valid input.")

            except InvalidInputError as e:
                # Handle the case where the invalid horse Id is given
                print(e)

    def display_leaderboard(self):
        """creates a visual display for the horses and their corresponding performance after the race.
        Parameters:
           self: the race results object
        Returns:
           print statements: The overall leaderboard from the race simulation and winner of the race
        """
           
        #Store in dataframe.
        sub_df = self.data[['result','horse_id','finish_time']].copy()
        sub_df = sub_df.sort_values(by='finish_time').copy().reset_index(drop=True)  
        position = sub_df['result']
        horse = sub_df['horse_id']
        finish_time = sub_df['finish_time']
        
        # Display the leaderboard
        print(f"\n🐢 Horse Race Leaderboard : {self.race_id}🐢")
        print("------------------------------------------------------------")
        print(f"{'Position':<10}{'Horse':<15}{'Time (s)':<10}")
        print("------------------------------------------------------------")
        for i in range(len(self.horses)):
            print(f"{position[i]:<10}{horse[i]:<15}{finish_time[i]:<10}")
    
        # Winner announcement
        print(f"\n🎉 Winner: {horse[0]} with a time of {finish_time[0]} seconds! 🎉")

    def generate_race_summary(self):
        """Display the race summary in detail includes attributes previously defined.
        Parameters:
           self: the race results object
        Returns:
           print statements: detailed race summary information
           """
        
        # Display the Performance results
        print(f"\n🐢 Race summary : {self.race_id} 🐢")
        print("------------------------------------------------------------")
        
        # Display all race attributes
        print(f" Date : {self.date}")
        print(f" Number of horses : {len(self.horses)}")
        print(f" Finish time of winner: {self.data['finish_time'].min()} seconds")
        print(f" Finish time of last horse: {self.data['finish_time'].max()} seconds")
         
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
            print(f"{horse}: " + "-" * positions[i] + "🐢" + "-" * (RaceResults.track_length - positions[i]))
        
        print('\nStage 2:\n')
        step2 = self.data['steps2'].astype(int)
        for i in range(len(self.data)):
            positions[i] = step2[i]  
        
        # Display the race track
        for i, horse in enumerate(horses):
            print(f"{horse}: " + "-" * positions[i] + "🐢" + "-" * (RaceResults.track_length - positions[i]))
        
        
        print('\nStage 3:\n')
        step3 = self.data['steps3'].astype(int)
        for i in range(len(self.data)):
            positions[i] = step3[i]  
        
        # Display the race track
        for i, horse in enumerate(horses):
            print(f"{horse}: " + "-" * positions[i] + "🐢" + "-" * (RaceResults.track_length - positions[i]))
        
        print('\nStage 4:\n')
        step4 = self.data['steps4'].astype(int)
        for i in range(len(self.data)):
            positions[i] = step4[i]  
        
        # Display the race track
        for i, horse in enumerate(horses):
            print(f"{horse}: " + "-" * positions[i] + "🐢" + "-" * (RaceResults.track_length - positions[i]))
        
    def get_horse_performance(self):
        """Retrieve performance summary for a specific horse, can be called for every horse in the race 
        Parameters:
           self: the race results object
        Returns:
           print statements: performance summary for a specific horse
        """

        sub_df = self.data[['result','horse_id']].copy()
        sub_df = sub_df.sort_values(by='result').copy().reset_index(drop=True)  
        position = sub_df['result']
        horse = sub_df['horse_id']
        
        print(f"🐢 Horse IDs 🐢")
        print("------------------------------------------------------------")
        print(f"{'Position':<10}{'Horse':<15}")
        print("------------------------------------------------------------")
        for i in range(len(self.horses)):
            print(f"{position[i]:<10}{horse[i]:<15}")

        horse_id_input = -1
        while True:
            try:
                take_input = input("\nEnter a horse id to compare performance with past results or enter to exit: ")
                if take_input == '':
                    return None

                horse_id_input = int(take_input)

                if self.find_horse_by_id(take_input) == None:
                    raise InvalidInputError("\nHorse id not in given list of horse ids.")

                break;
            except ValueError:
                # If the input cannot be converted to an integer, raise a custom exception
                print(f"\nInvalid input! '{take_input}' is not a valid horse id.")
            except InvalidInputError as e:
                # Handle the case where the invalid horse Id is given
                print(e)
        
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
        print(f"🐢 Horse Performance : {horse_id_input} 🐢")
        print("------------------------------------------------------------")
        
        # Display all horse attributes
        print(f" {'Horse age:':<20} {self.get_horse_age(horse_id_input)}")
        print(f" {'Horse type:':<20} {self.get_horse_type(horse_id_input)}")
        print(f" Weight: {self.get_horse_weight(horse_id_input)}")
        print(f" Jockey: {self.get_horse_jockey(horse_id_input)}")
        print(f" Historical Win count: {win_count} of {number_of_races} races [Win ratio of {win_ratio:.2f}%] ")
    
        # Display table
        print("------------------------------------------------------------")
        print(f"{'Metric':<20}{'Current race':<20}{'Past performance':<20}")
        print("------------------------------------------------------------")
        print(f"{'Finish time (sec)':<20}{round(finish_time,5):<20}{round(average_finish_time,5):<20}")
        print(f"{'Rank':<20}{rank:<20}{average_rank:<20}")
        
    # supplementary methods
    def find_horse_by_id(self, horse_id):
        for horse in self.horses:
            if horse.horse_id == horse_id:
                return horse
        return None
    
    def get_horse_age(self, horse_id):
        for horse in self.horses:
            if horse.horse_id == horse_id:
                return horse.horse_age
        return None  # Return None if the horse_id is not found

    def get_horse_type(self, horse_id):
        for horse in self.horses:
            if horse.horse_id == horse_id:
                return horse.horse_type
        return None  # Return None if the horse_id is not found

    def get_horse_weight(self, horse_id):
        for horse in self.horses:
            if horse.horse_id == horse_id:
                return horse.actual_weight
        return None  # Return None if the horse_id is not found

    def get_horse_jockey(self, horse_id):
        for horse in self.horses:
            if horse.horse_id == horse_id:
                return horse.jockey_id
        return None  # Return None if the horse_id is not found
