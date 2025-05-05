from src.MentalHealth.constants import *
from src.MentalHealth.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig
from src.MentalHealth.utils.common import read_yaml
from src.MentalHealth import logger
from src.MentalHealth.utils.common import create_directories

class ConfigurationManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH, params_file_path = PARAMS_FILE_PATH, schema_file_path = SCHEMA_FILE_PATH):
        logger.info(f"Loading Config Yaml File...")
        try:
            logger.info(f"{config_file_path} file loaded successfully.")
            self.config = read_yaml(config_file_path)
        except Exception as e:
            logger.info(f"{self.config} file unable to load: Error as: {e}!")

        logger.info(f"Loading Params Yaml File...")
        try:
            logger.info(f"{params_file_path} file loaded successfully.")
            self.params = read_yaml(params_file_path)
        except Exception as e:
            logger.info(f"{self.params} file unable to load: Error as: {e}!")
        
        logger.info(f"Loading Schema Yaml File...")
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

        create_directories([config.root_dir])
        print(f"{config.root_dir} folder (directory) created successfully")

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path    
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.XGBoost

        create_directories([config.root_dir])
        print(f"{config.root_dir} folder (directory) created successfully")

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            model_path=config.model_path,
            learning_rate=params.learning_rate,
            n_estimators=params.n_estimators,
            max_depth=params.max_depth,
            min_child_weight=params.min_child_weight,
            gamma=params.gamma,
            subsample=params.subsample,
            colsample_bytree=params.colsample_bytree,
            reg_alpha=params.reg_alpha,
            objective=params.objective,
            nthread=params.nthread,
            scale_pos_weight=params.scale_pos_weight,
            seed=params.seed    
        )
        logger.info(f"All parameters from Yaml file loaded successfully for Model Training Configurations.")
        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([config.root_dir])
        print(f"{config.root_dir} folder (directory) created successfully")

        model_evalution_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            metrics_file_path=config.metrics_file_path    
        )
        logger.info(f"All parameters from Yaml file loaded successfully for Model Evaluation Configurations.")
        return model_evalution_config