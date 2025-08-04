import json

import  pandas as pd
from src.analyzer_data import Analyzer_data
from src.cleaner_data import Cleaner_data





class Manager_analyzer:

    def __init__(self,data):

        self.data=data
        self.analyzer = Analyzer_data(self.data)
        self.dict_from_json=self.create_dict_from_json()
        self.save_to_json()




    def create_dict_from_json(self):
        dict_data_analyzer={}
        dict_data_analyzer["total_tweets_for_category"]=self.analyzer.dict_category
        dict_data_analyzer["amount_average_length_in_words"]=self.analyzer.dict_average_words
        dict_data_analyzer["longest_three_tweets"]=self.analyzer.dict_three_longest
        dict_data_analyzer["ten_most_common_words"]=self.analyzer.ten_words
        dict_data_analyzer["amount_upper_case"]=self.analyzer.dict_upper_case
        return dict_data_analyzer



    def save_to_json(self):
        print(self.dict_from_json)
        with open("results/data_analyzer.json","w")as f:
            json.dump(self.dict_from_json, f, ensure_ascii=False, indent=4)













