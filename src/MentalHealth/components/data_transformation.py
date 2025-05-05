from src.MentalHealth.entity.config_entity import DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split
import os
from src.MentalHealth import logger



class DataTransformation:
    def __init__(self, config=DataTransformationConfig):
        self.config = config

    def split_data(self) -> None:
        df = pd.read_csv(self.config.data_path)
        train, test = train_test_split(df)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info(f"Data splitted into train and test part.")
        logger.info(f"Train dataset Shape: {train.shape} and Test Dataset Shape: {test.shape}")
        print(train.shape, test.shape)