from expyriment import design, control, stimuli
exp = design.Experiment(name="Experiment")
control.set_develop_mode()
control.initialize(exp)

#Pass in a list of string variable names: this will give the names of your colums
exp.add_data_vriable_names(["X", "Y", "Z", ...])

#At the end of your run_trial function, store any data you want in exp.data
exp.data.add([x, y, z, ...]) #Can be condition, reaction times, response, anything!

""" Global settings """
exp = design.Experiment(name="Keys_exercice")
control.set_develop_mode()
control.initialize(exp)
# we should put and define our variables here if we have some
""" Experiment """
control.start(exp)
text = stimuli.TextLine("Press a key")
text.present()
key = exp.keyboard.wait()
# feedback = stimuli.TextLine("You pressed", print(key))
feedback = stimuli.TextLine("You pressed " + chr(key[0]))
print(key)
print(chr(key[0]))
print(type(chr(key[0])))
feedback.present()
exp.clock.wait(3000)
control.end()
