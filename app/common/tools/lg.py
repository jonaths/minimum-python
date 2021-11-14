import logging
from logging.handlers import TimedRotatingFileHandler
import os


class Logger:

    def __init__(self, name='log', log_level='DEBUG', stage='local', log_dir='logs'):
        """
        Configura un logger que cambia cada día
        :param name: el nombre del logger
        :param log_level: DEBUG por ejemplo
        :param stage: el stage del proyecto (local)
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        # create file handler which logs even debug messages
        fh = TimedRotatingFileHandler(os.path.join(log_dir, stage + '_'), when='midnight', interval=1)
        fh.suffix = "%Y%m%d.log"
        fh.setLevel(logging.DEBUG)

        os.path.join(log_dir, stage + '_')

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(name)-6s %(asctime)s %(levelname)-6s thread:%(thread)-8d - %(message)s')
        fh.setFormatter(formatter)

        # add the handler to the logger
        self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger
