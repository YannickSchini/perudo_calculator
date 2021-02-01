""" This module contains all statistics-related function that I'll need
    for my Perudo calculator. """

import math

PROBA_OF_PACO = 1 / 6
PROBA_OF_NON_PACO_FACE = 1 / 3
# 1/3 = 1/6 (proba of getting a given face) + 1/6 (proba of getting a Paco)


def get_proba_of_given_face(total_dice_num: int, total_match_num: int,
                            paco: bool) -> float:
    """ Function to get the probability of getting the given amount of matches
    of any single face in function of the number of dice.
    This assumes a standard dice and does not take into account the fact that
    the Paco face in the game of Perudo can count for any other face.

    Param:
        - total_dice_num: integer number of dice used
        - total_match_num: integer number of faces matching
        - paco: boolean stating if we care about the Paco face or any other
        face of the Dices

    Returns:
        - the probability of getting this number of matches """
    if paco:
        match_proba = PROBA_OF_PACO
    else:
        match_proba = PROBA_OF_NON_PACO_FACE

    result = match_proba**total_match_num * (
        1 - match_proba)**(total_dice_num - total_match_num) * math.comb(
            total_dice_num, total_match_num)

    return result


def get_posterior_proba(total_dice_num: int, total_match_num: int,
                        own_dice_num: int, own_match_num: int,
                        paco: bool) -> float:
    """ Function to get the posterior probability, this means the probability of
    getting X matches in total in all the dices knowing you have Y matches in
    your Z dices.

    I'm using Bayes' Theorem for that:

                        P(B|A) * P(A)
            P(A|B) =  ----------------
                             P(B)

    Applied to our case, we get:
        - P(A|B) is the probability of getting X matchs in total knowing we
          have Y matches in our Z dices
        - P(A) is the probability of getting X matches in all dices
        - P(B) is the probability of getting Y matches in our Z dices
        - P(B|A) is the probability of getting Y matches in our Z dices knowing
          there are X matches in all the dices.

    The first term is the one we're looking for.
    The second and third terms, we can calculate using get_proba_of_given_face
    The last term, we calculate using the following function:
    P(getting Y matches in Z dices | there are X matches in W total dices) =

        math.comb(Y, Z) * math.comb(W-Y, X-Y)
        -------------------------------------
                    math.comb(W, X)

    Parameters:
        - total_dice_num: total amount of dices (W)
        - total_match_num: total amount of matches (X)
        - own_dice_num: one's amount of matches (Y)
        - own_match_num: one's amount of dices (Z)
        - paco: if we consider Paco or non Paco faces (bool)

    """
    if paco:
        match_proba = PROBA_OF_PACO
    else:
        match_proba = PROBA_OF_NON_PACO_FACE

    other_dice_num = total_dice_num - own_dice_num
    other_match_num = total_match_num - own_match_num
    other_non_match_num = other_dice_num - other_match_num

    result = match_proba**other_dice_num * (
        1 - match_proba)**other_non_match_num * math.comb(
            other_dice_num, other_non_match_num)

    return result
