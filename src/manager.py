import  pandas as pd
from src.analyzer_data import Analyzer_data
class Manager:

    def __init__(self):

        self.data=self.data_loader()
        self.analyzer = Analyzer_data(self.data)




    def data_loader(self):
        df_data=pd.read_csv("data/tweets_dataset.csv")



        return df_data


