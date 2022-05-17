# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:07:06 2022

@author: steph
"""

# This code was used to solve the maze challenge on https://www.reeborg.ca/index_en.html

# Reeborg has a keyboard comprised of the following basic moves
# move(), turn_left(), take(), put(), toss(),
# build_wall(), pause(), done(), think(100),
# sound(True), World(), UsedRobot(), and 
# no_highlight().

# For Day 6 of 100 Days of Python the user
# solves hurdles 1-4 before moving on to the 
# maze challenge.

# Once the maze challenge is begun the coder
# has access to the additonal commands
# front_is_clear(), wall_in_front(),
# right_is_clear(), wall_on_right(), and
# at_goal().

# WIth these commands, while loops, and if/elif/else
# statement the coder is asked to teach the robot
# to solve random mazes.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        elif not wall_on_right():
            if front_is_clear():
                move()
        else:
            turn_left()
    elif right_is_clear():
        turn_right()
        move()
    else:
        if front_is_clear():
            move()
        else:
            turn_right()
