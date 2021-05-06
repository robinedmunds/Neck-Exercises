import os
import datetime
from time import sleep

# 1. CHIN TUCKS: 20 reps, 5 second hold, 4 times a day
# 2. SCAPULAR PINCHES: 30 reps, 3 second hold, 2 times a day
# 3. WALL ANGELS: 2 minutes, keep moving, once per day
# https://www.youtube.com/watch?v=q5SsM9PWWYc


class Exercise:
    def __init__(self, desc, reps, hold, rest):
        self.desc = desc
        self.reps = reps
        self.hold = hold  # seconds
        self.rest = rest  # seconds

    def perform(self):
        for i in range(self.reps):
            print(f"Prepare for {self.desc} {i+1} of {self.reps}")
            sleep(self.hold)
            print(f"!!!  {self.desc} {i+1}  !!!")
            sleep(self.hold)


class Routine:
    def __init__(self, exercises=[], prepare_time=15):
        self.exercises = exercises
        self.prepare_time = prepare_time

    def perform(self):
        screen_clear()
        for idx, exercise in enumerate(self.exercises):
            print("------------------------------------------------")
            print(f"Prepare for exercise {idx+1} of {self.exercise_count()}")
            print()
            sleep(self.prepare_time)
            exercise.perform()

    def exercise_count(self):
        return len(self.exercises)


def screen_clear():
    if os.name == "posix":
        _ = os.system("clear")
        return
    _ = os.system("cls")


def main():
    routine = Routine(
        exercises=[
            Exercise(
                desc="SHOULDER LUNGE",
                reps=1,
                hold=30,
                rest=5
            ),
            Exercise(
                desc="SCAPULAR PINCHES",
                reps=25,
                hold=5,
                rest=5
            ),
            Exercise(
                desc="CHIN TUCK",
                reps=20,
                hold=5,
                rest=5
            ),
            Exercise(
                desc="WALL ANGELS",
                reps=1,
                hold=2*60,
                rest=5
            ),
        ],
        prepare_time=15
    )

    routine.perform()


if __name__ == "__main__":
    main()
