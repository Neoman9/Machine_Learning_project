from housing_1.config_1.configration import configration
from housing_1.logger import logging 
from housing_1.exception import HousingException

from housing_1.entity.artifact_entity import DataIngestionArtifact
from housing_1.entity.config_entity import DataIngestionConfig
from housing_1.component.data_ingestion import DataIngestion
import os,sys


class Pipeline:

    def __init__(self,config_1:configration=configration()) ->None:
        try:
            self.config_1=config_1

        except Exception as e:
            raise HousingException(e,sys) from e
        
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def start_data_validation(self):
        pass

    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass
        

    def run_pipeline(self):
        try:
            #data ingestion
            data_ingestion_artifact=  self.start_data_ingestion()


        except Exception as e :
            raise HousingException(e,sys) from e
        