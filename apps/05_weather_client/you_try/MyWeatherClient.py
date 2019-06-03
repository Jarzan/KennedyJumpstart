def main():
    #  print the header
    print_the_header()
    #  get zip code from user
    postinumero = input('Mille postinumerolle haluat sääennusteen? (01860)')
    #  get html from web
    get_html_from_web(postinumero)
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
    requests

def fetch_zip_code():
    pass


def weather_info():
    pass


def display_weather():
    pass


if __name__ == '__main__':
    main()
