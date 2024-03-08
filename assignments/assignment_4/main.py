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

import warnings

warnings.simplefilter(action='ignore') # Due to method depracated in future versions, makes results more legible


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
    'num_ratings': np.zeros(len(products)),
    'percent_neg': np.zeros(len(products)),
    'percent_pos': np.zeros(len(products)),
    'percent_neu': np.zeros(len(products))
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

rating_count = [] # Initialize
query = list(products)
raw_df_product = pd.DataFrame(raw_df)

for i in range(len(products)):
    query[i] = f"id=='{products[i]}'"
    raw_df_product = raw_df.query(query[i])
    rating_count_df = raw_df_product["reviews.rating"].count()
    rating_count.append(rating_count_df)

df['num_ratings'] = rating_count



# 4. "Do Recommend" Score: we wanted to add and has potential but that field is not filled up in the raw data



# 5. Sentiment Analysis

def opinion(text):
    vader_analyzer = SentimentIntensityAnalyzer()
    output =vader_analyzer.polarity_scores(text)

    if output['neg']>0.3:
        return 0#,output['neg']
    elif  output['pos']>0.3:
        return 1#,output['pos']
    return 2#,output['neu']

# Usage
'''
for i in range(len(products)):
    review_sent = []
    query[i] = f"id=='{products[i]}'"
    raw_df_product = raw_df.query(query[i])
    for j in range(rating_count[i]): # Evaluate each review individually and obtain its sentiment key
        sent = opinion(raw_df["reviews.text"][j])
        review_sent.append(sent)
    review_df = pd.DataFrame({'review_score': review_sent})
    
    # Absolute count of reviews
    num_neg_rev = review_df[review_df['review_score'] == 0].count()
    num_pos_rev = review_df[review_df['review_score'] == 1].count()
    num_neu_rev = review_df[review_df['review_score'] == 2].count()
    # Relative occurences
    percent_neg = num_neg_rev/rating_count[i]
    percent_pos = num_pos_rev/rating_count[i]
    percent_neu = num_neu_rev/rating_count[i]
    # Add to main dataframe
    df['percent_neg'][i] = percent_neg
    df['percent_pos'][i] = percent_pos
    df['percent_neu'][i] = percent_neu



print(df)
'''

# 6. Season sales analysis
winter_count = [] # Initialize
query = list(products)
raw_df_product = pd.DataFrame(raw_df)
months = [10, 12, 1, 2]

# WORKS WITH OCTOBER BUT NOT IF OCTOBER IS NOT INCLUDED

for i in range(len(products)):
    counter = 0
    for j in range(rating_count[i]):
        
        datetime_str = raw_df_product['dateAdded'][i]
        datetime_obj = pd.to_datetime(datetime_str)
        month_purchase = datetime_obj.month
            
        if month_purchase in months:
            counter+=1
        else:
            pass
    winter_count.append(counter)

print(winter_count)













# 2. extract reviews.text, reviews.title
# 3. preprocess (remove stopwords)
# 4. extract sentiment
# 5. classify opinion
# 6. construct dataframe with product id, sentiment, opinion + [whatever we want to use later, n.reviews, doRecommend...]