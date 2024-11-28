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

            if turtle_horse not in self.finished_horses:
                all_horses_finished = False

        if all_horses_finished:
            self.end_race()
        else:
            self.screen.ontimer(self.update_position, 50)

    def start_race(self):
        self.race_setup()
        self.screen.ontimer(self.update_position, 50)

# test
if __name__ == "__main__":
    track = TrackData()
    track.create_track()
    track.weather_factor()

    race_details = Race(date="2024-12-01", venue=track.track_venue[0], distance=track.track_venue[1], prize=5000, num_horses=5)
    horses = Horse.create_horse("runs.csv", race_details.num_horses)
    race_details.horses = horses

    print(race_details.get_race_info())
    print(race_details.display_horses())

    race = RaceSimulator(race_details, track)
    race.start_race()
    turtle.mainloop()
