# race_results.py - Work-in-progress version

# Here 'data' refers to the dataframe that has the simulated race data
# Here 'hist' refers to the dataframe that has the historical data from 'https://www.kaggle.com/datasets/gdaley/hkracing'

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


