from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY
control.set_develop_mode()
exp = design.Experiment(name = "Kanizsa", background_colour=C_GREY)
control.initialize(exp)
fixation = stimuli.FixCross()
width, height = exp.screen.size
square_size = int(width * 0.25)
half_square = square_size // 2
circle_radius = int(width * 0.05)
left = -half_square
right = half_square
top = half_square
bottom = -half_square

circle1 = stimuli.Circle(radius = circle_radius, colour=(250, 250, 250), position = (left, bottom))
circle2 = stimuli.Circle(radius = circle_radius, colour=(0, 0, 0), position = (left, top))
circle3 = stimuli.Circle(radius = circle_radius, colour=(255, 255, 255), position = (right, bottom))
circle4 = stimuli.Circle(radius = circle_radius, colour=(0, 0, 0), position = (right, top))
rectangle = stimuli.Rectangle(size=(square_size, square_size), colour=(C_GREY), position = (0,0))

control.start(subject_id=1)
fixation.present(clear=True, update=True)
exp.clock.wait(1000)
circle1.present(clear=True, update=False)
circle2.present(clear=False, update=False)
circle3.present(clear=False, update=False)
circle4.present(clear=False, update=False)
rectangle.present(clear=False, update=True)
exp.keyboard.wait()
control.end()