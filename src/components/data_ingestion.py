import os
import sys
from src.exception import CustomError
from src.loggin import logging

import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:

    train_data_path: str=os.path.join('artifact', "train.csv")
    test_data_path: str=os.path.join('artifact', "test.csv")
    raw_data_path: str=os.path.join('artifact', "raw.csv")

class DataIngestion:

    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            raw_data = pd.read_csv('notebooks/raw.csv')
            logging.info("Raw data read successfully")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            logging.info("Splitting the raw data into train and test data")
            train_data, test_data = train_test_split(raw_data, test_size=0.2, random_state=42)
            logging.info("Raw data split successfully")

            logging.info("Saving the train and test data")
            train_data.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False, header=True) 
            logging.info("Data ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            logging.error("Error occured while ingesting the data")
            raise CustomError(e, sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
