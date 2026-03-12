from expyriment import design, control, stimuli
control.set_develop_mode()
exp = design.Experiment(name = "Edges")
control.initialize(exp)
fixation = stimuli.FixCross()
width, height = exp.screen.size
square_size = int(width * 0.05)
half_square = square_size//2
left = -width // 2 + half_square
right = width // 2 - half_square
bottom = -height // 2 + half_square
top = height // 2 - half_square

rectangle1 = stimuli.Rectangle(
    size=(square_size, square_size), 
    line_width=1, 
    colour=(255, 0, 0), 
    position = (left, bottom)
    )
rectangle2 = stimuli.Rectangle(
    size=(square_size, square_size), 
    line_width=1, 
    colour=(255, 0, 0), 
    position = (left, top)
    )
rectangle3 = stimuli.Rectangle(
    size=(square_size, square_size), 
    line_width=1, colour=(255, 0, 0), 
    position = (right, bottom)
    )
rectangle4 = stimuli.Rectangle(
    size=(square_size, square_size), 
    line_width=1, 
    colour=(255, 0, 0), 
    position = (right, top)
    )

control.start(subject_id=1)
fixation.present(clear=True, update=True)
exp.clock.wait(1000)
rectangle1.present(clear=True, update=False)
rectangle2.present(clear=False, update=False)
rectangle3.present(clear=False, update=False)
rectangle4.present(clear=False, update=True)
exp.keyboard.wait()
control.end()