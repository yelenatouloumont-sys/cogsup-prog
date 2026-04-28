from expyriment import design, control, misc, stimuli
import random

exp = design.Experiment(name="Text Experiment")
control.set_develop_mode()
control.initialize(exp)

STIMSIZE = 100 #Size of the stimuli in pixels
GREY = misc.constants.C_GREY #A grey color for the stimuli
LATERAL_OFFSET = 300 #Offset for lateral positioning 

# CSV FILE CULUMNS NAMES -------------------------------------------------------------------------------------------------------
exp.data_variable_names = ["block_name", "trial_id", "target_location","key_pressed", "rt_ms"]

# BLOCK 1: DETERMINISTIC -------------------------------------------------------------------------------------------------------
block_one = design.Block(name="Deterministic")

## TRIAL 1 : square LEFT, circle RIGHT
trial_one = design.Trial()
trial1_text = stimuli.TextLine(text= "TRIAL 1 - DETERMINISTIC")

rectangle_one = stimuli.Rectangle(size=(STIMSIZE, STIMSIZE), colour = GREY, position=(-LATERAL_OFFSET, 0))
circle_one = stimuli.Circle(radius = STIMSIZE//2, colour = GREY, position=(LATERAL_OFFSET, 0))

trial1_text.preload()
rectangle_one.preload()
circle_one.preload()

trial_one.add_stimulus(trial1_text)
trial_one.add_stimulus(rectangle_one)
trial_one.add_stimulus(circle_one)

trial_one.set_factor("square_side", "left")   #square is the target (but we can put circle also)

block_one.add_trial(trial_one)

## TRIAL 2 : square RIGHT, circle LEFT
trial_two = design.Trial()
trial2_text = stimuli.TextLine(text= "TRIAL 2 - DETERMINISTIC")

rectangle_two = stimuli.Rectangle(size=(STIMSIZE, STIMSIZE), colour = GREY, position=(LATERAL_OFFSET, 0))
circle_two = stimuli.Circle(radius = STIMSIZE//2, colour = GREY, position=(-LATERAL_OFFSET, 0))

trial2_text.preload()
rectangle_two.preload()
circle_two.preload()

trial_two.add_stimulus(trial2_text)
trial_two.add_stimulus(rectangle_two)
trial_two.add_stimulus(circle_two)

trial_two.set_factor("square_side", "right")   #square is the target (but we can put circle also)

block_one.add_trial(trial_two)

exp.add_block(block_one)

# BLOCK 2 : STOCHASTIC ------------------------------------------------------------------------------------------------------------------
block_two = design.Block(name="Stochastic")

## Trials are put randomly
for i in range(4):
    trials = design.Trial()

    square_x = random.choice([-LATERAL_OFFSET, LATERAL_OFFSET]) # randomize position
    circle_x  = LATERAL_OFFSET if square_x == -LATERAL_OFFSET else -LATERAL_OFFSET # set as other position
    
    stoch_text = stimuli.TextLine(text=f"TRIAL {i+1} - STOCHASTIC")
    rectangle = stimuli.Rectangle(size=(STIMSIZE, STIMSIZE), colour=GREY, position=(square_x, 0))
    circle = stimuli.Circle(radius=STIMSIZE // 2, colour=GREY, position=(circle_x, 0))

    stoch_text.preload()
    rectangle.preload()
    circle.preload()

    trials.add_stimulus(stoch_text)
    trials.add_stimulus(rectangle)
    trials.add_stimulus(circle)

    trials.set_factor("square_side", "left" if square_x < 0 else "right")
    trials.set_factor("circle_side", "left" if circle_x < 0 else "right")

    block_two.add_trial(trials)

exp.add_block(block_two)

# START THE EXPERIMENT ------------------------------------------------------------------------------------------------------

control.start()

for block in exp.blocks:
    for trial in block.trials:

        trial.stimuli[0].present()
        exp.clock.wait(1000)

        trial.stimuli[1].present(clear=True,  update=False)
        trial.stimuli[2].present(clear=False, update=True)

        #To wait for keypress
        key, rt = exp.keyboard.wait([misc.constants.K_LEFT, misc.constants.K_RIGHT])

        #Decode values for the CSV
        target_location = trial.get_factor("square_side")  # where the square was
        key_pressed = "left" if key == misc.constants.K_LEFT else "right"

        exp.data.add([block.name, trial.id, target_location, key_pressed, rt,])

        stimuli.BlankScreen().present()
        exp.clock.wait(500)

control.end()