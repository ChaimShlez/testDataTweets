import pandas as pd

from src.manager_analyzer import Manager_analyzer
from src.manager_cleaner import Manager_cleaner


class Main:
    def __init__(self):
        self.data=self.data_loader()
        self.data_copy=self.data.copy()
        self.analyzer=Manager_analyzer(self.data)
        self.cleaner=Manager_cleaner(self.data_copy)


    def data_loader(self):
        df_data=pd.read_csv("data/tweets_dataset.csv")

        return df_data



if __name__ == "__main__":
    main = Main()