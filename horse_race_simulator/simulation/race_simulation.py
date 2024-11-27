import random
import turtle

class race_simulator:
    def __init__(self, horses, track):
        self.screen = turtle.Screen()
        self.track = track
        self.horses = horses
        self.horse_objects = []
        self.finish_line = None

    def race_setup(self):
        # Screen setup
        self.screen.title("Horse Race Simulation")
        self.screen.bgcolor("white")
        self.screen.setup(width=800, height=600)

        # Track setup
        track_length = self.track.track_venue[1]
        scale = 0.3
        scaled_length = scale * track_length # scale length to fit window
        self.finish_line = scaled_length / 2  # Set the finish line 

        # Draw track
        track = turtle.Turtle()
        track.penup()
        track.goto(-scaled_length / 2, 150)
        track.pendown()
        track.setheading(0)
        track.forward(scaled_length)

        # Horse setup
        colors = ['chocolate4', 'brown3', 'DarkGoldenrod3', 'black', 'burlywood3']
        y_positions = [-100, -50, 0, 50, 100]

        for i, horse in enumerate(self.horses):
            horse.speed = max(horse.speed, 5)
            turtle_horse = turtle.Turtle()
            turtle_horse.shape("turtle")
            turtle_horse.color(colors[i % len(colors)])
            turtle_horse.penup()
            turtle_horse.goto(-scaled_length / 2, y_positions[i])
            self.horse_objects.append((turtle_horse, horse))
    
    def end_race(self):
        print("Race has finished. The window will close in 2 seconds.")
        self.screen.ontimer(self.screen.bye, 2000)

    def update_position(self):
        race_in_progress = False
        weather_multiplier = self.track.track_weather[1] 

        for turtle_horse, horse in self.horse_objects:
            rand_chance = random.random()
            if rand_chance < 0.05:
                move_distance = 0
            elif rand_chance < 0.20:
                move_distance = (horse.speed * weather_multiplier) * 0.1 
            else:
                move_distance = horse.speed * 0.1

            turtle_horse.forward(move_distance)

            # Check if the horse has crossed the finish line
            if turtle_horse.xcor() >= self.finish_line:
                print(f"Horse {horse.horse_id} wins the race!")
                race_in_progress = True
                break

        if not race_in_progress:
            self.screen.ontimer(self.update_position, 50)  # Continue the race in 50ms
        else:
            self.end_race()  # Race finished, trigger race_complete

    def start_race(self):
        self.race_setup()
        self.screen.ontimer(self.update_position, 50)

# make sure to store into data frame for four time intervals - and average race speed
horses = Horse.create_horse("runs.csv")
track = track_data()
track.create_track()
track.weather_factor()
race = race_simulator(horses, track)
race.start_race()
turtle.mainloop()
