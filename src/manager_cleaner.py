from src.cleaner_data import Cleaner_data

class Manager_cleaner:


    def __init__(self,data):
        self.data=data
        self.cleaner=Cleaner_data(self.data)

        self.save_to_csv()

    def save_to_csv(self):
        new_data = self.cleaner.data
        new_data.to_csv("results/tweets_data_clean.csv", index=False)



