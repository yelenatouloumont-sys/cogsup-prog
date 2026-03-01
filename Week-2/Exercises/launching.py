#------------------------------------------------------------------------------
# 3A: Michottean launching
#------------------------------------------------------------------------------
from expyriment import design, control, stimuli

exp = design.Experiment(name = "Two Squares")
control.initialize(exp)
fixation = stimuli.FixCross()

square_1 = stimuli.Rectangle(
    size=(50, 50), 
    colour=(255, 0, 0), 
    position=(-400, 0) #400 pixels on the left
    )
square_2 = stimuli.Rectangle(
    size=(50, 50), 
    colour=(0, 255, 0), 
    position=(0, 0) #In the center
    )

control.start(subject_id=1)
fixation.present(clear=True, update=True)
exp.clock.wait(1000)

# Animation parameters
speed = 5
frame_duration = 10

# PHASE 1: Move RED square (square_1) toward GREEN square (square_2)
while square_1.position[0] < -50:
    square_1.move((speed, 0))
    square_1.present(clear=True, update=False)
    square_2.present(clear=False, update=True)
    exp.clock.wait(frame_duration)

# PHASE 2: Once red reaches green, move GREEN square to the right --> Same speed and same number of steps
push_steps = 80  # adjust to match video timing

for i in range(push_steps):
    square_2.move((speed, 0))
    square_1.present(clear=True, update=False)
    square_2.present(clear=False, update=True)
    exp.clock.wait(frame_duration)

# Show final position for 1 second
exp.clock.wait(1000)

exp.keyboard.wait()
control.end()

