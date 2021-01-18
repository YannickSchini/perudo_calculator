""" This module contains all statistics-related function that I'll need
    for my Perudo calculator. """

import math


def get_proba_of_given_face(total_num_of_dice: int,
                            num_of_matches: int) -> float:
    """ Function to get the probability of getting the given amount of matches
    of any single face in function of the number of dice.
    Function gotten from http://villemin.gerard.free.fr/Denombre/JeuxDes.htm
    This assumes a standard dice and does not take into account the fact that
    the Paco face in the game of Perudo can count for any other face.

    Param:
        - total_num_of_dice: integer number of dice used
        - num_of_matches: integer number of faces matching

    Returns:
        - the probability of getting this number of matches """
    total_number_of_combinations = 6**total_num_of_dice
    number_of_matching_combinations = float(
        5**(total_num_of_dice - num_of_matches) *
        math.comb(total_num_of_dice, num_of_matches))
    return float(number_of_matching_combinations /
                 total_number_of_combinations)
