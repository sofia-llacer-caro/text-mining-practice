#!/usr/bin/python

import pandas as pd
import re
import unicodedata
import string
import sklearn
import sys
from config import FILE, STOP_WORDS, BAG_OF_WORDS


def read_file(file:str) -> list: 
    '''
    Takes in the location of a .txt file, returns the contents of a .txt file into a string.
    Structures the contents into documents and a corpus
    :input: file; .txt file to be read
    :output: documents; list where each of the elements are the documents as extracted from the file
    '''
    try:
        with open(file, 'r', encoding="utf8") as f:
            documents = f.readlines()
            raw_corpus = [] # Initialize corpus
            for document in documents:
                raw_corpus.append(document.strip())
        return documents, raw_corpus
      
    except IOError:
        print("Error opening or reading input file: ", file)
        sys.exit()



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

