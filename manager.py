#THE IDEA IS TO MAKE A PREPROCESSING FUNCTION LIBRARY

#reading from text file with soup package
#create funciton that is preprocess(file) an it should do everything in the clearning thing


#!/usr/bin/python



import pandas as pd
import re
import string
import sklearn
from config import FILE, STOP_WORDS, BAG_OF_WORDS
# from bs4 import BeautifulSoup     # this library is giving problems

def preprocessing(file) -> str:
    '''
    Preprocesses a .txt file and applies case normalization for later use in text mining tasks
    :file: .txt file in directory /sample_texts relative to main.py
    '''
    file = FILE
    content = open(file, 'r', encoding="utf8") # Added encoding to ensure spanish characters identified

    stop_words = STOP_WORDS



    content.lower() # lowercase
    re.sub(r'\d+', '', content) # remove numbers
    content.translate(string.maketrans("",""), string.punctuation) # remove a set of punctuation symbols
    content = content.strip() # removes white space

    # removing stopwords
    text = " ".join([word for word in text.split() if word not in stop_words]) # stop_words to be made

    # Removing URLs, Hashtags, Punctuation, Mentions, etc

    # removing mentions

    text = "You should get @BlockFiZac from @BlockFi to talk about bitcoin lending, stablecoins, institution adoption, and the future of crypto"

    text = re.sub("@\S+", "", text)
    # remove tickers

    text = """#BITCOIN LOVES MARCH 13th A year ago the price of Bitcoin collapsed to $3,800 one of the lowest levels in the last 4 years. Today, exactly one year later it reaches the new all-time high of $60,000 Thank you Bitcoin for always making my birthday exciting"""

    text = re.sub("\$", "", text)
    print(text)

    #Output: #BITCOIN LOVES MARCH 13th A year ago the price of Bitcoin collapsed to  3,800 one of the lowest levels in the last 4 years. Today, exactly one year  later it reaches the new all-time high of 60,000 Thank you Bitcoin for  always making my birthday exciting

    # remove urls


    text = "Did someone just say “Feature Engineering”? https://buff.ly/3rRzL0s"

    text = re.sub("https?:\/\/.*[\r\n]*", "", text)
    print(text)

    # Output: Did someone just say “Feature Engineering”?

    # removing hashtags

    text = """.#FreedomofExpression which includes #FreedomToProtest should be the cornerstone of any democracy. I’m looking forward to speaking in the 2 day debate on the #PoliceCrackdownBill & explaining why I will be voting against it."""


    text = re.sub("#", "", text)
    print(text)


    #Output: FreedomofExpression which includes FreedomToProtest should be the  cornerstone of any democracy. I’m looking forward to speaking in the 2 day  debate on the PoliceCrackdownBill & explaining why I will be voting against it.






    return content