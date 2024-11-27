# race_results.py - Work-in-progress version

# Here 'data' refers to the dataframe that has the simulated race data
# Here 'hist' refers to the dataframe that has the historical data from 'https://www.kaggle.com/datasets/gdaley/hkracing'

<<<<<<< HEAD
''' Updating RaceSimulator class to include a get_times method

import random
import turtle
from race_details import Race
from track_data import TrackData
from horse_stats import Horse

class RaceSimulator:
    def __init__(self, race, track):
        self.screen = turtle.Screen()
        self.track = track
        self.horses = race.horses
        self.horse_objects = []
        self.finish_line = None
        self.finished_horses = []
        self.finish_times = {}
        self.timer = 0.0

    def race_setup(self):
        self.screen.title("Horse Race Simulation")
        self.screen.bgcolor("DarkGreen")
        self.screen.setup(width=800, height=600)

        track_length = self.track.track_venue[1]  # Get distance from track module
        scale = 0.3
        scaled_length = scale * track_length  # Scale length to fit window
        self.finish_line = scaled_length / 2  # Set the finish line

        track = turtle.Turtle()
        track.penup()
        track.goto(-scaled_length / 2, 150)
        track.pendown()
        track.setheading(0)
        track.forward(scaled_length)

        track.penup()
        track.goto(-scaled_length / 2, -150)
        track.pendown()
        track.setheading(0)
        track.forward(scaled_length)
        track.hideturtle()

        finish_line_turtle = turtle.Turtle()
        finish_line_turtle.penup()
        finish_line_turtle.goto(self.finish_line, 150)
        finish_line_turtle.setheading(270)
        finish_line_turtle.pendown()
        finish_line_turtle.color("white")
        finish_line_turtle.width(10)
        finish_line_turtle.forward(300)
        finish_line_turtle.hideturtle()

        colors = ['chocolate4', 'brown3', 'DarkGoldenrod3', 'black', 'burlywood3']
        y_positions = [-100, -50, 0, 50, 100]

        for i, horse in enumerate(self.horses):
            horse.speed = max(horse.speed, 5)
            turtle_horse = turtle.Turtle()
            turtle_horse.shape("turtle")
            turtle_horse.color(colors[i % len(colors)])
            turtle_horse.penup()
            turtle_horse.goto(-scaled_length / 2, y_positions[i])  # Start from left
            self.horse_objects.append((turtle_horse, horse))

    def end_race(self):
        print("All horses have crossed the finish line.")
        self.screen.ontimer(self.screen.bye, 1000)

    def update_position(self):
        all_horses_finished = True
        weather_multiplier = self.track.track_weather[1]
        self.timer += 50

        for turtle_horse, horse in self.horse_objects:
            if turtle_horse not in self.finished_horses:
                rand_chance = random.random()
                if rand_chance < 0.05:
                    move_distance = 0
                elif rand_chance < 0.20:
                    move_distance = (horse.speed * weather_multiplier) * 0.1
                else:
                    move_distance = horse.speed * 0.1

                if move_distance < 0:
                    move_distance = 0

                turtle_horse.forward(move_distance)

                if turtle_horse.xcor() >= self.finish_line and turtle_horse not in self.finished_horses:
                    print(f"Horse {horse.horse_id} has crossed the finish line!")
                    self.finished_horses.append(turtle_horse)
                    self.finish_times[horse.horse_id] = self.timer

            if turtle_horse not in self.finished_horses:
                all_horses_finished = False

        if all_horses_finished:
            self.end_race()
        else:
            self.screen.ontimer(self.update_position, 50)

    def start_race(self):
        self.race_setup()
        self.screen.ontimer(self.update_position, 50)

    def get_times(self):
        print(self.finish_times)
        return self.finish_times
       

'''

import pandas as pd

