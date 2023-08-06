import os
from src.NER.config.configuration import ConfigurationManager
import zipfile
from src.NER.entity import DataIngestionConfig
import urllib.request as request
from src.NER.logging import logger


class DataIngestion:

    def __init__(self,
                 config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download following info  :: \ n{header}")
        else:
            logger.info(f'files already downloaded !')

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as f:
            f.extractall(unzip_path)


