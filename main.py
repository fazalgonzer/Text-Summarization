from textSummarizer.logging import logger

from textSummarizer.pipeline.stage_01_data_ingestion import Data_ingestionTrainingPipeline



STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} Started <<<<<")
    obj=Data_ingestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME}  completed  <<<<<")

except Exception as e:
    logger.exception(e)
    raise e
