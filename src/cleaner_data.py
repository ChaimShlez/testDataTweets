import pandas as pd

class Cleaner_data:

    def __init__(self,data):
        self.data=data
        self.save_columns()
        self.clean_data()
        self.update_to_lower_case()
        self.drop_data_without_calcification()


    def save_columns(self):
        self.data=self.data.drop(["TweetID","Username","CreateDate","Keyword","Word_Count"], axis='columns')
        # print(self.data)


    def clean_data(self):
        self.data["Text"]= self.data["Text"].replace("," ," ")
        # print(self.data)
        # return data_clean

    def update_to_lower_case(self):
        self.data["Text"]=self.data["Text"].str.lower()
        print(self.data)

    def drop_data_without_calcification(self):
        mask=self.data["Biased"].isin([0,1])
        self.data=self.data[mask]
        print(self.data)







