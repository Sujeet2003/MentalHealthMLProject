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