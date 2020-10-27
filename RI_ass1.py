#!/bin/env python3
from ass1_classes import CorpusReader, SimpleTokenizer, ImprovedTokenizer, Indexer, results
import time
import sys
import tracemalloc

#tracemalloc.start()

data = CorpusReader.read('all_sources_metadata_2020-03-13.csv')


#if '-i' use ImprovedTokenizer
if len(sys.argv) == 2 and sys.argv[1] == '-i':
    tokenizer = ImprovedTokenizer('english', 'snowball_stopwords_EN.txt')
    tokenizer_type = 'Improved'
#else use Default SimpleTokenizer
else:
    tokenizer = SimpleTokenizer()
    tokenizer_type = 'Simple'

#Tokenization Step
files_tokens1 = [tokenizer.process(data_from_doc[1]) for data_from_doc in data]
#Indexing Step

#start timer
time1 = time.time()

inverted_index1 = Indexer.process(files_tokens1)

#end timer
time2 = time.time()
#memory, max = tracemalloc.get_traced_memory()

with open('results.txt', 'w') as fout:
    fout.write(str([inverted_index1.keys()]))
#tracemalloc.stop()
#show results
results(tokenizer_type, time2- time1,  1, inverted_index1, data)

