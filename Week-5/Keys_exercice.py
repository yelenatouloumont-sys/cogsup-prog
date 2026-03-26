from expyriment import design, control, stimuli

""" Global settings """
exp = design.Experiment(name="Keys_exercice")

control.set_develop_mode()
control.initialize(exp)

text = stimuli.TextLine("Press a key")
text.present()

key = exp.keyboard.wait()

feedback = stimuli.TextLine("You pressed", print(key))
feedback.present()

exp.clock.wait(3000)
control.end()
