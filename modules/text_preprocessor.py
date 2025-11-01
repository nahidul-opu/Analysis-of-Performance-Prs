import re
import string
from html import unescape
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

class Preprocessor:
    def __init__(
        self,
        *,
        to_lowercase=True,
        remove_punctuation=False,
        remove_stopwords=False,
        lemmatize=False,
        stem=False,
        remove_numbers=False,
        remove_whitespace=False,
        remove_special_chars=False,
        remove_urls=False,
        remove_emails=False,
        remove_html_tags=False,
        remove_md_tags=False
    ):
        self.to_lowercase = to_lowercase
        self.remove_punctuation = remove_punctuation
        self.remove_stopwords = remove_stopwords
        self.lemmatize = lemmatize
        self.stem = stem
        self.remove_numbers = remove_numbers
        self.remove_whitespace = remove_whitespace
        self.remove_special_chars = remove_special_chars
        self.remove_urls = remove_urls
        self.remove_emails = remove_emails
        self.remove_html_tags = remove_html_tags
        self.remove_md_tags = remove_md_tags

        self.stop_words = set(stopwords.words("english")) if remove_stopwords else set()
        self.stemmer = PorterStemmer() if stem else None
        self.lemmatizer = WordNetLemmatizer() if lemmatize else None

    def _remove_html(self, text):
        return BeautifulSoup(text, "html.parser").get_text()

    def _remove_md(self, text):
        # Remove markdown-style formatting like **bold**, *italic*, [links](url), etc.
        text = re.sub(r'\[.*?\]\(.*?\)', '', text)  # remove markdown links
        text = re.sub(r'[`*_>{}\[\]#+\-!]', '', text)  # remove special markdown chars
        return text

    def _remove_urls(self, text):
        return re.sub(r'http\S+|www\.\S+', '', text)

    def _remove_emails(self, text):
        return re.sub(r'\S+@\S+\.\S+', '', text)

    def _remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def _remove_numbers(self, text):
        return re.sub(r'\d+', '', text)

    def _remove_special_chars(self, text):
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)

    def _remove_stopwords(self, tokens):
        return [word for word in tokens if word not in self.stop_words]

    def _stem_words(self, tokens):
        return [self.stemmer.stem(word) for word in tokens]

    def _lemmatize_words(self, tokens):
        return [self.lemmatizer.lemmatize(word) for word in tokens]

    def preprocess(self, text):
        text = unescape(text)

        if self.remove_html_tags:
            text = self._remove_html(text)
        if self.remove_md_tags:
            text = self._remove_md(text)
        if self.remove_urls:
            text = self._remove_urls(text)
        if self.remove_emails:
            text = self._remove_emails(text)
        if self.remove_numbers:
            text = self._remove_numbers(text)
        if self.remove_punctuation:
            text = self._remove_punctuation(text)
        if self.remove_special_chars:
            text = self._remove_special_chars(text)
        if self.to_lowercase:
            text = text.lower()
        if self.remove_whitespace:
            text = ' '.join(text.split())

        tokens = text.split()

        if self.remove_stopwords:
            tokens = self._remove_stopwords(tokens)
        if self.stem:
            tokens = self._stem_words(tokens)
        if self.lemmatize:
            tokens = self._lemmatize_words(tokens)

        return ' '.join(tokens)
