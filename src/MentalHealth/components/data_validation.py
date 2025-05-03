# from src.MentalHealth import logger
import pandas as pd
from src.MentalHealth import logger
from src.MentalHealth.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config=DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True
            df = pd.read_csv(self.config.local_data_path)

            all_columns = list(df.columns)
            schema_columns = list(self.config.schema_columns.keys())
            target_columns = list(self.config.target_columns.keys())
            all_schema_cols = schema_columns + target_columns
            

            for column in all_columns:
                if column not in all_schema_cols:
                    validation_status = False
                    logger.info(f"{column} not found in schema, may be mismatched to dataset columns or in 'schema.yaml' file columns assigned.")
            return validation_status
        except Exception as e:
            logger.info(f"Found error with data validation as: {e}")
            raise e