from ass1_classes import CorpusReader, SimpleToken, ImprovedTokenizer, Indexer
import time

def main():

    cr = CorpusReader('all_sources_metadata_2020-03-13.csv')

    #start timer
    time1 = time.time()
    simple_token = SimpleToken()
    files_tokens1 = [(simple_token.process(cr.memory_files[k]), k) for k in cr.memory_files.keys() ]
    inverted_index1 = Indexer.process(files_tokens1)

    #end timer
    time2 = time.time()

    print('Answers'
          + '\n------- with simple tokenizer -------'
          + '\na) What was the total indexing time and how much memory (roughly) is required to index this collection?'
          + '\n' + str(time2 -time1) + " segundos"
          + '\nb) What is your vocabulary size?'
          + '\nR: ' + str(len(list(inverted_index1.keys())))
          + '\nc) List the ten first terms (in alphabetic order) that appear in only one document (document frequency = 1)')

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


    # start timer
    time3 = time.time()

    impTokenizer = ImprovedTokenizer('english', 'snowball_stopwords_EN.txt')
    files_tokens2 = [(impTokenizer.process(cr.memory_files[k]), k) for k in cr.memory_files.keys() ]
    inverted_index2 = Indexer.process(files_tokens2)

    # stop timer
    time4 = time.time()

    print('\n------- with improved tokenizer -------'
    + '\na) What was the total indexing time and how much memory (roughly) is required to index this collection?'
    + '\n' + str(time4 -time3) + " segundos"
    + '\nb) What is your vocabulary size?'
    + '\nR: '  + str(len(list(inverted_index2.keys())))
    + '\nc) List the ten first terms (in alphabetic order) that appear in only one document (document frequency = 1)')

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
