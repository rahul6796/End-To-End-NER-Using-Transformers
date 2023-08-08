import os
from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_FILE_NAME: list


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: str
    tokenizer_name: str


