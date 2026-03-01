# Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Two Squares")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a fixation cross (color, size, and position will take on default values)
fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered

# Create the Squares 50x50
offset = 200

square_1 = stimuli.Rectangle(
    size=(50, 50), 
    colour=(255, 0, 0), 
    position=(-offset//2, 0)
    )

square_2 = stimuli.Rectangle(
    size=(50, 50), 
    colour=(0, 255, 0), 
    position=(offset//2, 0)
    )

# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross
fixation.present(clear=True, update=True)

# Leave it on-screen for 1,000 ms
exp.clock.wait(1000)

# Remove the cross and replace it with a square
square_1.present(clear=True, update=False)
square_2.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()
