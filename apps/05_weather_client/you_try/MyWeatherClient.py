import requests
import bs4


def main():
    #  print the header
    print_the_header()
    #  get zip code from user
    postinumero = input('Mille postinumerolle haluat sääennusteen? (01860)')
    html = get_html_from_web(postinumero)
    #  parse the html
    get_weather_from_html(html)
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
    #  print(response.text[0:2500]) # Tämä antaa sivusta 250 ekaa merkkiä

    return response.text


def get_weather_from_html(html):
    #  cityCss = '.region-content-header h1'
    #  weatherScaleCss = '.wu-unit-temperature.wu-label'
    #  weatherTempCss = '.wu-unit-temperature.wu-value'
    #  weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()
    # print(soup) # Testiprinttaus että pyydetty html latautuu.
# Poistetaan tyhjät rivit:
    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    print(condition, temp, scale, loc)



def cleanup_text(text):
    if not text:
        return text

    text = text.strip()
    return text



def weather_info():
    pass


def display_weather():
    pass


if __name__ == '__main__':
    main()
