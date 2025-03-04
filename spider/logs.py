import logging
LOG_FILENAME = 'spider.log'
logger = logging.getLogger(__name__)
logging.basicConfig(filename=LOG_FILENAME,
                    encoding='utf-8', level=logging.DEBUG)
# also logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)
# git config --global user.email "
# git config --global user.name "