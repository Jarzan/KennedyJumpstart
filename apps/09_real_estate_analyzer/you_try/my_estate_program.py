import collections
import csv
import os


def main():
    print_header()
    filename = get_data_file()
    print(filename)
    data = load_file(filename)
    # query_data(data)
    # estate_header
    # estate_price


def print_header():
    print('--------------------------------------------')
    print('         Real Estate Data Mining App')
    print('--------------------------------------------')


def get_data_file():
    """Tässä tapauksessa tieto haetaan os-modulia käyttämällä.
    base_folder määritetään ensin. Jokaiselle modulille on __file__,
    joka kertoo, että tässä on "base folder".
    Etuna on se että ei väliä missä kansiossa ajamme ohjelmaamme,
    pääsemme siitä huolimatta aina hakemaan tietoa base_folderin kautta."""
    base_folder = os.path.dirname(__file__)
    """HUOMAA: Michaelin koodissa 
    return os.path.join(base_folder, data, 'SacramentoRealEstateTransactions2008.csv')
    'data'-parametri määrittää alikansion tämän/kyseisen kansion alla!!!"""
    return os.path.join(base_folder, 'SacramentoRealEstateTransactions2008.csv')

def load_file(filename):
    """Tehdään tiedostonhaku fiksummin csv-modulia käyttäen. Iterable tässä
    tapauksessa on fin-muuttuja"""
    with open(filename, 'r', encoding='utf-8') as fin:

        """Paras vaihtoehto tiedon hakemiseen csv-modulilla on DictReader-metodi,
        joka tuottaa csv:stä sanakirjamuotoisen tiedon (avain:arvo-pari), johon ei
        tiedon lisääminen vaikuta:"""

        reader = csv.DictReader(fin)
        for row in reader:
            print(type(row), row)
            print('Bed count: {}'.format(row['beds']))

        """Tämä ei ole optimaalinen tapa koska saraketieto riippuu indeksistä
        joka voi muuttua tiedon lisäämisen yhteydessä:"""
        #header = fin.readline().strip()
        #reader = csv.reader(fin)
        #for row in reader:
        #    print(type(row), row)
        #    beds = row[4] #


        #print('found header' + header)

        lines = []
        """Ensimmäinen rivi täytyy jättää lukematta.
        Lisäksi jokainen rivi täytyy muuttaa datasarakkeeksi."""
        for line in fin:
            line_data = line.strip().split(',')
            bed_count = line_data[4]
            lines.append(line_data)

        print(lines[:5])

#def load_file_basic(filename):
#    """Tässä metodissa tiedosto vain luetaan."""
#    with open(filename, 'r', encoding='utf-8') as fin:
#        header = fin.readline().strip()
#        print('found header' + header)
#
#        lines = []
#        """Ensimmäinen rivi täytyy jättää lukematta.
#        Lisäksi jokainen rivi täytyy muuttaa datasarakkeeksi."""
#        for line in fin:
#            line_data = line.strip().split(',')
#            bed_count = line_data[4]
#            lines.append(line_data)
#
#        print(lines[:5])


#def query_data(data):
#    pass

if __name__ == '__main__':
    main()
