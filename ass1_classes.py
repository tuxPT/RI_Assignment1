import csv
import re
import Stemmer
from collections import defaultdict

# Class used to read and store document data such as title and abstract
# Files with no title or abstract are ignored
# All data is stored in a dictionary with a format like
# {id_file0 : "title and abstract", id_file1 : "title and abstract", id_file2 : "title and abstract"}
class CorpusReader:
    def read(filename):
        # Open csv file
        with open(filename, "r", newline='') as csvfile:
            data_reader = csv.reader(csvfile, delimiter=',')
            # Pass the header line
            next(data_reader)
            return [(line[3],line[2] + " " + line[7]) for line in data_reader if line[7] != '']



# Class used to create tokens
# Deletes non alpha numeric characters, ignores tokens with less than 3 chars, transforms all text to lower case and split
class SimpleTokenizer:
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
        self.stem.maxCacheSize = 100000
    def process(self, document_data):
        # Replace all non alpha numeric characters by spaces
        _text = self.match.sub(' ', document_data).lower().split()

        # Filter tokens with stop words
        token_init = frozenset({ token for token in _text if token not in self._stop_words})

        # Use stemm processing
        return self.stem.stemWords(token_init)


# Class that given a token and a file id stores that info in a dictionary
class Indexer:
    def process(file_tokens):
        index = defaultdict(list)
        for i, tokens in enumerate(file_tokens):
            for token in tokens:
                index[token].append(i)
        return index

def results(tokenizer_name, time1, time2, inverted_index1, data_to_match):
    print('Answers'
          + '\n------- with ' + tokenizer_name + ' tokenizer -------'
          + '\na) What was the total indexing time and how much memory (roughly) is required to index this collection?'
          + '\n' + str(time2 - time1) + " segundos"
          + '\nb) What is your vocabulary size?'
          + '\nR: ' + str(len(inverted_index1))
          + '\nc) List the ten first terms (in alphabetic order) that appear in only one document (document frequency = 1)'
          + '\nR: ' + str(sorted([(token, data_to_match[inverted_index1[token][0]][0]) for token in inverted_index1 if len(inverted_index1[token]) == 1])[0:10])
          + '\nd) List the ten terms with highest document frequency'
          + '\nR: ' + str(sorted([token for token in inverted_index1], key=lambda token: len(inverted_index1[token]), reverse=True)[0:10]))

