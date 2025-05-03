from src.MentalHealth.entity.config_entity import DataIngestionConfig
from src.MentalHealth import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def get_file_path(self):
        logger.info(f"Datasets file path are as: {self.config.local_data_path}")
        print(f"{self.config.local_data_path}")