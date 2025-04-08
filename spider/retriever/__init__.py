from spider.logs import logger
import re
from spider.soup import parse_html
from playwright.sync_api import sync_playwright
import urllib.robotparser


class Retriever():
    """
    Retriever class to retrieve the HTML content of the URL, parse it and find job links
    """

    def __init__(self):
        """
        Initialize the Retriever instance and setup the playwright browser instance
        """
        logger.info('Retriever instance created')
        self.browser = self.setup_playwright()
        self.job_link_keywords = ['job', 'career',
                                  'vacancy', 'opening', 'position', 'recruitment', 'hire', 'employment', 'opportunity']

    def setup_playwright(self):
        """
        Setup the playwright browser instance
        """
        playwright_instance = sync_playwright().start()
        browser = playwright_instance.chromium.launch()  # headless=False)
        playwright_instance.chromium.launch(args=["--disable-http2"])
        browser.new_context(
            ignore_https_errors=True,
            user_agent='msnbot', bypass_csp=True)
        return browser

    def pull_url(self, url):
        """
        Pull the HTML content of the URL using playwright library
        this is extra slow because of JavaScript execution being fucky
        """
        page = self.browser.new_page()
        try:
            page.goto(url=url, wait_until='load')
        except:
            logger.error('Error loading URL: %s' % url)
            return None

        page.set_extra_http_headers({'Upgrade-Insecure-Requests': '1'})
        # make sure the page is fully loaded and javascript is executed
        page.wait_for_load_state('load')
        # wait for 2 seconds to make sure all the content is loaded
        page.wait_for_timeout(2000)
        content = page.content()
        page.close()
        return content

    def parse_html_data(self, html_text, url):
        """
        Parse the HTML content of the URL using BeautifulSoup library
        """
        logger.info('Parsing URL content for %s' % url)
        parsed_html_value = parse_html(html_text)
        return parsed_html_value

    def find_job_links(self, parsed_html, url):
        """
        Find all the job links in the parsed HTML using keywords like 'job', 'career', 'vacancy', etc.
        """
        logger.info('Finding job links for %s' % url)
        job_links = []
        # find all the anchor tags in the HTML with a href attribute and with a text that contains the keywords or a similar variation
        for link in parsed_html.find_all('a', href=True, text=re.compile(r'(%s)' % '|'.join(self.job_link_keywords), re.IGNORECASE)):
            logger.info('Found job link: %s on %s' % (link['href'], url))
            job_links.append(link['href'])
        return job_links

    def robt_txt_check(self, url):
        """
        Check the robots.txt file of the domain to see if the URL is allowed to be scraped
        """
        rp = urllib.robotparser.RobotFileParser()
        page = self.browser.new_page()
        page.goto(url + '/robots.txt')
        # get the content of the robots.txt file
        robots_txt = page.content()
        rp.parse(robots_txt)
        if not rp.can_fetch('*', url):
            logger.error('URL %s is not allowed to be scraped' % url)
            return False
        return True  # check

    def retrieve(self, url):
        """
        Retrieve the HTML content of the URL, parse it and find job links
        """
        if not self.robt_txt_check(url):
            return []
        html_content = self.pull_url(url)
        if not html_content:
            return []
        parsed_html = self.parse_html_data(html_content, url)
        if not parsed_html:
            return []
        job_links = self.find_job_links(parsed_html, url)
        return job_links
