import os
from box.exceptions import BoxValueError
import yaml
from src.NER.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f'crating dir at :{path}')
    except Exception as ex:
        raise ex


@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} kb"


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    try:

        with open(path_to_yaml, 'r') as f:
            content = yaml.safe_load(f)
            logger.info(f'yaml file {path_to_yaml} is successfully loaded !! ')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml is empty !!")
    except Exception as ex:
        raise ex





