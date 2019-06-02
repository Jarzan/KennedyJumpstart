# Tämä file hoitaa appin File I/O-toiminnot, tarkoittaen ohjelman lataus, nimeäminen ja tallennus:

import os


def load(name):  # Lataa journaalin ja ottaa sen nimen vastaan.

    """
        This method creates and loads a new journal.

        :param name: This base name of the journal to load.
        :return: A new journal data structure populated with the file data.
        """
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data


def save(name, journal_data):  # Tallentaa journaalin nimellä.
    filename = get_full_pathname(name)
    print("...saving to: {}".format(filename))
    # fout = open(filename, 'w')  # fout-muuttuja avaa tiedostonnimellä ja kirjoittaa siihen.
    with open(filename, 'w') as fout:

        for entry in journal_data:
            fout.write(entry + '\n') # \n lisättävä muuten kirjoittaa samalle riville pötköön.

    # fout.close()


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'MyJournals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)
