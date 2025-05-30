import yaml, os, json
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
    
@ensure_annotations
def create_directories(path_to_directory: list, verbose=True):
    """
        create a list of directories 
        Args:
            path_to_directories (list): list of path of directories
            verbose = True: print or log the detailed message
    """
    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
        saves JSON data
        Args:
            path: Path to json file
            data (dict): data which has to be saved into json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")