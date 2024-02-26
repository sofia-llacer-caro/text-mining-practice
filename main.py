#!/usr/bin/python

from config import FILE
from manager import *

def main():
    file = FILE

    # 1. Read twitter teat data from file tweets.txt
    text = read(file)

    # 2. Create corpus of document by using this data
    corpus = into_corpus(text)
    # 3. Preprocess data for required clearning up to gain insight about data
    # 4. Represent document di in matrix form
    # 5. Find most relevant words from all documents
    # 6. Visualize word frequencies found in document term matrix using wordcloud
    # 7. What can we tell abotu tweets by looking at wordcloud?
    # 8. Find the most similar tweets from twitter data

    result = ""
    return result

if __name__ == "__main__":
    print(main())