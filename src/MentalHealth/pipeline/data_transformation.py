from src.MentalHealth.components.data_transformation import DataTransformation
from src.MentalHealth import logger
from src.MentalHealth.config.configuration import ConfigurationManager



class DataTransfomrmationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        status = True
        try:
            if status:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.split_data()
                logger.info(f"Training Pipeline done for data transformation.")
            else:
                logger.info(f"Data Splitter failed during data transformation")
                raise Exception(f"Data Splitter failed during data transformation")
        except Exception as e:
            logger.info(f"Data Splitter failed during data transformation: {e}")
            raise Exception(f"Data Splitter failed during data transformation: {e}")