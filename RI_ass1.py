#!/bin/env python3
from ass1_classes import CorpusReader, SimpleTokenizer, ImprovedTokenizer, Indexer, results
import time
import sys

data = CorpusReader.read('all_sources_metadata_2020-03-13.csv')

#start timer
time1 = time.time()

#if '-i' use ImprovedTokenizer
if len(sys.argv) == 2 and sys.argv[1] == '-i':
    tokenizer = ImprovedTokenizer('english', 'snowball_stopwords_EN.txt')
    tokenizer_type = 'Improved'
#else use Default SimpleTokenizer
else:
    tokenizer = SimpleTokenizer()
    tokenizer_type = 'Simple'

#Tokenization Step
files_tokens1 = [tokenizer.process(data_from_doc) for data_from_doc in data]
#Indexing Step
inverted_index1 = Indexer.process(files_tokens1)

#end timer
time2 = time.time()

#show results
results(tokenizer_type, time1, time2, inverted_index1)

