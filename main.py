from cybersecurity.components.data_ingestion import DataIngestion
from cybersecurity.exception.exception import cyberSecurityException
from cybersecurity.logging.logger import logging
import sys
from cybersecurity.entity.config_entity import DataIngestionConfig
from cybersecurity.entity.config_entity import TrainingPipelineConfig
if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion= DataIngestion(dataingestionconfig)
        logging.info("initiating the data_ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        raise cyberSecurityException(e,sys)
