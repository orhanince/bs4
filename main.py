import sys

import requests
from bs4 import BeautifulSoup

# Prompt from the terminal.
url = str(sys.argv[1])

# Define headers.
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 "
                  "Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}


def get_data(site_url):
    """
    Define parser function.
    :param site_url: Target link
    :type site_url: str
    :return: str
    """
    site = requests.get(site_url, headers=headers)
    site_content = BeautifulSoup(site.content, "lxml")
    product_title = site_content.find("h1", attrs={"class": "product-name"}).text.strip()
    return str(product_title)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_data(url)
