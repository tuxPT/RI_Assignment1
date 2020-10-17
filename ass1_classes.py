import csv

### Class used to read and store document data such as title and abstract
### Files with no title or abstract are ignored
### All data is stored in a dictionary with a format like
### {id_file0 : "title and abstract", id_file1 : "title and abstract", id_file2 : "title and abstract"}
class CorpusReader():
    def __init__(self, filename):
        self.memory_files = {}
        ### Open csv file
        with open(filename, "r", newline='') as csvfile:
            data_reader = csv.reader(csvfile, delimiter=',')
            ### Pass the header line
            next(data_reader)
            index_file=0
            for line in data_reader:
                ### Store only the documents with title and abstract
                if line[2]  != '' and line[7] != '':
                    self.memory_files[index_file] = line[2] + " " +  line[7]

                ### Update file index
                index_file +=1

        print(self.memory_files)

   
    
### Class used to create tokens
### Only deletes non alpha numeric characters, transforms all text to lower case and split
class SimpleToken():
    def __init__(self, document_data):
        self._text = document_data
        self._not_alphaNum = ['\'', ',', '.', '*', '+', '=', '@', ':', ';', '"', '?', '!', '/', '\\', '|', '#', '-', '<', '>', '$', '%', '(',')', '[',']','{','}']
        ### Delete all non alpha numeric characters
        for char in self._not_alphaNum:
            self._text = self._text.replace(char, "")
        

        ### Convert all text to lower case and split
        self.tokens = self._text.lower().split()



### Class that given a token and a file id stores that info in a dictionary
class Indexer():
    def __init__(self):
        self.dict_inverted_index = {}

    def add_token(self, token, id_file):

        ### If token already in dictionary of inverted indexes and the file id not in the file list of the token
        if token in self.dict_inverted_index.keys()and id_file not in self.dict_inverted_index[token][1]:
                self.dict_inverted_index[token][1].append(id_file)
                self.dict_inverted_index[token][0] += 1

        ### If token not in dictionary of inverted indexes add token to dict and init structure with file id    
        else:
            self.dict_inverted_index[token] = [1,[id_file]]

