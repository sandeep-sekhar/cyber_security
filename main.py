from cybersecurity.components.data_ingestion import DataIngestion
from cybersecurity.components.data_validation import DataValidation
from cybersecurity.components.data_transformation import DataTransformation
from cybersecurity.components.model_trainer import ModelTrainer
from cybersecurity.exception.exception import cyberSecurityException
from cybersecurity.logging.logger import logging
import sys
from cybersecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from cybersecurity.entity.config_entity import TrainingPipelineConfig
if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion= DataIngestion(dataingestionconfig)
        logging.info("initiating the data_ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info('data ingestion done')
        print(dataingestionartifact)
        
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)
        
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info("data Transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")

        logging.info("Model Training sstared")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")
    except Exception as e:
        raise cyberSecurityException(e,sys)
