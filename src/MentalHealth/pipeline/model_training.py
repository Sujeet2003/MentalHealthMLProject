from src.MentalHealth.components.model_trainer import ModelTrainer
from src.MentalHealth.config.configuration import ConfigurationManager
from src.MentalHealth import logger


STAGE_NAME = "Model Training Pipeline"
class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train_model()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e