class RaceResults(RaceSimulator):

    def __init__(self, race, track):
        RaceSimulator.__init__(self, race, track)
        self.race_id = race.race_id
        self.data = race.date
        self.results_type = ''
        self.data = RaceSimulator.get_times(self) # retreive a dictionary of {horse id : finish times}

    hist = pd.read_excel('runs.xlsx')
    
    #convert dictionary to dataframe
    
    horse_id = []
    finish_time = []
    for key,value in self.data.items():
        horse_id.append(key)
        finish_time.append(value)

    data_set = {'horse_id': horse_id, 'finish_time': finish_time}
    data = pd.DataFrame(data_set)
      
    def user_interface(self):
        self.results_type = input(
        """Choose type of results to show:\n
        A: Leaderboard\n 
        B: Overall summary\n 
        C: Horse performance\n 
        Enter your response:""")
        if self.results_type == 'A':
            display_leaderboard(self)
        elif self.results_type == 'B':
            generate_race_summary(self,hist)
        elif self.results_type == 'C':
            return None
           # horse_id_input = int(input("Enter horse id to view results: "))
           # get_horse_performance(self, hist, horse_id_input)

    def generate_race_summary(self,data):
        """ Display the race summary in detail includes attributes previously defined."""
        
        # Display the Performance results
        print(f"🏇 Race summary : {self.race_id} 🏇")
        print("------------------------------------------------------------")
        
        # Display all race attributes
        print(f" Date : {self.date}")
        
        print(f" Number of horses : {len(self.finish_times)}")
        
        print(f" Finish time of winner: {data['finish_time'].max()} seconds")
        print(f" Finish time of last horse: {data['finish_time'].min()} seconds")
    
         
        # Add visualizations (static and dynamic???)
        
        track_length = 101
        horses = data['horse_id']
        positions = [0]* len(horses) # Starting positions
        
        print("\n🏁 Race Snapshot 🏁")
        print("------------------------------------------------------------")
        # Print race for each stage
        print('\nStage 1:\n')
        # Update positions 
        step1 = data['steps1'].astype(int)
        for i in range(len(data)):
            positions[i] += step1[i] 
        
        # Display the race track
        for i, horse in enumerate(horses):
            print(f"{horse}: " + "-" * positions[i] + "🐎" + "-" * (track_length - positions[i]))
        
        print('\nStage 2:\n')
        step2 = data['steps2'].astype(int)
        for i in range(len(data)):
            positions[i] += step2[i]  
        
        # Display the race track
        for i, horse in enumerate(horses):
            print(f"{horse}: " + "-" * positions[i] + "🐎" + "-" * (track_length - positions[i]))
        
        
        print('\nStage 3:\n')
        step3 = data['steps3'].astype(int)
        for i in range(len(data)):
            positions[i] += step3[i]  
        
        # Display the race track
        for i, horse in enumerate(horses):
            print(f"{horse}: " + "-" * positions[i] + "🐎" + "-" * (track_length - positions[i]))
        
        print('\nStage 4:\n')
        step4 = data['steps4'].astype(int)
        for i in range(len(data)):
            positions[i] += step4[i]  
        
        # Display the race track
        for i, horse in enumerate(horses):
            print(f"{horse}: " + "-" * positions[i] + "🐎" + "-" * (track_length - positions[i]))
        
    def get_horse_performance(self, data, hist):
        """ Retrieve performance summary for a specific horse, can be called for every horse in the race """
        
        horse_id_input = int(input("Enter horse id to view results: "))
        
        # Current race
        finish_time = data.loc[data['horse_id'] == horse_id,'finish_time'].iloc[0]
        rating = data.loc[data['horse_id'] == horse_id,'horse_rating'].iloc[0]
        rank = data.loc[data['horse_id'] == horse_id,'result'].iloc[0]
        win_odds = data.loc[data['horse_id'] == horse_id,'win_odds'].iloc[0]
            
        # Historical data for comparison
        average_finish_time = hist[hist['horse_id'] == horse_id]['finish_time'].mean()
        average_rating = hist[hist['horse_id'] == horse_id]['horse_rating'].mean()
        average_win_odds = hist[hist['horse_id'] == horse_id]['win_odds'].mean()
        win_count = hist[(hist['horse_id'] == horse_id) & (hist['won'] == 1)]['horse_id'].count()
        average_rank = round(hist[hist['horse_id'] == horse_id]['result'].mean())
        number_of_races = hist[hist['horse_id'] == horse_id]['race_id'].nunique()
        win_ratio = (win_count/number_of_races)*100
        
        # Display the Performance results
        print(f"🏇 Horse Performance : {horse_id} 🏇")
        print("------------------------------------------------------------")
        
        # Display all horse attributes
        print(f" {'Horse age:':<20} {data.loc[data['horse_id'] == horse_id,'horse_age'].iloc[0]}")
        print(f" {'Horse country:':<20} {data.loc[data['horse_id'] == horse_id,'horse_country'].iloc[0]}")
        print(f" {'Horse type:':<20} {data.loc[data['horse_id'] == horse_id,'horse_type'].iloc[0]}")
        print(f" Weight: {data.loc[data['horse_id'] == horse_id,'actual_weight'].iloc[0]}")
        print(f" Jockey: {data.loc[data['horse_id'] == horse_id,'jockey_id'].iloc[0]}")
        print(f" Historical Win count: {win_count} of {number_of_races} races [Win ratio of {win_ratio:.2f}%] ")
    
        # Display table
        print("------------------------------------------------------------")
        print(f"{'Metric':<20}{'Current race':<20}{'Past performance':<20}")
        print("------------------------------------------------------------")
        print(f"{'Finish time':<20}{round(finish_time,2):<20}{round(average_finish_time,2):<20}")
        print(f"{'Rank':<20}{rank:<20}{average_rank:<20}")
        print(f"{'Rating':<20}{rating:<20}{round(average_rating):<20}")
        print(f"{'Win Odds':<20}{round(win_odds,2):<20}{round(average_win_odds,2):<20}")
        
    def display_leaderboard(self, data):
        """creates a visual display for the horses and their corresponding performance after the race."""
           
        #Store in dictionary or dataframe.
        sub_df = data[['result','horse_id','finish_time']].copy()
        sub_df = sub_df.sort_values(by='finish_time').copy().reset_index(drop=True)  
        position = sub_df['result']
        horse = sub_df['horse_id']
        finish_time = sub_df['finish_time']
        
        # Display the leaderboard
        print(f"🏇 Horse Race Leaderboard : {race_id}🏇") # add date/time
        print("------------------------------------------------------------")
        
        print(f"{'Position':<10}{'Horse':<15}{'Time (s)':<10}")
        print("------------------------------------------------------------")
        for i in range(14):
            print(f"{position[i]:<10}{horse[i]:<15}{finish_time[i]:<10}")
    
        # Winner announcement
        print(f"\n🎉 Winner: {horse[0]} with a time of {finish_time[0]} seconds! 🎉")
        
