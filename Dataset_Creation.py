from datasets import load_dataset
import pandas as pd
import re
dataset_names = [
                 'raw_review_Grocery_and_Gourmet_Food', 
                 'raw_review_Sports_and_Outdoors', 
                 'raw_review_Home_and_Kitchen', 
                 'raw_review_Subscription_Boxes', 
                 'raw_review_Tools_and_Home_Improvement', 
                 'raw_review_Pet_Supplies', 
                 'raw_review_Video_Games', 
                 'raw_review_Kindle_Store', 
                 'raw_review_Clothing_Shoes_and_Jewelry', 
                 'raw_review_Patio_Lawn_and_Garden', 
                 'raw_review_Unknown', 
                 'raw_review_Books', 
                 'raw_review_Automotive', 
                 'raw_review_CDs_and_Vinyl', 
                 'raw_review_Beauty_and_Personal_Care', 
                 'raw_review_Amazon_Fashion', 
                 'raw_review_Magazine_Subscriptions', 
                 'raw_review_Software', 
                 'raw_review_Health_and_Personal_Care', 
                 'raw_review_Appliances', 
                 'raw_review_Movies_and_TV']



# Initialize an empty list to store DataFrames
dfs = []

for name in dataset_names:
    df = pd.DataFrame(load_dataset("McAuley-Lab/Amazon-Reviews-2023", name, trust_remote_code=True, split="full[:500000]"))
    df.to_csv(name+'.csv', index=False)


