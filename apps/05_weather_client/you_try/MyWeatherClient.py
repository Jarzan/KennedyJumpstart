import requests


def main():
    #  print the header
    print_the_header()
    #  get zip code from user
    postinumero = input('Mille postinumerolle haluat sääennusteen? (01860)')
    html = get_html_from_web(postinumero)
    #  parse the html
    #  display the forecast



def print_the_header():
    print('-------------------------')
    print('       WEATHER APP')
    print('-------------------------')
    print()


def get_html_from_web(postinumero):
    url = 'https://www.wunderground.com/weather/fi/{}'.format(postinumero)
    # print(url)
    response = requests.get(url)
    # print(response.status_code) # Tällä saadaan selville webbisivun status_code
    #  https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    # print(response.text[0:250]) # Tämä antaa sivusta 250 ekaa merkkiä

    return response.text

def fetch_zip_code():
    pass


def weather_info():
    pass


def display_weather():
    pass


if __name__ == '__main__':
    main()
