from dataclasses import dataclass
from pathlib import Path

# Data Ingestion Cofig
@dataclass(frozen=True)
class DataIngestionConfig:
    local_data_path: Path


# Data Validation Cofig
@dataclass(frozen=True)
class DataValidationConfig:
    local_data_path: Path
    schema_columns: dict
    target_columns: dict

# Data Transformation Config
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

# Model Trainer Config
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_path: str
    learning_rate: float
    n_estimators: int
    max_depth: int
    min_child_weight: int
    gamma: int
    subsample: float
    colsample_bytree: float
    reg_alpha: float
    objective: str
    nthread: int
    scale_pos_weight: int
    seed: int