from ass1_classes_2nd import CorpusReader, SimpleToken, ImprovedTokenizer, Indexer
import time

def main():

    cr = CorpusReader('all_sources_metadata_2020-03-13.csv')
    #print(cr.memory_files.keys())
    time1 = time.time()

    simpleTokenizer_files_tokens = sorted([elem for k in cr.memory_files.keys() for elem in SimpleToken.process(cr.memory_files[k], k)], key= lambda x : x[0])

    
    #simple_token.add_data(cr.memory_files[k],k)
    #print(files_tokens)
    #print(simple_token.tokens)
    inverted_index = Indexer.process(simpleTokenizer_files_tokens)
    #print(inverted_index)
    #print(indexer.dict_inverted_index)
    time2 = time.time()

    print("Simple tokenizer time: " + str(time2 -time1) + " segundos")

    #time3 = time.time()
    #impTokenizer = ImprovedTokenizer()

    #improvedTokenizer_files_tokens = sorted([elem for k in cr.memory_files.keys() for elem in impTokenizer.process(cr.memory_files[k], k)], key= lambda x : x[0])
    #inverted_index = Indexer.process(improvedTokenizer_files_tokens)


    #time4 = time.time()

    #print("Improved tokenizer time: " + str(time4 -time3) + " segundos")

main()
