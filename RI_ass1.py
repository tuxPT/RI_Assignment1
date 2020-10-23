from ass1_classes import CorpusReader, SimpleToken, ImprovedTokenizer, Indexer
import time

def main():

    time1 = time.time()
    cr = CorpusReader('all_sources_metadata_2020-03-13.csv')
    #print(cr.memory_files.keys())
    impTokenizer = ImprovedTokenizer()
    files_tokens = []
    for k in cr.memory_files.keys():
        files_tokens.append((SimpleToken.process(cr.memory_files[k]), k))

        #simple_token.add_data(cr.memory_files[k],k)
    #print(files_tokens)
    #print(simple_token.tokens)
    inverted_index = Indexer.process(files_tokens)
    #print(inverted_index)
    #print(indexer.dict_inverted_index)

    time2 = time.time()

    print(str(time2 -time1) + " segundos")

main()