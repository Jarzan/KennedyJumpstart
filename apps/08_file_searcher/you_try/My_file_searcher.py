import os


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print('Sorry, we cannot search that location.')
        return

    text = get_search_text_from_user()
    if not folder:
        print('Sorry, we cannot find the file in the location.')
        return

    matches = search_folders(folder, text)

    for m in matches:
        print(m)


def print_header():
    print('--------------------------')
    print("     File Search App")
    print('--------------------------')


def get_folder_from_user():
    folder = input('What folder do you want to search?')
    # Ehto tapaukseen mikäli kansiota ei löydy tai mikäli pelkkä 'white space'
    if not folder or not folder.strip(): # Käynnistää if-lauseen main():ssa.
        return None
    # Tsekkaa onko kansiota, isdir() mikäli antaa filen nimen:
    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]? ')
    return text.lower()


def search_folders(folder, text):
    print("Would search {} for {}".format(folder, text))
    # Hakutulos palautetaan listana:
    all_matches = []
    # Tämä palauttaa kaikki itemit (files+filders) kansiossa:
    items = os.listdir(folder) # <= Tämä (videolta) aiheuttaa crashin MacOS:ssä, joten:
    # items = glob.glob( os.path.join(folder, '*'))

    for item in items:
        full_item = os.path.join(folder, item)
        # Jos item on kansio, jatka looppaamista, eli:
        if os.path.isdir(full_item):
            continue

        matches = search_file(full_item, text)
        # With collection of matches you need to add to [] with extend()-method instead of append()-method:
        all_matches.extend(matches)

    return all_matches


def search_file(filename, search_text):
    matches = []
    # with open()-komennolla varmistetaan että file suljetaan avaamisen jälkeen:
    # Avataan file ja luetaan filename tekstinä
    with open(filename, 'r', encoding='utf-8') as fin:
        # Tekstifilen rivien iteratiivinen luku onko teksti riveillä:
        for line in fin:
            # find()-method palauttaa -1 mikäli ei mätsiä:
            if line.lower().find(search_text) >= 0:
                matches.append(line)

        return matches



if __name__ == '__main__':
    main()
