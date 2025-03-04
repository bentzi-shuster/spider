from spider.logs import logger
from spider.retriever import Retriever


class Spider():
    def __init__(self):
        logger.info('Spider instance created')

    def test(self):
        retriever = Retriever()
        logger.info(retriever.retrieve('https://www.verizon.com/'))
        logger.info(retriever.retrieve('https://www.att.com/'))
        logger.info(retriever.retrieve('https://www.t-mobile.com/'))
        logger.info(retriever.retrieve('https://www.sprint.com/'))
