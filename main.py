
from src.NER.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.NER.pipeline.data_validation_pipeline import DataValidationPipeline
from src.NER.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.NER.logging import logger
START = "data_ingestion_pipeline"

try:
    logger.info(f'{START}')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
except Exception as ex:
    print(ex)


START = "data_validation_pipeline"

try:
    logger.info(f'{START}')
    data_validation = DataValidationPipeline()
    data_validation.main()
except Exception as ex:
    print(ex)


# START = "data_transformation_pipeline"
#
# try:
#     logger.info(f'{START}')
#     data_transformation = DataTransformationPipeline()
#     data_transformation.main()
# except Exception as ex:
#     print(ex)
