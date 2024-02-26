#!/usr/bin/python

from config import FILE
from manager import read_file, preprocess

def main():
    file = FILE

    # 1. Read twitter tweat data from file tweets.txt
    tweets = read_file(file)
    
    # 2. Create corpus of document by using this data
    corpus = [] # Initialize corpus
    for tweet in tweets:
        corpus.append(tweet.strip())

    # 3. Preprocess data for required clearning up to gain insight about data
    for document in range(len(corpus)):
        a = preprocess(corpus[document])
        print(a)
    #result = preprocess(corpus[5])


    # 4. Represent document in matrix form
    # 5. Find most relevant words from all documents
    # 6. Visualize word frequencies found in document term matrix using wordcloud
    # 7. What can we tell abotu tweets by looking at wordcloud?
    # 8. Find the most similar tweets from twitter data

    return 'result'

if __name__ == "__main__":
    print(main())