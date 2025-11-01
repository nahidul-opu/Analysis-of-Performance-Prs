import unittest
from modules.text_classifiers import RegexClassifier, SimpleSubstringClassifier, LLMClassifier, EmbeddingClassifier

keywords = set(["performance", "compile-time-hog", "perf", "hang", "optimization", "responsive", "slow" , "speed", "latency", "throughput", "wait", "slow", "fast", "lag", "tim", "minor", "stuck", "instant", "respons", "react", "speed", "latenc", "perform", "throughput", "hang", "memory", "leak"])
keyword_text = " ".join(keywords)

class TestRegexClassifier(unittest.TestCase):
    def setUp(self):
        self.keywords = keywords
        self.classifier = RegexClassifier(self.keywords)

    def test_match_found(self):
        text = "The changes improved performance in time complexity"
        self.assertTrue(self.classifier.classify(text))
        matches = self.classifier.get_matches()
        self.assertIn("performance", [m.lower() for m in matches])
        self.assertIn("time", [m.lower() for m in matches])

    def test_no_match(self):
        text = "Fix bug in user interface"
        self.assertFalse(self.classifier.classify(text))
        self.assertEqual(self.classifier.get_matches(), [])


class TestSimpleSubstringClassifier(unittest.TestCase):
    def setUp(self):
        self.keywords = keywords
        self.classifier = SimpleSubstringClassifier(self.keywords)

    def test_match_found(self):
        text = "The changes improved performance in time complexity"
        self.assertTrue(self.classifier.classify(text))
        matches = [m.lower() for m in self.classifier.get_matches()]
        self.assertIn("performance", matches)
        self.assertIn("tim", matches)

    def test_no_match(self):
        text = "Fix bug in user interface"
        self.assertFalse(self.classifier.classify(text))
        self.assertEqual(self.classifier.get_matches(), [])


class TestLLMClassifier(unittest.TestCase):
    def setUp(self):
        self.classifier = LLMClassifier(prompt_template="Does  the following text discuss performance issues? Text: ")

    def test_classify_returns_false(self):
        text = "Any text."
        self.assertFalse(self.classifier.classify(text))



class TestEmbeddingClassifier(unittest.TestCase):
    def setUp(self):
        self.base_text = keyword_text
        self.classifier = EmbeddingClassifier(self.base_text)

    def test_classify_returns_false(self):
        text = "Random text"
        self.assertFalse(self.classifier.classify(text))


if __name__ == "__main__":
    unittest.main()
