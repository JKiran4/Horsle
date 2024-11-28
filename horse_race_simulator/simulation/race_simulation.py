import random
import turtle
import time  # Added for timing functionality

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
        self.start_time = None
        self.race_data = {}  # Store race data for each horse
        self.leg_markers = []  #  legs
        self.final_results = {}  # Dictionary to store final results

    def draw_track(self, scaled_length):
        # Create a track turtle for the main track
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

        # Create a turtle for drawing lanes
        lane_turtle = turtle.Turtle()
        lane_turtle.penup()
        lane_turtle.color("white")
        lane_turtle.speed(0.5)
        
        # Draw lanes for horses
        y_lanes = [-125, -75, -25, 25, 75, 125]
        for y_pos in y_lanes:
            lane_turtle.goto(-scaled_length / 2, y_pos)
            lane_turtle.pendown()
            lane_turtle.forward(scaled_length)
            lane_turtle.penup()
        
        lane_turtle.hideturtle()

        # Draw the finish line
        finish_line_turtle = turtle.Turtle()
        finish_line_turtle.penup()
        finish_line_turtle.goto(self.finish_line, 150)
        finish_line_turtle.setheading(270)
        finish_line_turtle.pendown()
        finish_line_turtle.color("white")
        finish_line_turtle.width(10)
        finish_line_turtle.forward(300)
        finish_line_turtle.hideturtle()

    def race_setup(self):
        # Set up screen
        self.screen.title("Horse Race Simulation")
        self.screen.bgcolor("DarkGreen")
        self.screen.setup(width=800, height=600)

        track_length = self.track.track_venue[1]  # Get distance from track module
        scale = 0.3
        scaled_length = scale * track_length  # Scale length
        self.finish_line = scaled_length / 2  # Set the finish line
        self.leg_markers = [
            -scaled_length / 2 + (scaled_length / 4),  # End of first leg
            -scaled_length / 2 + (scaled_length / 2),  # End of second leg
            -scaled_length / 2 + (3 * scaled_length / 4),  # End of third leg
        ]

        self.draw_track(scaled_length)  # Draw the track and lanes

        # Set up 'horses', fixed right now
        colors = ['chocolate4', 'brown3', 'DarkGoldenrod3', 'black', 'burlywood3']
        y_positions = [-100, -50, 0, 50, 100]

        for i, horse in enumerate(self.horses):
            horse.speed = max(horse.speed, 5)
            turtle_horse = turtle.Turtle()
            turtle_horse.shape("turtle")
            turtle_horse.turtlesize(stretch_wid=2, stretch_len=2)
            turtle_horse.color(colors[i % len(colors)])
            turtle_horse.penup()
            turtle_horse.goto(-scaled_length / 2, y_positions[i])  # Start from left
            self.horse_objects.append((turtle_horse, horse))

            # Initialize horse data in race_data
            self.race_data[horse.horse_id] = {
                "final_position": None,
                "overall_time": None,
                "leg_times": {"First Leg": None, "Second Leg": None, "Third Leg": None},
            }

    def update_position(self):
        if self.start_time is None:
            self.start_time = time.time()

        current_time = time.time()
        elapsed_time = current_time - self.start_time
        weather_multiplier = self.track.track_weather[1]

        for race_horse, horse in self.horse_objects:
            if race_horse not in self.finished_horses:
                rand_chance = random.random()
                if rand_chance < 0.05:
                    move_distance = 0
                elif rand_chance < 0.20:
                    move_distance = (horse.speed * weather_multiplier) * 0.1
                else:
                    move_distance = horse.speed * 0.1

                if move_distance < 0:
                    move_distance = 0

                race_horse.forward(move_distance)

                # Check leg times
                if race_horse.xcor() >= self.leg_markers[0] and not self.race_data[horse.horse_id]["leg_times"]["First Leg"]:
                    self.race_data[horse.horse_id]["leg_times"]["First Leg"] = elapsed_time
                if race_horse.xcor() >= self.leg_markers[1] and not self.race_data[horse.horse_id]["leg_times"]["Second Leg"]:
                    self.race_data[horse.horse_id]["leg_times"]["Second Leg"] = elapsed_time
                if race_horse.xcor() >= self.leg_markers[2] and not self.race_data[horse.horse_id]["leg_times"]["Third Leg"]:
                    self.race_data[horse.horse_id]["leg_times"]["Third Leg"] = elapsed_time

                # Finish line crossing
                if race_horse.xcor() >= self.finish_line:
                    if race_horse not in self.finished_horses:
                        position = len(self.finished_horses) + 1
                        self.finished_horses.append(race_horse)
                        self.race_data[horse.horse_id]["final_position"] = position
                        self.race_data[horse.horse_id]["overall_time"] = elapsed_time
                        self.final_results[horse.horse_id] = {
                            "final_position": position,
                            "overall_time": round(elapsed_time, 2),
                            "leg_times": {leg: round(time, 2) for leg, time in self.race_data[horse.horse_id]["leg_times"].items()}
                        }
                        print(f"Horse {horse.horse_id} has crossed the finish line!")

        if len(self.finished_horses) == len(self.horse_objects):
            self.screen.ontimer(self.screen.bye, 1000)  # Close the window after the race is done

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
    print("\nRace Results:")
    for horse_id, result in race.final_results.items():
        print(f"Horse {horse_id}: Position: {result['final_position']}, "
              f"Overall Time: {result['overall_time']}s, "
              f"Leg Times: {result['leg_times']}")
