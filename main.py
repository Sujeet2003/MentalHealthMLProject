from src.MentalHealth import logger
from src.MentalHealth.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.MentalHealth.pipeline.data_validation import DataValidationTrainingPipeline
from src.MentalHealth.pipeline.data_transformation import DataTransfomrmationTrainingPipeline
from src.MentalHealth.pipeline.model_training import ModelTrainingPipeline
from src.MentalHealth.pipeline.model_evaluation import ModelEvaluationPipeline



STAGE_NAME = "Data Ingestion Pipeline"
try:
    logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Pipeline"
try:
    logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Pipeline"
try:
    logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
    obj = DataTransfomrmationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Pipeline"
try:
    logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evalaution Pipeline"
try:
    logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e