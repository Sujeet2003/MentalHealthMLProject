from src.MentalHealth import logger
from src.MentalHealth.components.model_evaluation import ModelEvaluation
from src.MentalHealth.config.configuration import ConfigurationManager



STAGE_NAME = "Model Evaluation Training Pipeline"
class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self) -> None:
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evalaution = ModelEvaluation(model_evaluation_config)
        model_evalaution.evaluate_model()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<\n")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<<\n")
    except Exception as e:
        logger.exception(e)
        raise e