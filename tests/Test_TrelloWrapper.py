import TrelloWrapper as wrapper
import unittest

class PrimesTestCase(unittest.TestCase):
    """Tests for TrelloWrapper."""


    """ TESTS FOR LEVENSHTEIN DISTANCE """

    def test_0_levenshtein_distance(self):
        """Is 0 successfully determined in the levenshtein distance?"""
        # Two identical words should return 0
        test = wrapper.levenshtein_distance("unito", "unito")
        self.assertEqual(test,0, "Unito and Unito should return 0")

    def test_2_levenshtein_distance(self):
        """Is 2 successfully determined in the levenshtein distance?"""
        # Delete F, Add N at the end
        test = wrapper.levenshtein_distance("flaw", "lawn")
        self.assertEqual(test, 2, "flaw and lawn should return 2")

    def test_3_levenshtein_distance(self):
        """Is 3 successfully determined in the levenshtein distance?"""
        test = wrapper.levenshtein_distance("kitten", "sitting")
        self.assertEqual(test,3, "Kitten and Sitting should return 3")

    """ END TESTS FOR LEVENSHTEIN DISTANCE """


if __name__ == '__main__':
    unittest.main()