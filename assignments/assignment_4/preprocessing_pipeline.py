import warnings
warnings.simplefilter(action='ignore') # Due to method depracated in future versions, makes results more legible

import nltk
import pandas as pd 
import numpy as np

nltk.download('vader_lexicon')

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


# 6. Season sales analysis
winter = []
query = list(products)
raw_df_product = pd.DataFrame(raw_df)
months = [11, 12, 1, 2]

for i in range(len(raw_df)):

    datetime_str = raw_df['dateAdded'][i]
    datetime_obj = pd.to_datetime(datetime_str)
    month_purchase = datetime_obj.month

    if month_purchase in months:
        raw_df.loc[i, "Winter"] = 1
    else:
        raw_df.loc[i, "Winter"] = 0
    

for i in range(len(products)):
    query[i] = f"id=='{products[i]}'"
    raw_df_product = raw_df.query(query[i])
    winter_df = raw_df_product[raw_df_product["Winter"] == 1]["Winter"].count()
    winter.append(winter_df)

winter_per = []
for i in range(len(products)):
    # Relative occurence
    percent_winter = winter[i]/rating_count[i]
    # Add to main dataframe
    winter_per.append(percent_winter)
df['percent_winter'] = winter_per


# Add the product name for clarity in the data for analysis
unique_product_names = raw_df['name'].unique()
df['product_name'] = unique_product_names

# Export to .csv
df.to_csv('preprocessed_data.csv', index=False)
