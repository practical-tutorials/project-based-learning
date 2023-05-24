from bs4 import BeautifulSoup
from urllib.request import urlopen

DEFAULT_YEAR = 2017

# Getting user input
while True:
    year = input("Enter a year to search for: ")

    if year == '':
        year = str(DEFAULT_YEAR)
        print("Setting default year to {}...".format(year))

    if len(year) == 4 and year.isdigit():
        break

    print("Year must be 4 digits long.")


# Sending a GET request to specified URL and getting the response as a HTTPResponse object
url = "https://www.imdb.com/search/title/?release_date=" + year
http_response = urlopen(url)
markup = http_response.read()

# Parser
soup = BeautifulSoup(markup, 'lxml')
print(soup.prettify())
# print(soup.find_all('title'))