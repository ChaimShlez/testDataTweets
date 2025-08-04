import pandas as pd
class Analyzer_data:

    def __init__(self,data_df):
        self.data=data_df
        self.check_amount_tweets_from_category()

    def check_amount_tweets_from_category(self):
              dict_category={}
              unique_data=self.data['Biased'].unique()
              for val in  unique_data:
                  count = (self.data['Biased'] == val).sum()
                  # print(f"Category {val}: {count} tweets")
                  dict_category[val]=count
                  return dict_category



