import os
from src.NER.logging import logger
from src.NER.entity import DataIngestionConfig, DataValidationConfig
from src.NER.utils.common import read_yaml, create_directories
from src.NER.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH


class ConfigurationManager:

    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 param_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
        self.config_yaml = read_yaml(config_filepath)
        self.params_yaml = read_yaml(param_filepath)
        self.schema_yaml = read_yaml(schema_filepath)
        create_directories([self.config_yaml.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config_yaml.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config_yaml.data_validation
        all_columns = self.schema_yaml.COLUMNS
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=all_columns
        )

        return data_validation_config


