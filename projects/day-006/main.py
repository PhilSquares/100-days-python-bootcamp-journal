# Day 6 — Reeborg Maze Solver
# Uses the right-hand rule algorithm to navigate a maze.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Move to the maze wall first
while front_is_clear():
    move()
    turn_left()


# Navigate the maze until the goal is reached
while not at_goal():

    if right_is_clear():
        turn_right()
        move()

    elif front_is_clear():
        move()

    else:
        turn_left()