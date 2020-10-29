# Authors:
## Alexandre Santos 80106
## Leonardo Costa   80162

import csv
import re
import Stemmer
from collections import defaultdict

# Class used to read and store document data such as title and abstract
# Files with no title or abstract are ignored
# All data is stored in a list with a format like
# [(doi , "title and abstract"), (doi , "title and abstract"), (doi , "title and abstract")]
class CorpusReader:
    def read(filename):
        # Open csv file
        with open(filename, "r", newline='') as csvfile:
            data_reader = csv.reader(csvfile, delimiter=',')
            # Pass the header line
            next(data_reader)
            return [(line[3],line[2] + " " + line[7]) for line in data_reader if line[7] != '']



# Class used to create tokens
# Deletes non alpha characters, ignores tokens with less than 3 chars, transforms all text to lower case and split
class SimpleTokenizer:
    def __init__(self):
        # precompiled regex
        # deletes all characters not presented in A-Za-z
        self.match = re.compile('[^a-zA-Z]+')

    def process(self, document_data):
        # Replace all non alphabetic characters by spaces
        # Convert all text to lower case and split by spaces
        _text = self.match.sub(' ', document_data).lower().split()

        # removes trailing and leading characters like - and _ from tokens
        return {token for token in _text if len(token)>2}

class ImprovedTokenizer:
    def __init__(self, language, stop_words_file):
        self.stem = Stemmer.Stemmer(language)
        self._stop_words = open(stop_words_file).read().split() + ['-','_','.',',','/','']


        # precompiled regex that
        # deletes all characters not presented in A-Za-z0-9-_.,
        # that allows words with _ - . , / and \ in the middle not to be splitted, just like links and number intervals
        self.match = re.compile('[^A-Za-z0-9-_.,/]+')
        self.stem.maxCacheSize = 100000
    def process(self, document_data):
        # turns all text into lower case and splits by spaces
        _text = self.match.sub(' ', document_data).lower().split()

        # Filter tokens with stop words
        # removes leading and trailing characters like \-_.,/ from tokens
        token_init = {token.strip('-_.,/') for token in _text if token.strip('-_.,/') not in self._stop_words}

        # Use stemm processing
        return self.stem.stemWords(token_init)


# Class that given a token and a file id stores that info in a dictionary
class Indexer:
    def process(file_tokens):
        index = defaultdict(list)
        # Beware only stores the id and not the length of the list of ids because python internaly has a variable where the size of lists, sets and other objects is stored, so len(list) is a O(1) operation
        for i, tokens in enumerate(file_tokens):
            for token in tokens:
                index[token].append(i)
        return index

def results(tokenizer_name, time1, time2, inverted_index1, data_to_match):
    print('Answers'
          + '\n------- with ' + tokenizer_name + ' tokenizer -------'
          + '\na) What was the total indexing and writing time is required to index this collection?'
          + '\nR) Indexing time: ' + str(time1) + " segundos / writing index to file: " + str(time2) + " segundos"
          + '\nb) What is your vocabulary size?'
          + '\nR: ' + str(len(inverted_index1))
          + '\nc) List the ten first terms (in alphabetic order) that appear in only one document (document frequency = 1)'
          + '\nR: ' + str(sorted([(token, data_to_match[inverted_index1[token][0]][0]) for token in inverted_index1 if len(inverted_index1[token]) == 1], key= lambda token : token[0]  )[0:10])
          + '\nd) List the ten terms with highest document frequency'
          + '\nR: ' + str(sorted([(token, len(inverted_index1[token])) for token in inverted_index1], key=lambda token: token[1], reverse=True)[0:10]))

