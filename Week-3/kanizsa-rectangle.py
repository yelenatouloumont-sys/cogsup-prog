from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY
control.set_develop_mode()

def KanizsaRectangle(size_percentage=0, radius_percentage=0):
    width, height = exp.screen.size
    square_size = int(width * size_percentage)
    half_square = square_size // 2
    circle_radius = int(width * radius_percentage)
    left = -half_square
    right = half_square
    top = half_square
    bottom = -half_square

    # 1. Create the circles
    circle1 = stimuli.Circle(
        radius = circle_radius, 
        colour=(250, 250, 250), 
        position = (left, bottom))
    circle2 = stimuli.Circle(
        radius = circle_radius, 
        colour=(0, 0, 0), 
        position = (left, top))
    circle3 = stimuli.Circle(
        radius = circle_radius, 
        colour=(255, 255, 255), 
        position = (right, bottom))
    circle4 = stimuli.Circle(
        radius = circle_radius, 
        colour=(0, 0, 0), 
        position = (right, top))
    # 2. Create the rectangle
    rectangle = stimuli.Rectangle(
        size=(square_size, square_size), 
        colour=(C_GREY), 
        position = (0,0))
    circle1.present(clear=True, update=False)
    circle2.present(clear=False, update=False)
    circle3.present(clear=False, update=False)
    circle4.present(clear=False, update=False)
    rectangle.present(clear=False, update=True)
    exp.keyboard.wait()
    control.end()

def show_fixation():
    fixation.present(clear=True, update=True)
    exp.clock.wait(1000)

#---------------------------------------------
# EXPERIMENT
#---------------------------------------------

exp = design.Experiment(name = "Kanizsa", background_colour=C_GREY)
control.initialize(exp)
fixation = stimuli.FixCross()
control.start(subject_id=1)

#---------------------------------------------
# TEST
#---------------------------------------------
show_fixation()
KanizsaRectangle(0.25, 0.05)