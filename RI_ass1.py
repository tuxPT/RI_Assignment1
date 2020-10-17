from ass1_classes import CorpusReader,SimpleToken,Indexer


def main():
    cr = CorpusReader('all_sources_metadata_2020-03-13.csv')
    print(cr.memory_files.keys())
    indexer = Indexer()
    for k in cr.memory_files.keys():
        simple_token = SimpleToken(cr.memory_files[k])

        print(simple_token.tokens)

        

        for token in simple_token.tokens:
            indexer.add_token(token,k)

        print(indexer.dict_inverted_index)

    

main()