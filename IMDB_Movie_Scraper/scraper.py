from bs4 import BeautifulSoup
from urllib.request import urlopen

BASE_URL = 'https://www.imdb.com'
DEFAULT_YEAR = 2017

# Getting user input
while True:
    year = input("Enter a year to search for: ")

    if year == '':
        year = str(DEFAULT_YEAR)
        print("Setting default year to {}...".format(year))
        break

    if len(year) == 4 and year.isdigit():
        break

    print("Year must be 4 digits long.")


# Sending a GET request to specified URL and getting the response as a HTTPResponse object
url = BASE_URL + "/search/title/?release_date=" + year
http_response = urlopen(url)
markup = http_response.read()

# Parser
soup = BeautifulSoup(markup, 'lxml')
movie_list = soup.find_all('div', class_='lister-item mode-advanced')

def get_movie_info(movie):
    return {
        'title': movie.find('h3', class_='lister-item-header').a.text,
        'rating': movie.find('div', class_='inline-block ratings-imdb-rating').text.strip() if movie.find('div', class_='inline-block ratings-imdb-rating') else 'No rating',
        'path': movie.find('h3', class_='lister-item-header').a['href']
    }

movie_list = list(map(get_movie_info, movie_list))

for idx, movie in enumerate(movie_list, 1):
    print(f'{idx}. {movie["title"]}, {movie["rating"]}\n{BASE_URL + movie["path"]}')
    