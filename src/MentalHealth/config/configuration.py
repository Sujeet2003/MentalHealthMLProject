from src.MentalHealth.constants import *
from src.MentalHealth.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from src.MentalHealth.utils.common import read_yaml
from src.MentalHealth import logger
from src.MentalHealth.utils.common import create_directories

class ConfigurationManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH, params_file_path = PARAMS_FILE_PATH, schema_file_path = SCHEMA_FILE_PATH):
        try:
            logger.info(f"{config_file_path} file loaded successfully.")
            self.config = read_yaml(config_file_path)
        except Exception as e:
            logger.info(f"{self.config} file unable to load: Error as: {e}!")
        # self.params = read_yaml(params_file_path)
        try:
            logger.info(f"{schema_file_path} file loaded successfully.")
            self.schema = read_yaml(schema_file_path)
        except Exception as e:
            logger.info(f"{self.schema} file unable to load: Error as: {e}!")

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        data_ingestion_config = DataIngestionConfig(
            local_data_path=config.local_data_path,
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        data_validation_config = DataValidationConfig(
            local_data_path=config.local_data_path,
            schema_columns=self.schema.COLUMNS,
            target_columns=self.schema.TARGET_COLUMNS
        )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        # create_directories([config.root_dir])
        # print(f"{config.root_dir} folder (directory) created successfully")

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path    
        )
        return data_transformation_config