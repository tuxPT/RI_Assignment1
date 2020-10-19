from ass1_classes import CorpusReader, SimpleToken, ImprovedTokenizer, Indexer


def main():
    cr = CorpusReader('all_sources_metadata_2020-03-13.csv')
    #print(cr.memory_files.keys())
    simple_token = SimpleToken()
    impTokenizer = ImprovedTokenizer()    
    indexer = Indexer()
    for k in cr.memory_files.keys():
        simple_token.add_data(cr.memory_files[k],k)
    

    simple_token.sort_tokens()
    #print(simple_token.tokens)

        

    for token in simple_token.tokens:
        indexer.add_token(token[0],token[1])

    #print(indexer.dict_inverted_index)

    

main()