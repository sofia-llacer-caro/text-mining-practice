#!/usr/bin/python

import pandas as pd
import re
import unicodedata
import string
import sklearn
import sys
import spacy
from config import FILE, STOP_WORDS, BAG_OF_WORDS


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


def preprocess(text:str) -> str:
    '''
    Preprocesses a .txt file and applies case normalization for later use in text mining tasks
    :input: text; string containing text to be preprocessed
    :output: doc; string of preprocessed text
    '''

    #stop_words = STOP_WORDS

    # Make all text lowercase
    doc = text.lower() # lowercase
    
    # Remove punctuation.Used custom punctuation based on unicode instead of using method string.punctuation.
    # This is because the latter is ASCII, which doesn't include spanish punctuation sign ¡
    punctuation = "".join((chr(i) for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P')))
    doc = doc.translate(str.maketrans('', '', punctuation))  
    
    # Remove numbers
    doc = re.sub(r'\d+', '', doc)

    # Remove white space
    doc = doc.strip()

    # Remove mentions
    doc = re.sub(r"@\S+", "", doc)
    doc = re.sub(r'#\w+', '', doc)

    # Remove links
    doc = re.sub(r'http\S+', '', doc)
    
    # Remove b at the beginning of tweets
    doc = re.sub(r'^b', '', doc)

    # Remove hashtags
    doc = re.sub("#", "", doc)

    # Remove tickers
    doc = re.sub("\$", "", doc)

    # Remove stopwords
    #clean_text = " ".join([word for word in t8.split() if word not in stop_words])

    return doc

def tokenization(text):
    nlp = spacy.load('en_core_web_sm')
    print("Creating a text object with nlp")
    text = nlp(u'Google is looking at buying U.S. startup for $6 million')

    print("Printing each token separately")
    for token in text:
        print(token.text, token.pos_, token.dep_)


    print("Tokenization")
