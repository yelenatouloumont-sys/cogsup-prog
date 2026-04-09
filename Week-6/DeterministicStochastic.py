from expyriment import design, control, misc, stimuli

exp = design.Experiment(name="Text Experiment")
control.set_develop_mode()
control.initialize(exp)

block_one = design.Block(name="Deterministic")
# TRIAL 1
trial_one = design.Trial()

STIMSIZE = 100 #Size of the stimuli in pixels
GREY = misc.constants.C_GREY #A grey color for the stimuli
LATERAL_OFFSET = 300 #Offset for lateral positioning 

square = stimuli.Rectangle(size=(STIMSIZE, STIMSIZE), colour = GREY, position=(-LATERAL_OFFSET, 0))
circle = stimuli.Circle(radius = STIMSIZE//2, colour = GREY, position=(LATERAL_OFFSET, 0))

#Preload the stimuli (this can help reduce delays during the experiment)
square.preload()
circle.preload()

trial_one.add_stimulus(square)
trial_one.add_stimulus(circle)

exp.clock.wait(2000) #Wait for 2s to let the participant see the stimuli

# TRIAL 2
trial_two = design.Trial()
stim = stimuli.TextLine(text="I am a stimulus in Block 1, Trial 2")
trial_two.add_stimulus(stim)
block_one.add_trial(trial_one)
block_one.add_trial(trial_two)
exp.add_block(block_one)

block_two = design.Block(name="Stochastic")
trial_one = design.Trial()
stim = stimuli.TextLine(text="I am a stimulus in Block 2, Trial 1")
stim.preload()
trial_one.add_stimulus(stim)
trial_two = design.Trial()
stim = stimuli.TextLine(text="I am a stimulus in Block 2, Trial 2")
trial_two.add_stimulus(stim)
block_two.add_trial(trial_one)
block_two.add_trial(trial_two)
exp.add_block(block_two)

control.start()

for block in exp.blocks:
    for trial in block.trials:
        trial.stimuli[0].present()
        key, rt = exp.keyboard.wait([misc.constants.K_LEFT,
                                     misc.constants.K_RIGHT])
        exp.data.add([block.name, trial.id, key, rt])

control.end()