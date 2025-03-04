from spider.logs import logger


class Analyzer:
    def __init__(self, url):
        logger.info('Analyzer instance created')
        self.url = url
