from ass1_classes import CorpusReader, SimpleToken, ImprovedTokenizer, Indexer
import time

def main():

    cr = CorpusReader('all_sources_metadata_2020-03-13.csv')

    #start timer
    time1 = time.time()
    
    files_tokens1 = [(SimpleToken.process(cr.memory_files[k]), k) for k in cr.memory_files.keys() ]
    inverted_index1 = Indexer.process(files_tokens1)
    
    #end timer
    time2 = time.time()

    print('Answers')
    print('------- with simple tokenizer -------')
    print('a) What was the total indexing time and how much memory (roughly) is required to index this collection?')

    print(str(time2 -time1) + " segundos")

    print('b) What is your vocabulary size?')
    print('R: '  + str(len(list(inverted_index1.keys()))))
    print('c) List the ten first terms (in alphabetic order) that appear in only one document (document frequency = 1)')

    term_with_one = [token for token in list(inverted_index1.keys()) if inverted_index1[token][0] == 1]
    ten_terms_alph = sorted(term_with_one)
    print('R: ')
    for x in ten_terms_alph[0:10]:
        print(x  + ":" + str(inverted_index1[x])) 
    print('d) List the ten terms with highest document frequency')
    ten_terms_high = sorted(inverted_index1, key = lambda x : inverted_index1[x][0] and inverted_index1[x] , reverse= True)
    print('R: ')
    for x in ten_terms_high[0:10]:
        print( (x,inverted_index1[x][0]) )
    
    
    ##start timer
    time3 = time.time()
    
    impTokenizer = ImprovedTokenizer()
    files_tokens2 = [(impTokenizer.process(cr.memory_files[k]), k) for k in cr.memory_files.keys() ]
    inverted_index2 = Indexer.process(files_tokens2)
    
    ###stop timer 
    time4 = time.time()
    
    print('------- with improved tokenizer -------')
    print('a) What was the total indexing time and how much memory (roughly) is required to index this collection?')

    print(str(time4 -time3) + " segundos")

    print('b) What is your vocabulary size?')
    print('R: '  + str(len(list(inverted_index2.keys()))))
    print('c) List the ten first terms (in alphabetic order) that appear in only one document (document frequency = 1)')

    term_with_one = [token for token in list(inverted_index2.keys()) if inverted_index2[token][0] == 1]
    ten_terms_alph = sorted(term_with_one)
    print('R: ')
    for x in ten_terms_alph[0:10]:
        print(x  + ":" + str(inverted_index2[x])) 
    print('d) List the ten terms with highest document frequency')
    ten_terms_high = sorted(inverted_index2, key = lambda x : inverted_index2[x][0] and inverted_index2[x] , reverse= True)
    print('R: ')
    for x in ten_terms_high[0:10]:
        print( (x,inverted_index2[x][0]) )
    





main()