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

nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer


# 1. group by product
# 2. extract reviews.text, reviews.title
# 3. preprocess (remove stopwords)
# 4. extract sentiment
# 5. classify opinion
# 6. construct dataframe with product id, sentiment, opinion + [whatever we want to use later, n.reviews, doRecommend...]