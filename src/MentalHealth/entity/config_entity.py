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