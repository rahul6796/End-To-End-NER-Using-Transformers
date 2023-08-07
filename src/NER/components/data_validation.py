import os
import pandas as pd
from src.NER.entity import DataValidationConfig
from src.NER.logging import logger


class DataValidation:

    def __init__(self,
                 config: DataValidationConfig):
        self.config = config

    def validate_all_files_exists(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            data.drop(['Unnamed: 4', 'Unnamed: 5'], axis=1, inplace=True)
            all_column = list(data.columns)
            schema_cols = self.config.all_schema.keys()
            for col in all_column:
                if col not in schema_cols:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"{validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"{validation_status}")
            return validation_status
        except Exception as ex:
            logger.error(f" invalid dataset :: {ex}")
