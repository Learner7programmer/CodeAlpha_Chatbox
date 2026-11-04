"""Run with: python -m unittest test_chatbot.py -v"""
import unittest
from chatbot import normalize, extract_name, detect_intents, respond


class TestChatbot(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize("  Hey!!  HOW r u? "), "hey how r u")

    def test_greeting(self):
        self.assertIn("greet", detect_intents(normalize("Hello")))

    def test_word_boundary(self):
        # "hi" must not match inside "this" or "which"
        self.assertEqual(detect_intents(normalize("this which")), [])

    def test_multiple_intents(self):
        intents = detect_intents(normalize("Hey!! how r u?"))
        self.assertEqual(intents, ["greet", "status"])

    def test_status_reply(self):
        memory = {"name": None, "misses": 0}
        self.assertIn(respond("status", memory),
                      ["I'm fine, thanks!", "Doing great, thanks for asking!"])

    def test_bye(self):
        self.assertIn("bye", detect_intents(normalize("ok bye")))

    def test_extract_name(self):
        self.assertEqual(extract_name("my name is Tanvi"), "Tanvi")
        self.assertIsNone(extract_name("hello"))

    def test_greeting_uses_name(self):
        memory = {"name": "Tanvi", "misses": 0}
        self.assertIn("Tanvi", respond("greet", memory))

    def test_unknown(self):
        self.assertEqual(detect_intents(normalize("asdfgh")), [])


if __name__ == "__main__":
    unittest.main()
