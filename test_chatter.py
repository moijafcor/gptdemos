import unittest
from unittest.mock import patch
from chatbot_tokens_counter import chatter


class TestChatter(unittest.TestCase):
    @patch(
        "builtins.input", side_effect=["Hello", "How are you?", "I'm fine, thank you!"]
    )
    def test_chatter(self, mock_input):
        chatter()
        # Add your assertions here


if __name__ == "__main__":
    unittest.main()
