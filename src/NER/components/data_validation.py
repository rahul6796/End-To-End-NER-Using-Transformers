import os
import pandas as pd
from src.NER.entity import DataValidationConfig
from src.NER.logging import logger


class DataValidation:

    def __init__(self,
                 config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "conll2003"))

            for file in all_files:
                if file not in self.config.ALL_FILE_NAME:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"validation_status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"validation_status: {validation_status}")
            return validation_status
        except Exception as ex:
            raise ex