# Test code

if __name__ == "__main__":
    track = TrackData()
    track.create_track()
    track.weather_factor()

    race_details = Race(date="2024-12-01", venue=track.track_venue[0], distance=track.track_venue[1], prize=5000, num_horses=5)
    horses = Horse.create_horse("runs.csv", race_details.num_horses)
    race_details.horses = horses

    print(race_details.get_race_info())
    print(horses.display_horses())
    race = RaceResults(race_details, track)
    race.start_race()
    turtle.mainloop()
    race.get_times()
    race.user_interface()
   
=======
def generate_race_summary(data, race_id):
    """ Display the race summary in detail."""
    
    # Display the Performance results
    print(f"🏇 Race summary : {race_id} 🏇")
    print("------------------------------------------------------------")
    
    # Display all race attributes
    print(f" Date : {None}")
    print(f" Number of horses : {data['horse_id'].count()}")
    print(f" Finish time of winner: {data['finish_time'].max()} seconds")
    print(f" Finish time of last horse: {data['finish_time'].min()} seconds")

    # Race snapshot    
    track_length = 101
    horses = data['horse_id']
    positions = [0]* len(horses) # Starting positions
    
    print("\n🏁 Race Snapshot 🏁")
    print("------------------------------------------------------------")
    # Print race for each stage
    
    print('\nStage 1:\n')
    # Update positions 
    step1 = data['steps1'].astype(int)
    for i in range(len(data)):
        positions[i] += step1[i] 
    
    # Display the race track
    for i, horse in enumerate(horses):
        print(f"{horse}: " + "-" * positions[i] + "🐎" + "-" * (track_length - positions[i]))
    
    print('\nStage 2:\n')
    step2 = data['steps2'].astype(int)
    for i in range(len(data)):
        positions[i] += step2[i]  
    
    # Display the race track
    for i, horse in enumerate(horses):
        print(f"{horse}: " + "-" * positions[i] + "🐎" + "-" * (track_length - positions[i]))
    
    print('\nStage 3:\n')
    step3 = data['steps3'].astype(int)
    for i in range(len(data)):
        positions[i] += step3[i]  
    
    # Display the race track
    for i, horse in enumerate(horses):
        print(f"{horse}: " + "-" * positions[i] + "🐎" + "-" * (track_length - positions[i]))
    
    print('\nStage 4:\n')
    step4 = data['steps4'].astype(int)
    for i in range(len(data)):
        positions[i] += step4[i]  
    
    # Display the race track
    for i, horse in enumerate(horses):
        print(f"{horse}: " + "-" * positions[i] + "🐎" + "-" * (track_length - positions[i]))


