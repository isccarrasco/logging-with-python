import logging


# logging.basicConfig(
#         level=logging.DEBUG,
#         filename='myexample.log',
#         format='%(asctime)s %(name)s %(filename)s:%(lineno)d %(levelname)s %(message)s',
#         )

logger = logging.getLogger(__name__)


def method_1():

    logger.info('Hello from parent')
    logger.debug('debug  from parent')
    logger.error('error  from parent')

    return True