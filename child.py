import logging

# This is required if you want to run the module as main
#
# logging.basicConfig(
#         level=logging.DEBUG,
#         filename='myexample.log',
#         format='%(asctime)s %(name)s %(filename)s:%(lineno)d %(levelname)s %(message)s',
#         )

logger = logging.getLogger(__name__)

from parent import method_1

def method_2():

    method_1()

    logger.info('Hello from child')
    logger.debug('debug  from child')
    logger.error('error  from child')

    return True
