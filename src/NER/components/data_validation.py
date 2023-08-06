import os

from src.NER.entity import DataValidationConfig
from src.NER.logging import logger


class DataValidation:

    def __init__(self,
                 config: DataValidationConfig):
        self.config = config

    def validate_all_files_exists(self) -> bool:
        try:
            validate_status = None
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "conll2003"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validate_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"{validate_status}")
                else:
                    validate_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"{validate_status}")
            return validate_status
        except Exception as ex:
            raise ex

