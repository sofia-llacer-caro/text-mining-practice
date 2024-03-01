#!/usr/bin/python

import spacy
from config import FILE, STOP_WORDS
from manager import read_file, preprocess, split_into_documents


def main():
    # 1. Read with Python a chapter from your favourite book and create a Corpus C.
    file = FILE
    text = read_file(file)

    corpus = [] # Initialize corpus
    documents = split_into_documents(text)
    for document in documents: 
        corpus.append(document)

    # 2. What is the total number of documents in the corpus C?
    # Answer: 45
    number_of_documents = len(documents)
    print(f"Total number of documents: {number_of_documents}")

    # 3. Find the Tokens from the corpus C by using Tokenization. What is the total number of tokens?
    # Answer: 875
    nlp = spacy.load('en_core_web_sm') # Load model
    tokens_raw = nlp(text)
    number_of_tokens_raw = len(tokens_raw)
    print(f"Total number of tokens before removing stop words: {number_of_tokens_raw}")

    # 4. Remove the stop words and repeat the count of tokens. Has the number changed?
    # Answer: 494 (almost half as before, much lower computational requirements for later analysis)
    stop_words = STOP_WORDS
    text_clean = " ".join([word for word in text.split() if word not in stop_words])
    tokens_clean = nlp(text_clean)
    number_of_tokens_clean = len(tokens_clean)
    print(f"Total number of tokens after removing stop words: {number_of_tokens_clean}")

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
    



    return "as"

if __name__ == "__main__":
    print(main())