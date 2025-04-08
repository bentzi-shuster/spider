from spider.logs import logger
from spider.retriever import Retriever
import pandas as pd


class Spider():
    def __init__(self):
        logger.info('Spider instance created')
        self.csv_file = './companies_sorted.csv'

    def test(self):
        data = self.read_csv()
        retriever = Retriever()
        for name, domain in data:
            job_urls = retriever.retrieve(self.normalize_url(domain))
            # if the url starts with a slash '/', append the domain to it
            job_urls = [url if url.startswith(
                'http') else self.normalize_url(domain) + url for url in job_urls]
            logger.info('Job URLs for %s: %s' % (name, job_urls))

    def read_csv(self):
        """
        Read the CSV file containing the company names and domains and return the data
        """
        data = pd.read_csv(self.csv_file)
        data = data[['name', 'domain']].head(200).to_records(index=False)
        data = list(data)
        return data

    def normalize_url(self, url):
        """
        Normalize the URL to have a proper format
        ensure the URL starts with 'http://' or 'https' and if not, add it
        remove any trailing slashes, parameters, paths, etc.
        """
        return_url = url
        if not url.startswith('http'):
            return_url = 'https://' + url
        return_url = return_url.rstrip('/')  # remove trailing slashes
        return return_url
