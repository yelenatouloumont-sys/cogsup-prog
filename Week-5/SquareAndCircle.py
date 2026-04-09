from expyriment import design, control, stimuli, misc

#Create an experiment object called 'exp'
exp = design.Experiment(name='First Experiment')

#Avoid fullscreen mode and use a small window for development
control.set_develop_mode()

#Initialize the experiment (this creates the window and prepares everything)
control.initialize(exp)

#Define some constants for the experiment
STIMSIZE = 100 #Size of the stimuli in pixels
GREY = misc.constants.C_GREY #A grey color for the stimuli
LATERAL_OFFSET = 300 #Offset for lateral positioning 

#Prepare some stimuli
square = stimuli.Rectangle(size=(STIMSIZE, STIMSIZE), colour = GREY, position=(-LATERAL_OFFSET, 0))
circle = stimuli.Circle(radius = STIMSIZE//2, colour = GREY, position=(LATERAL_OFFSET, 0))

#Preload the stimuli (this can help reduce delays during the experiment)
square.preload()
circle.preload()

#Start the experiment (this will show the window and wait for a key press to start)
control.start()

#Present the square and circle stimuli
square.present(clear = True, update = False)
circle.present(clear = False, update = True)

exp.clock.wait(2000) #Wait for 2s to let the participant see the stimuli

control.end()