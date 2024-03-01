#!/usr/bin/python

import pandas as pd
import numpy as np
import re
import unicodedata
from wordcloud import WordCloud
import string
import sklearn
import sklearn.feature_extraction
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import sys

from config import FILE, DOCS_TO_CLOUDS
from manager import read_file, preprocess

def main():
    file = FILE
    docs_to_clouds = DOCS_TO_CLOUDS

    # 1. Read data from file
    documents = read_file(file)
    
    # 2. Create corpus of document by using this data
    raw_corpus = [] # Initialize corpus
    for document in documents:
        raw_corpus.append(document.strip())

    # 3. Preprocess data for required clearning up to gain insight about data
        
    corpus = preprocess(raw_corpus)
    corpus = []
    for document in range(100): # Computational cost restraint
        a = preprocess(corpus[document])
        corpus.append(a)

    # 4. Represent document in matrix form
    vec = CountVectorizer()
    X = vec.fit_transform(corpus)
    df = pd.DataFrame(X.toarray(), columns = vec.get_feature_names_out())
        
    # 5. Find most relevant words from all documents
    bow = df.sum(axis=0).sort_values(ascending=False).head(15)
    
    # 6. Visualize word frequencies found in document term matrix using wordcloud
    for i in docs_to_clouds:
        wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(corpus[i])
        wordcloud.to_file(f"wordcloud_document{i}.png") 
    text_cloud = ' '.join(corpus)
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text_cloud)
    wordcloud.to_file("wordcloud_all.png")
    
    # 8. Find the most similar tweets from twitter data
    # source: https://www.newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
    csmat = cosine_similarity(X.toarray())
    np.fill_diagonal(csmat, -2)  
    simindex = np.unravel_index(np.argmax(csmat, axis=None), csmat.shape)
    
    return corpus, df, bow, simindex, corpus[simindex[0]], corpus[simindex[1]]

if __name__ == "__main__":
    print(main())