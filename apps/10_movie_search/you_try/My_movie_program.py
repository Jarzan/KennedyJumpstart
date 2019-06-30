import movie_svc
import requests.exceptions


def main():
    print_header()
    search_event_loop()


def print_header():
    print('-------------------------------')
    print('       Movie Search App')
    print('-------------------------------')
    print('')


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x': # Tee etsintää niin kauan kunnes käyttäjä painaa 'x' eli exit.
        try:
            search = input('Movie search text (x to exit): ')
            if search != 'x':
                results = movie_svc.find_movies(search)
                print("Found {} results.".format(len(results)))
                for r in results:
                    print('{} -- {}'.format(
                        r.year, r.title
                    ))
                print()
        except requests.exceptions.ConnectionError as ce:
            print("Error, your network is down! Details: {}".format(ce))
        except ValueError as ve:
            print("Error, search text is required! Details: {}".format(ve))
        except Exception as x:
            print("Unexpected error. Details: {}".format(x))
    print('exiting...')
    # http://movie_service.talkpython.fm/api/search/


if __name__ == '__main__':
    main()

