from src.MentalHealth import logger
from src.MentalHealth.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.MentalHealth.pipeline.data_validation import DataValidationTrainingPipeline



STAGE_NAME = "Data Ingestion Pipeline"
try:
    logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data validation Pipeline"
try:
    logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e