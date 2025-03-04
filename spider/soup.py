from bs4 import BeautifulSoup
from spider.logs import logger


def parse_html(html_doc):
    """
    Parse the HTML content using BeautifulSoup library, log the title of the page and return the soup object
    """
    soup = BeautifulSoup(html_doc, 'lxml')
    logger.info(soup.title.string)
    return soup
