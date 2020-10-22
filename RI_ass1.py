from ass1_classes import CorpusReader, SimpleToken, ImprovedTokenizer, Indexer


def main():
    cr = CorpusReader('all_sources_metadata_2020-03-13.csv')
    #print(cr.memory_files.keys())
    impTokenizer = ImprovedTokenizer()
    files_tokens = []
    for k in cr.memory_files.keys():
        files_tokens.append(SimpleToken.process(cr.memory_files[k]))
        #simple_token.add_data(cr.memory_files[k],k)
    #print(files_tokens)
    #print(simple_token.tokens)

    inverted_index = Indexer.process(files_tokens)
    print(inverted_index)
    #print(indexer.dict_inverted_index)



main()
