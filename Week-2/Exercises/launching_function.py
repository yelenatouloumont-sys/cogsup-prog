from expyriment import design, control, stimuli
#---------------------------------------------------
# 3E: Launching function
#---------------------------------------------------
def horizontal_launching_event(temporal_gap=0, spatial_gap=0, speed_ratio=1.0):
    """
    Displays a horizontal launching event.

    Parameters:
    temporal_gap (ms): delay between collision and green movement
    spatial_gap (px): distance between squares at collision
    speed_ratio: speed of green relative to red (1 = same speed)
    """
    # 1. Create the squares
    square_red = stimuli.Rectangle(
        size=(50, 50),
        colour=(255, 0, 0),
        position=(-400, 0)
    )
    square_green = stimuli.Rectangle(
        size=(50, 50),
        colour=(0, 255, 0),
        position=(0, 0)
    )
    # Animation parameters
    speed = 5
    frame_duration = 10
    # Contact position (normal contact = -50)
    contact_position = -50 - spatial_gap
    # ----------------------------------------------
    # PHASE 1: Red moves toward green
    # ----------------------------------------------
    while square_red.position[0] < contact_position:
        square_red.move((speed, 0))
        square_red.present(clear=True, update=False)
        square_green.present(clear=False, update=True)
        exp.clock.wait(frame_duration)
    # ----------------------------------------------
    # Temporal gap after contact (if one)
    # ----------------------------------------------
    square_red.present(clear=True, update=False)
    square_green.present(clear=False, update=True)
    exp.clock.wait(temporal_gap)
    # ----------------------------------------------
    # PHASE 2: Green moves
    # ----------------------------------------------
    green_speed = speed * speed_ratio
    push_steps = 80

    for _ in range(push_steps):
        square_green.move((green_speed, 0))
        square_red.present(clear=True, update=False)
        square_green.present(clear=False, update=True)
        exp.clock.wait(frame_duration)
    # Hold final display 1 second
    exp.clock.wait(1000)


# ==================================================
# EXPERIMENT
# ==================================================
exp = design.Experiment(name="Combined Launching Events")
control.initialize(exp)
fixation = stimuli.FixCross()
control.start(subject_id=1)

# Show fixation before each event
def show_fixation():
    fixation.present(clear=True, update=True)
    exp.clock.wait(1000)

# --------------------------------------------------
# TEST 1: Michottean Launching (baseline)
# --------------------------------------------------
show_fixation()
horizontal_launching_event(
    temporal_gap=0,
    spatial_gap=0,
    speed_ratio=1.0
)

# --------------------------------------------------
# TEST 2: Launching with a temporal Gap
# --------------------------------------------------
show_fixation()
horizontal_launching_event(
    temporal_gap=2000,  # delay
    spatial_gap=0,
    speed_ratio=1.0
)

# --------------------------------------------------
# TEST 3: Launching with a spatial Gap
# --------------------------------------------------
show_fixation()
horizontal_launching_event(
    temporal_gap=0,
    spatial_gap=40,  # gap
    speed_ratio=1.0
)

# --------------------------------------------------
# TEST 4: Triggering (green 3 times faster than red)
# --------------------------------------------------
show_fixation()
horizontal_launching_event(
    temporal_gap=0,
    spatial_gap=0,
    speed_ratio=3.0  # green faster than red
)

exp.keyboard.wait()
control.end()