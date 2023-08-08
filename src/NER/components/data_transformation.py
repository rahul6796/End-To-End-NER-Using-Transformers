import pandas as pd
from transformers import AutoTokenizer

from src.NER.config.configuration import DataTransformationConfig
from sklearn.model_selection import train_test_split
import os
from src.NER.logging import logger


class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def train_test_splits(self):
        data = pd.read_csv(self.config.data_path)
        x_train, x_test = train_test_split(data, test_size=0.2)
        x_train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        x_test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        logger.info("spliting data into train and test set !!")






