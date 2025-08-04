from collections import Counter

import pandas as pd
class Analyzer_data:

    def __init__(self,data_df):
        self.data=data_df
        self.unique_category=self.extract_unique_categorys()
        self.dict_category=self.check_amount_tweets_from_category()
        self.sum_chars_by_unique_name()
        self.dict_three_longest=self.Three_longest_tweets_for_category()
        self.ten_words=self.ten_most_common_words()
        self.amount_upper_case=self.amount_upper_case()


    def extract_unique_categorys(self):
        unique_data = self.data['Biased'].unique()
        return unique_data



#extracts the value names because I don't know what "undefined" will be, and then lists the quantity by value.
    def check_amount_tweets_from_category(self):
              dict_category={}
              for val in  self.unique_category:
                  count = (self.data['Biased'] == val).sum()
                  dict_category[val]=count
                  return dict_category

    def sum_chars_by_unique_name(self):

        self.data['Word_Count'] = self.data['Text'].str.len()
        dict_sum_words= self.data.groupby('Biased')['Word_Count'].mean().to_dict()
        dict_sum_words['all'] =self.data['Word_Count'].mean()
        return dict_sum_words


    def Three_longest_tweets_for_category(self):
        dict_three_longest = {}
        for val in self.unique_category:
            top3 = self.data[self.data['Biased'] == val].nlargest(3, 'Word_Count')
            dict_three_longest[val] = top3
            return dict_three_longest

    def ten_most_common_words(self):

        all_words = ' '.join(self.data['Text']).split()
        word_counts = Counter(all_words)
        ten_words = [word for  word ,count in word_counts.most_common(10)]
        return ten_words

    def amount_upper_case(self):
        words_by_category = self.data.groupby('Biased')["Text"].apply(' '.join)
        words_by_category = words_by_category.apply(lambda x: x.split())
        for category,words in words_by_category.items():

            amount_upper_case= sum(1 for word in words if word.isupper())
            return amount_upper_case





