import csv
import re
import Stemmer
from collections import defaultdict

### Class used to read and store document data such as title and abstract
### Files with no title or abstract are ignored
### All data is stored in a dictionary with a format like
### {id_file0 : "title and abstract", id_file1 : "title and abstract", id_file2 : "title and abstract"}
class CorpusReader():
    def __init__(self, filename):
        ### Open csv file
        with open(filename, "r", newline='') as csvfile:
            data_reader = csv.reader(csvfile, delimiter=',')
            ### Pass the header line
            next(data_reader)
            self.memory_files = { i : line[2] + " " + line[7] for i, line in enumerate(data_reader) if line[2]  != '' and line[7] != ''}
            #self.memory_files={}
            #index_file=0
            #for line in data_reader:
                ### Store only the documents with title and abstract
            #    if line[2]  != '' and line[7] != '':
            #        self.memory_files[index_file] = line[2] + " " +  line[7]

                ### Update file index
            #    index_file +=1    

        #print(self.memory_files)



### Class used to create tokens
### Deletes non alpha numeric characters, ignores tokens with less than 3 chars, transforms all text to lower case and split
class SimpleToken:

    def process(document_data):
        ### Replace all non alpha numeric characters by spaces
        _text = re.sub( '[^a-zA-Z0-9]+', ' ', document_data)

        ### Convert all text to lower case and split
        return {token for token in _text.lower().split() if len(token)>3}
        #print(_test)
        #self.tokens = self._text.lower().split()
        # for elem in self._initial_tokens:
        #     if len(elem) > 3:
        #         self.tokens.append((elem, id_file))


    ###Sort tokens by alphabetical order
    def sort_tokens(self):
        self.tokens = sorted(self.tokens, key= lambda x : x[0])


class ImprovedTokenizer():
    def __init__(self):
        self.stem = Stemmer.Stemmer('english')
        self._stop_words_file = open('snowball_stopwords_EN.txt')
        self._stop_words = self._stop_words_file.read().split()
    
    def process(self,document_data):
        ### Replace all non alpha numeric characters by spaces
        _text = re.sub( '[^a-zA-Z0-9]+', ' ', document_data)
        ##Filter tokens with stop words
        token_init = [ tk for tk in _text.lower().split() if tk not in self._stop_words]
        
        ##Use stemm processing
        return self.stem.stemWords(token_init)
        ### Convert all text to lower case and split
        #return frozenset({token for token in _text.lower().split() if len(token)>3})
    

### Class that given a token and a file id stores that info in a dictionary
class Indexer:
    def process(file_tokens):
        index = defaultdict(list)
        for token_tuple in file_tokens:
            for token in token_tuple[0]:
                index[token].append(token_tuple[1])


        inverted_index = {token : (len(index[token]), index[token]) for token in index.keys()}

        #print(inverted_index)

        return inverted_index
        ### If token already in dictionary of inverted indexes and the file id not in the file list of the token
        # if token in self.dict_inverted_index.keys():
        #     if id_file not in self.dict_inverted_index[token][1]:
        #         self.dict_inverted_index[token][1].append(id_file)
        #         self.dict_inverted_index[token][0] += 1

        # ### If token not in dictionary of inverted indexes add token to dict and init structure with file id
        # else:
        #     self.dict_inverted_index[token] = [1,[id_file]]
