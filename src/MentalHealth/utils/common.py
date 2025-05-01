import yaml
from src.MentalHealth import logger
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ 
        Reads yaml file and returs Box type
        Args:
            path_to_yaml (str): path like input
        Raises:
            ValueError: if yaml file is empty
            e: empty file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        logger.info(f"yaml file {path_to_yaml} is empty!")
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e