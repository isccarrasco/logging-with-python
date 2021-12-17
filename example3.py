import logging.config

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)

logger = logging.getLogger(__name__)

logger.debug('Hello')
logger.info('Hello')
logger.error('Hello')