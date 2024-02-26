#!/usr/bin/python

import pandas as pd
import re
import unicodedata
import string
import sklearn
import sys
from config import FILE, STOP_WORDS, BAG_OF_WORDS


def read_document(document:str) -> str: 
    '''
    Takes in the location of a .txt file, returns the contents of a .txt file into a string.
    :input: document; .txt file to be read
    :output: data; contents of the .txt file
    '''
    try:
        with open(document, 'r') as f:
            data = f.read()
        return data
      
    except IOError:
        print("Error opening or reading input file: ", document)
        sys.exit()


def reformatting(text:str) -> list:
    '''
    Reformats a text into documents and a corpus for later text mining use
    :input: text; full text in string type
    :output: document; each of the documents or "sentences" that the text has been divided onto
    :output: corpus; ensemble of documents in the corpus list object
    '''
    document = []
    corpus = []
    lines = text.splitlines() #  Here we consider different lines to be each of the documents, as we're dealing with tweets
    for line in lines:
        document.append(line)
    return corpus


def preprocessing() -> str:
    '''
    Preprocesses a .txt file and applies case normalization for later use in text mining tasks
    '''
    file = FILE
    raw_content = open(file, 'r', encoding="utf8").read()     # Added encoding to ensure spanish characters identified

    stop_words = STOP_WORDS

    # Make all text lowercase
    t1 = raw_content.lower() # lowercase
    
    # Remove punctuation.Used custom punctuation based on unicode instead of using method string.punctuation.
    # This is because the latter is ASCII, which doesn't include spanish punctuation sign ¡
    punctuation = "".join((chr(i) for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P')))
    t2 = t1.translate(str.maketrans('', '', punctuation))  
    
    # Remove numbers
    t3 = re.sub(r'\d+', '', t2)

    # Remove white space
    t4 = t3.strip()

    # Remove mentions
    t5 = re.sub("@\S+", "", t4)

    # Remove links
    t6 = re.sub("https?:\/\/.*[\r\n]*", "", t5)

    # Remove hashtags
    t7 = re.sub("#", "", t6)

    # Remove tickers
    t8 = re.sub("\$", "", t7)

    # Remove stopwords
    clean_text = " ".join([word for word in t8.split() if word not in stop_words])

    return clean_text

