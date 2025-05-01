from src.MentalHealth.config.configuration import ConfigurationManager
from src.MentalHealth.components.data_ingestion import DataIngestion
from src.MentalHealth import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.get_file_path()

if __name__ == "__main__":
    try:
        logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e