from src.MentalHealth.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def get_file_path(self):
        print(self.config.local_data_path, "\n", self.config.validation_data_path)