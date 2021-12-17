import logging


logging.basicConfig(
        level=logging.DEBUG,
        filename='myexample.log',
        format='%(asctime)s %(name)s %(filename)s:%(lineno)d %(levelname)s %(message)s',
        )

logger = logging.getLogger(__name__)

logger.debug('Another example')
logger.info('Another info example')
logger.error('Another error example')

from child import method_2

method_2()