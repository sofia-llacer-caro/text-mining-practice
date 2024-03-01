#!/usr/bin/python

from config import FILE
from manager import read_file, preprocess


def main():
    # 1. Read with Python a chapter from your favourite book and create a Corpus C.
    file = FILE
    corpus = read_file(file)

    # 2. What is the total number of documents in the corpus C?
    
    # 3. Find the Tokens from the corpus C by using Tokenization. What is the total number of tokens?
    # 4. Remove the stop words and repeat the count of tokens. Has the number changed?
    # 5. Preprocess the data for required cleaning up of data.
    # 6. Create a knowledge base with the final set of documents Di from Corpus C.
    # 7. Does your knowledge base contains all the proper nouns. Use Named Entity Recognition(NET)
    # to find out.
    # 8. Change the proper names for some tokens in the knowldge base and introduce a mapping that
    # recognizes them. Now introduce a document and do the text mapping with your new mapping
    # and proper names.
    # 9. With parts of speech(POS) tagging find out the total number of nouns in Corpus C. Which
    # noun is repeated the most. Is this relevant to character dominance in the book?
    # 10. List the root words from corpus C that have frequency higher than 15. Do they show you
    # something about the book?
    



    return corpus

if __name__ == "__main__":
    print(main())