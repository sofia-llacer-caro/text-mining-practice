# Which products should be kept?
# Which products should be dropped? --> THRESHOLD!
# Which products are junk? (lot of reviews and all a bad, decline in buying in time)
# Which product should be recommended to customer? (good reviews, good rating, lot of rating, doRecommend)
# Which consumer products are the best products? (Best rating, most ratings, text reviews good sentiment)
# Which products should be planned for inventory for coming winter? (Good reviews and more buying during winter)
# Which products require advertisment? (Little reviews, good ratings, would recommend)
# In list of opinion O how many quintuples have positive sentiment s?

# ----------------------------
# do sentiment analysis: reviews.text,reviews.title

# Polarity classification - Opinion Mining - Sentiment Analysis

import nltk
import pandas as pd 
import numpy as np

#nltk.download('vader_lexicon') #UNCOMMENT WHEN UPLOAD

from nltk.sentiment.vader import SentimentIntensityAnalyzer


# 1. Group by product

raw_df = pd.read_csv("reviews.csv")
products = pd.unique(raw_df["id"]) # See how many different products there are, which is 65

contents = {
    'product': products,
    'avg_rating': np.zeros(len(products)),
    'num_ratings': np.zeros(len(products))
}

df = pd.DataFrame(contents) # Create final df for later analysis



# 2. Calculate average rating per product

mean = [] # Initialize
query = list(products)
raw_df_product = pd.DataFrame(raw_df)

for i in range(len(products)):
    query[i] = f"id=='{products[i]}'"
    raw_df_product = raw_df.query(query[i])
    mean_df = raw_df_product["reviews.rating"].mean()
    mean.append(mean_df)

df['avg_rating'] = mean


# 3. Count Number of ratings



# 4. "Do Recommend" Score


# 5. Sentiment Analysis










# 2. extract reviews.text, reviews.title
# 3. preprocess (remove stopwords)
# 4. extract sentiment
# 5. classify opinion
# 6. construct dataframe with product id, sentiment, opinion + [whatever we want to use later, n.reviews, doRecommend...]