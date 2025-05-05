from src.MentalHealth.entity.config_entity import ModelTrainerConfig
import joblib, os
import pandas as pd
from xgboost.sklearn import XGBClassifier
from src.MentalHealth import logger


class ModelTrainer:
    def __init__(self, config=ModelTrainerConfig):
        self.config = config

    def train_model(self) -> None:
        train_data = pd.read_csv(self.config.train_data_path)
        logger.info(f"Trianing dataset loaded successfully.")

        X_train = train_data.drop(columns=['Depression'])
        y_train = train_data.Depression
        logger.info(f"Data ready for training with X_train and y_train (target).")

        model = XGBClassifier(
            learning_rate=self.config.learning_rate,
            n_estimators=self.config.n_estimators,
            max_depth=self.config.max_depth,
            min_child_weight=self.config.min_child_weight,
            gamma=self.config.gamma,
            subsample=self.config.subsample,
            colsample_bytree=self.config.colsample_bytree,
            reg_alpha=self.config.reg_alpha,
            objective=self.config.objective,
            nthread=self.config.nthread,
            scale_pos_weight=self.config.scale_pos_weight,
            seed=self.config.seed
        )
        model.fit(X_train, y_train)
        logger.info(f"Model fitted successfully.")
        
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_path))
        logger.info(f"Model dumped successfully as: {self.config.model_path}")