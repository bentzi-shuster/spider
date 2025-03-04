from spider.logs import logger


class Extractor:
    def __init__(self, url):
        logger.info('Retrieve instance created')
        self.url = url
