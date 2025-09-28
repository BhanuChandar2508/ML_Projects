import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass #used to create class variables


# While working with Data Ingestion there should be an input for it like where should save train , test and raw data:
#with this dataclass decorator we can directly define the class variable
#inside a class , to define a class variable we use __init__ in general
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv') # path and filename...
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','raw_data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

#this data ingestion function is used to read the data of dataset which is stored in the DataBase
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method or component is Started")

        try:
            file_path='NoteBook\Data\stud.csv'
            df=pd.read_csv(filepath_or_buffer=file_path)
            logging.info(f'Read The DataSet from "{file_path}" file as DataFrame, It has [{df.shape[0]}] records')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test Split is Initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the Data is Completed by Train Test Split")
            logging.info( f"Train Test Split is completed and Created the {self.ingestion_config.train_data_path} and {self.ingestion_config.test_data_path} files" )

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_data_ingestion()
