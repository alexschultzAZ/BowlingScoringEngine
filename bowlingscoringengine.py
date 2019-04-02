#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Calculates the current score of a game of bowling given each roll.

Frame
A frame consists of 2 opportunities to knock down 10 bowling pins with a bowling ball. The 10 pins are
then replaced in an upright position for the next frame.

Strike
If you knock down all 10 pins in the first shot of a frame, you get a strike.
How to score: A strike earns 10 points plus the sum of your next two shots.

Spare
If you knock down all 10 pins using both shots of a frame, you get a spare.
How to score: A spare earns 10 points plus the sum of your next one shot.

Open Frame
If you do not knock down all 10 pins using both shots of your frame (9 or fewer pins knocked down), you
have an open frame.
How to score: An open frame only earns the number of pins knocked down.

The 10th Frame
The 10th frame is a bit different:
If you roll a strike in the first shot of the 10th frame, you get 2 more shots.
If you roll a spare in the first two shots of the 10th frame, you get 1 more shot.
If you leave the 10th frame open after two shots, the game is over and you do not get an additional
shot.
How to Score: The score for the 10th frame is the total number of pins knocked down in the 10th frame.

Description:
As a user, when I provide a list of frame scores I should receive a score so that I can understand if I am
winning.

Acceptance Criteria:
I should have a place to enter a series of frames.
A strike is scored as defined above.
A spare is scored as defined above.
An incomplete game is scored up to the last frame provided.

Author:
Alexander Schultz
alexhschultz@gmail.com
"""

import sys


def calculate_score(rolls, frame=1, score=0):
    """given a list of rolls, calculate the bowling score
    
    Arguments:
        rolls {list} -- list of integers that represent individual scores, list must not have any open frames (as per requirements)
    
    Keyword Arguments:
        frame {int} -- current frame used to recursively calculate score (default: {1})
        score {int} -- running score total (default: {0})
    
    Returns:
        int -- total score calculated
    """
    if not rolls or frame > 10: # base case
        return score
    elif rolls[0] == 10: # strike
        rolls = rolls[1:] # trim off this strike
        if len(rolls) > 0:
            bonus = sum(rolls[0:2]) # add next two frames as strike bonus if they exist
        else:
            bonus = 0
        return calculate_score(rolls, frame + 1, score + bonus + 10) # recursively call calculate_score with the remaining rolls, moving to the next frame, and adding 10 points for strike plus the bonus
    elif len(rolls) == 1: # last roll
        return score + rolls[0]
    elif sum(rolls[0:2]) == 10: # spare
        rolls = rolls[2:] # trim off this spare
        if len(rolls) > 0:
            bonus = rolls[0]
        else:
            bonus = 0
        return calculate_score(rolls, frame + 1, score + bonus + 10) # recursively call calculate_score with the remaining rolls, moving to the next frame, and adding 10 points for spare plus the bonus
    else: # open frame
        score += sum(rolls[0:2]) # simply add the two scores to the score
        return calculate_score(rolls[2:], frame + 1, score) # recursively call calculate_score with the remaining rolls, moving to the next frame


def parse_input(input_string):
    """parses input to list of integers
    
    Arguments:
        input {str} -- input string

    Returns:
        list -- list of integers representing each roll
    """
    input_list = list(''.join(input_string.split())) # split input string into list
    parsed_input = []
    for i in range(len(input_list)):
        if input_list[i] == 'X' or input_list[i] == 'x': # convert strike symbol to 10
            parsed_input.append(10)
        elif input_list[i] == '/': # convert spare symbol to integer
            parsed_input.append(10 - int(input_list[i - 1]))
        elif input_list[i] == '-' and i > 0 and input_list[i - 1] == 'X': # remove spare symbol after X
            continue
        elif input_list[i] == '-': # convert spare symbol to integer
            parsed_input.append(0)
        else:
            parsed_input.append(int(input_list[i])) # convert numbers to integer
    return parsed_input


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for input in sys.argv[1:]:
            print(calculate_score(parse_input(input)))