#THE IDEA IS TO MAKE A PREPROCESSING FUNCTION LIBRARY

#reading from text file with soup package
#create funciton that is preprocess(file) an it should do everything in the clearning thing


#!/usr/bin/python



import pandas as pd
import re
import unicodedata
import string
import sklearn
import sys
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import textmining

from config import FILE, STOP_WORDS, BAG_OF_WORDS
# from bs4 import BeautifulSoup     # this library is giving me problems

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


def visualize(text):
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

