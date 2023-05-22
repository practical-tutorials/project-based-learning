from bs4 import BeautifulSoup
import urllib3

# Getting user input
while True:
    year = input("Enter a year to search for: ")

    if len(year) == 4 and year.isdigit():
        break

    print("Year must be 4 digits long.")


# Sending a GET request to specified URL and getting the response as a HTTPResponse object
url = "https://www.imdb.com/search/title/?release_date=" + year
http = urllib3.PoolManager()
response = http.request('GET', url).data

# Parser
soup = BeautifulSoup(response, 'lxml')
# print(soup.prettify())
print(soup.find_all('title'))