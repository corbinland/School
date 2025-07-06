# test_final.py
import unittest
from final import determine_winner

class TestRPS(unittest.TestCase):

    def test_tie(self):
        self.assertEqual(determine_winner("rock", "rock"), "Tie")
        self.assertEqual(determine_winner("paper", "paper"), "Tie")
        self.assertEqual(determine_winner("scissors", "scissors"), "Tie")

    def test_player_wins(self):
        self.assertEqual(determine_winner("rock", "scissors"), "Player")
        self.assertEqual(determine_winner("paper", "rock"), "Player")
        self.assertEqual(determine_winner("scissors", "paper"), "Player")

    def test_computer_wins(self):
        self.assertEqual(determine_winner("rock", "paper"), "Computer")
        self.assertEqual(determine_winner("paper", "scissors"), "Computer")
        self.assertEqual(determine_winner("scissors", "rock"), "Computer")

if __name__ == "__main__":
    unittest.main()