def get_horse_performance(data, hist, horse_id):
    """ Retrieve performance summary for a specific horse. """

    # Current race
    finish_time = data.loc[data['horse_id'] == horse_id,'finish_time'].iloc[0]
    rating = data.loc[data['horse_id'] == horse_id,'horse_rating'].iloc[0]
    rank = data.loc[data['horse_id'] == horse_id,'result'].iloc[0]
    win_odds = data.loc[data['horse_id'] == horse_id,'win_odds'].iloc[0]
        
    # Historical data for comparison
    average_finish_time = hist[hist['horse_id'] == horse_id]['finish_time'].mean()
    average_rating = hist[hist['horse_id'] == horse_id]['horse_rating'].mean()
    average_win_odds = hist[hist['horse_id'] == horse_id]['win_odds'].mean()
    win_count = hist[(hist['horse_id'] == horse_id) & (hist['won'] == 1)]['horse_id'].count()
    average_rank = round(hist[hist['horse_id'] == horse_id]['result'].mean())
    number_of_races = hist[hist['horse_id'] == horse_id]['race_id'].nunique()
    win_ratio = (win_count/number_of_races)*100
        
    # Display the Performance results
    print(f"🏇 Horse Performance : {horse_id} 🏇")
    print("------------------------------------------------------------")
    
    # Display all horse attributes
    print(f" {'Horse age:':<20} {data.loc[data['horse_id'] == horse_id,'horse_age'].iloc[0]}")
    print(f" {'Horse country:':<20} {data.loc[data['horse_id'] == horse_id,'horse_country'].iloc[0]}")
    print(f" {'Horse type:':<20} {data.loc[data['horse_id'] == horse_id,'horse_type'].iloc[0]}")
    print(f" Weight: {data.loc[data['horse_id'] == horse_id,'actual_weight'].iloc[0]}")
    print(f" Jockey: {data.loc[data['horse_id'] == horse_id,'jockey_id'].iloc[0]}")
    print(f" Historical Win count: {win_count} of {number_of_races} races [Win ratio of {win_ratio:.2f}%] ")

    # Display table
    print("------------------------------------------------------------")
    print(f"{'Metric':<20}{'\Current race':<20}{'Past performance':<20}")
    print("------------------------------------------------------------")
    print(f"{'Finish time':<20}{round(finish_time,2):<20}{round(average_finish_time,2):<20}")
    print(f"{'Rank':<20}{rank:<20}{average_rank:<20}")
    print(f"{'Rating':<20}{rating:<20}{round(average_rating):<20}")
    print(f"{'Win Odds':<20}{round(win_odds,2):<20}{round(average_win_odds,2):<20}")


def display_leaderboard(data, race_id):
    """Displays a leaderboard."""
    # Access simulation resutlts from using update_positions or determine_standings

    #Store in dictionary or dataframe.
    sub_df = data[['result','horse_id','finish_time']].copy()
    sub_df = sub_df.sort_values(by='finish_time').copy().reset_index(drop=True)  
    position = sub_df['result']
    horse = sub_df['horse_id']
    finish_time = sub_df['finish_time']
    
    # Display the leaderboard
    print(f"🏇 Horse Race Leaderboard : {race_id}🏇") # add date/time
    print("------------------------------------------------------------")
    
    print(f"{'Position':<10}{'Horse':<15}{'Time (s)':<10}")
    print("------------------------------------------------------------")
    for i in range(14):
        print(f"{position[i]:<10}{horse[i]:<15}{finish_time[i]:<10}")

    # Winner announcement
    print(f"\n🎉 Winner: {horse[0]} with a time of {finish_time[0]} seconds! 🎉")


# Test code

# take user input to show desired output
results_type = input(
    """Choose type of results to show:\n
    A: Leaderboard\n 
    B: Overall summary\n 
    C: Horse performance\n 
    Enter your response:""")

race_id = 0 # test case retreived from kaggle data set
horse_id = 2170

if results_type == 'A':
    display_leaderboard(data, race_id)
elif results_type == 'B':
    generate_race_summary(data, race_id)
elif results_type == 'C':
    horse_id_input = int(input("Enter horse id to view results: "))
    get_horse_performance(data, hist, horse_id_input)


>>>>>>> 8d60ecc (Adding race_details.py and race_results.py modules - WIP)
