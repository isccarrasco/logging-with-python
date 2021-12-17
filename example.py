import logging

logging.basicConfig(
        level=logging.DEBUG,
        filename='myexample.log',
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        )

logging.debug('This is an example')
logging.info('Info example')
logging.error('An error example')

