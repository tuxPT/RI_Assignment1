import csv
import re
import Stemmer
from collections import defaultdict

# Class used to read and store document data such as title and abstract
# Files with no title or abstract are ignored
# All data is stored in a dictionary with a format like
# {id_file0 : "title and abstract", id_file1 : "title and abstract", id_file2 : "title and abstract"}
class CorpusReader():
    def __init__(self, filename):
        # Open csv file
        with open(filename, "r", newline='') as csvfile:
            data_reader = csv.reader(csvfile, delimiter=',')
            # Pass the header line
            next(data_reader)
            self.memory_files = { i : line[2] + " " + line[7] for i, line in enumerate(data_reader) if line[2]  != '' and line[7] != ''}



# Class used to create tokens
# Deletes non alpha numeric characters, ignores tokens with less than 3 chars, transforms all text to lower case and split
class SimpleToken:
    def __init__(self):
        # precompiled regex
        self.match = re.compile('[^a-zA-Z0-9]+')

    def process(self, document_data):
        # Replace all non alpha numeric characters by spaces
        _text = self.match.sub(' ', document_data).lower().split()

        # Convert all text to lower case and split
        return frozenset({token for token in _text if len(token)>3})


    # Sort tokens by alphabetical order
    def sort_tokens(self):
        self.tokens = sorted(self.tokens, key= lambda x : x[0])


class ImprovedTokenizer:
    def __init__(self, language, stop_words_file):
        self.stem = Stemmer.Stemmer(language)
        self._stop_words = open(stop_words_file).read().split()
        # precompiled regex
        self.match = re.compile('[^a-zA-Z0-9]+')
    def process(self, document_data):
        # Replace all non alpha numeric characters by spaces
        _text = self.match.sub(' ', document_data).lower().split()

        # Filter tokens with stop words
        token_init = frozenset({ tk for tk in _text if tk not in self._stop_words})

        # Use stemm processing
        return self.stem.stemWords(token_init)


# Class that given a token and a file id stores that info in a dictionary
class Indexer:
    def process(file_tokens):
        index = defaultdict(tuple)
        for i, tokens in enumerate(file_tokens):
            for token in tokens:
                index[token]
        return index
