from src.MentalHealth.constants import *
from src.MentalHealth.entity.config_entity import DataIngestionConfig
from src.MentalHealth.utils.common import read_yaml


class ConfigurationManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH, params_file_path = PARAMS_FILE_PATH, schema_file_path = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_file_path)
        # self.params = read_yaml(params_file_path)
        # self.schema = read_yaml(schema_file_path)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        data_ingestion_config = DataIngestionConfig(
            local_data_path=config.local_data_path,
            validation_data_path=config.validation_data_path
        )
        return data_ingestion_config