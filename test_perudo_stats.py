import unittest
import perudo_stats


class TestStatistics(unittest.TestCase):
    """ Test class for the computation done in the statistics module """
    def test_get_proba_of_given_face_with_first_values(self) -> None:
        # Given
        one_dice = 1
        two_dices = 2
        three_dices = 3
        one_match = 1
        two_match = 2
        # When
        result_one_dice = perudo_stats.get_proba_of_given_face(
            one_dice, one_match)
        result_two_dice = perudo_stats.get_proba_of_given_face(
            two_dices, one_match)
        result_three_dice_one_match = perudo_stats.get_proba_of_given_face(
            three_dices, one_match)
        result_three_dice_two_matchs = perudo_stats.get_proba_of_given_face(
            three_dices, two_match)
        # Then
        self.assertAlmostEqual(result_one_dice, 1 / 6)
        self.assertAlmostEqual(result_two_dice, 10 / 36)
        self.assertAlmostEqual(result_three_dice_one_match, 75 / 6**3)
        self.assertAlmostEqual(result_three_dice_two_matchs, 15 / 6**3)


if __name__ == "__main__":
    unittest.main()
