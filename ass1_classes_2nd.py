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

    def process(document_data, id_file):
        ### Replace all non alpha numeric characters by spaces
        _text = re.sub( '[^a-zA-Z0-9]+', ' ', document_data)

        ### Convert all text to lower case and split
        return {(token, id_file) for token in _text.lower().split() if len(token)>3}
        

class ImprovedTokenizer():
    def __init__(self):
        self.stem = Stemmer.Stemmer('english')
        self._stop_words = open('snowball_stopwords_EN.txt').read().split()

    def process(self,document_data, id_file):
        ### Replace all non alpha numeric characters by spaces
        _text = re.sub( '[^a-zA-Z0-9]+', ' ', document_data)

        ##Filter tokens with stop words
        token_init = [ tk for tk in _text.lower().split() if tk not in self._stop_words]
        
        ##Use stemm processing
        return {(token, id_file) for token in set(self.stem.stemWords(token_init))}
       

### Class that given a token and a file id stores that info in a dictionary
class Indexer:
    def process(file_tokens):
        index = {}
        last= ''
        list_tokens=[]
        for tokens in file_tokens:
            if tokens[0] != last:
                index[last] = (len(list_tokens),list_tokens)
                list_tokens = []
                last = tokens[0]

            list_tokens.append(tokens[1])
        


        #print(index)

        return index
