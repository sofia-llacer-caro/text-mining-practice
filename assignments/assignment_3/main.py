#!/usr/bin/python

import pandas as pd
import re
import unicodedata
import string
import sklearn
import sys
import spacy
import nltk
from collections import Counter
from nltk.stem import PorterStemmer



def read_file(file: str) -> str: 
    '''
    Takes in the location of a .txt file, returns the contents of a .txt file as a string.
    :input: file; .txt file to be read
    :output: file_contents; contents of the file as a string
    '''
    try:
        with open(file, 'r', encoding="utf8") as f:
            file_contents = f.read()
        return file_contents
      
    except IOError:
        print("Error opening or reading input file: ", file)
        sys.exit()


def split_into_documents(text):
    sentence_delimiters = r'[.!?]'
    sentences = re.split(sentence_delimiters, text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences


def create_knowledge_base(documents):
    nlp = spacy.load('en_core_web_sm')
    knowledge_base = []
    for doc_text in documents:
        doc = nlp(doc_text)
        entities = [ent.text for ent in doc.ents]  # Extract named entities
        nouns = [token.lemma_ for token in doc if token.pos_ == 'NOUN']  # Extract nouns
        knowledge_base.append({'entities': entities, 'nouns': nouns})
    return knowledge_base

def named_entity_recognition(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    print("Named Entity Recognition:")
    print("The language model recognizes that certain words are organizational names while others are locations, and still other combinations relate to money, dates, etc. Named entities are accessible through the ents property of a text object.")
    for ent in doc.ents:
        print(ent.text + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))

def list_root_words(documents):
    stemmer = PorterStemmer()
    root_words = set()  # Using a set to ensure unique root words
    nlp = spacy.load('en_core_web_sm')
    for document in documents:
        doc = nlp(document)
        for token in doc:
            if token.pos_ == 'NOUN':
                root_word = stemmer.stem(token.text.lower())
                root_words.add(root_word)
    return root_words


def root_words_frequency(root_words):
    root_word_counts = Counter(root_words)
    frequent_root_words = {word: count for word, count in root_word_counts.items() if count > 15}
    return frequent_root_words

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    # 1. Read with Python a chapter from your favourite book and create a Corpus C.
    file = "favourite_book.txt"
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
    tokens_no_stopwords = [token.text for token in tokens_raw if not token.is_stop]
    number_of_tokens_no_stopwords = len(tokens_no_stopwords)
    print(f"Total number of tokens after removing stop words: {number_of_tokens_no_stopwords}")

    # 5. Preprocess the data for required cleaning up of data.
    preprocessed_text = ' '.join(tokens_no_stopwords).lower()
    tokens_preprocessing = [token.lemma_ for token in tokens_raw if not token.is_punct and not token.is_space]
    preprocessed_text = ' '.join(tokens_preprocessing)


    # 6. Create a knowledge base with the final set of documents Di from Corpus C.
    # This is taken to be from the initial corpus
    knowledge_base = create_knowledge_base(documents)

    # 7. Does your knowledge base contains all the proper nouns. Use Named Entity Recognition(NER) to find out.
    # Answer: There are some differences. In general, the knowledge base is not as accurate,
    # as it identifies for example "our" as a noun. On the other hand, NER is more accurate as well as more precise,
    # as it is able to recognise which type of entity, for example, we're dealing with, such as Nationalities or religious or political groups
    # It still, however, makes mistakes, such as identifying Belarusian Turkmen Ukrainian Kazakh as an EVENT.
    nouns_knowledge_base = []
    for item in knowledge_base:
        nouns_knowledge_base.extend(item['nouns'])
    print(f"The nouns found through the knowledge base are the following: {nouns_knowledge_base}")
    nouns_ner = named_entity_recognition(preprocessed_text)

    # 8. Change the proper names for some tokens in the knowldge base and introduce a mapping that
    # recognizes them. Now introduce a document and do the text mapping with your new mapping
    # and proper names.
    # Now they're manually substituted
    mapping = {
        "homo": "Homo",
        "sovieticus": "Sovieticus",
        "gulag": "Gulag"
    }
    test_document = "The homo sovieticus was accustomed to the presence of gulags as a weapon of terror."
    for entity, proper_name in mapping.items():
        test_document = test_document.replace(entity, proper_name)
    print("Document with proper names:")
    print(test_document)

    # 9. With parts of speech(POS) tagging find out the total number of nouns in Corpus C. Which
    # noun is repeated the most. Is this relevant to character dominance in the book?
    # Answer: the most repeated word is 'life', which is actually very poetic taking into account
    # the topic of the book. It is an account of how the soviet world fell and interviews of everyday
    # people about how their life changed and how their cosmovision was different after this.
    # The book is very crude, and I thought the most repeated word in the introduction would be 'soviet'.
    # This is why I find it very poetic that it's actually 'life' instead, aligns very well with the 
    # ideals and literary view of the author, who is all about the life of just regular people.
    noun_counts = {}
    total_nouns = 0
    for document in documents: # Iterate through each document in the corpus
        doc = nlp(document)
        for token in doc:
            if token.pos_ == 'NOUN':
                total_nouns += 1
                if token.text in noun_counts:
                    noun_counts[token.text] += 1
                else:
                    noun_counts[token.text] = 1

    print(f"Total number of nouns in Corpus C: {total_nouns}")
    most_common_noun = max(noun_counts, key=noun_counts.get)
    print(f"The most repeated noun in Corpus C is: {most_common_noun}, repeated {noun_counts[most_common_noun]} times")


    # 10. List the root words from corpus C that have frequency higher than 15. Do they show you
    # something about the book?
    # Answer: This is not giving any output, and when printing debug statements I found that all of them have
    # frequency 1. This is either because the frequency is not properly counted, and a new frequency
    # counter is started for every word, regardless of whether it's repeated; or because the corpus is not 
    # big enough for there to be several occurences of a root. However, this is unlikely as 'life' appears 8 times
    # in the Corpus, as found before.
    root_words = list_root_words(documents)
    frequent_root_words = root_words_frequency(root_words)
    print("Root words with frequency higher than 15:")
    for word, count in frequent_root_words.items():
        print(f"{word}: {count}")


    return 'Done!'

if __name__ == "__main__":
    print(main())