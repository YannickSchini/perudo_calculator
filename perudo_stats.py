""" This module contains all statistics-related function that I'll need
    for my Perudo calculator. """

import math

PROBA_OF_PACO = 1 / 6
PROBA_OF_NON_PACO_FACE = 1 / 3
# 1/3 = 1/6 (proba of getting a given face) + 1/6 (proba of getting a Paco)


def get_proba_of_given_face(total_num_of_dice: int, num_of_matches: int,
                            paco: bool) -> float:
    """ Function to get the probability of getting the given amount of matches
    of any single face in function of the number of dice.
    This assumes a standard dice and does not take into account the fact that
    the Paco face in the game of Perudo can count for any other face.

    Param:
        - total_num_of_dice: integer number of dice used
        - num_of_matches: integer number of faces matching
        - paco: boolean stating if we care about the Paco face or any other
        face of the Dices

    Returns:
        - the probability of getting this number of matches """
    if paco:
        match_proba = PROBA_OF_PACO
    else:
        match_proba = PROBA_OF_NON_PACO_FACE
    result = match_proba**num_of_matches * (1 - match_proba)**(
        total_num_of_dice - num_of_matches) * math.comb(
            total_num_of_dice, num_of_matches)
    return result
