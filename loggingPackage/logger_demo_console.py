import logging

class LoggerDemoConsole():
    
    def testLog(self):
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                              datefmt='%m/%d/%Y %I:%M:%S %p')

        consoleHandler.setFormatter(formatter)
        logger.addHandler(consoleHandler)

        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')


demo = LoggerDemoConsole()
demo.testLog()


