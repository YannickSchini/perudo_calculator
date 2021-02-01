""" Test module for the statistics calculations """

import unittest
import perudo_stats


class TestStatistics(unittest.TestCase):
    """ Test class for the computation done in the statistics module """
    def test_get_proba_of_paco_face_with_first_values(self) -> None:
        """ This function tests the probability calculator with a few values
        gotten by hand, which explains why I did not go to bigger amount of
        dices (or matches)"""
        # Given
        one_dice = 1
        two_dices = 2
        three_dices = 3
        one_match = 1
        two_match = 2
        # When
        result_one_dice = perudo_stats.get_proba_of_given_face(
            one_dice, one_match, True)
        result_two_dice = perudo_stats.get_proba_of_given_face(
            two_dices, one_match, True)
        result_three_dice_one_match = perudo_stats.get_proba_of_given_face(
            three_dices, one_match, True)
        result_three_dice_two_matchs = perudo_stats.get_proba_of_given_face(
            three_dices, two_match, True)
        # Then
        self.assertAlmostEqual(result_one_dice, 1 / 6)
        self.assertAlmostEqual(result_two_dice, 10 / 36)
        self.assertAlmostEqual(result_three_dice_one_match, 75 / 6**3)
        self.assertAlmostEqual(result_three_dice_two_matchs, 15 / 6**3)

    def test_get_proba_of_normal_face_with_first_values(self) -> None:
        """ This function tests the probability calculator with a few values
        gotten by hand, which explains why I did not go to bigger amount of
        dices (or matches)"""
        # Given
        one_dice = 1
        two_dices = 2
        three_dices = 3
        zero_match = 0
        one_match = 1
        two_match = 2
        three_match = 3
        # When
        result_one_dice_no_match = perudo_stats.get_proba_of_given_face(
            one_dice, zero_match, False)
        result_one_dice_one_match = perudo_stats.get_proba_of_given_face(
            one_dice, one_match, False)
        result_two_dice_zero_match = perudo_stats.get_proba_of_given_face(
            two_dices, zero_match, False)
        result_two_dice_one_match = perudo_stats.get_proba_of_given_face(
            two_dices, one_match, False)
        result_two_dice_two_match = perudo_stats.get_proba_of_given_face(
            two_dices, two_match, False)
        result_three_dice_three_matchs = perudo_stats.get_proba_of_given_face(
            three_dices, three_match, False)
        # Then
        self.assertAlmostEqual(result_one_dice_no_match, 2 / 3)
        self.assertAlmostEqual(result_one_dice_one_match, 1 / 3)
        self.assertAlmostEqual(result_two_dice_zero_match, 16 / 36)
        self.assertAlmostEqual(result_two_dice_one_match, 16 / 36)
        self.assertAlmostEqual(result_two_dice_two_match, 4 / 36)
        self.assertAlmostEqual(result_three_dice_three_matchs, 8 / 6**3)

    def test_get_posterior_proba(self) -> None:
        """ This function tests the probability calculator with a few values
        gotten by hand, which explains why I did not go to bigger amount of
        dices (or matches)"""
        # Given
        first_input = (6, 5, 5, 5, False)
        second_input = (3, 1, 2, 0, False)
        # When
        first_result = perudo_stats.get_posterior_proba(*first_input)
        second_result = perudo_stats.get_posterior_proba(*second_input)
        # Then
        self.assertAlmostEqual(first_result, 0.2222222222)
        self.assertAlmostEqual(second_result, 0.3333333333)


if __name__ == "__main__":
    unittest.main()
