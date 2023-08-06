
from src.NER.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.NER.logging import logger
START = "data_ingestion_pipeline"

try:
    logger.info(f'{START}')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
except Exception as ex:
    print(ex)