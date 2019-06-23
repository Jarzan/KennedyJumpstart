import collections
import csv
import os
from My_data_types import Purchases
import statistics

def main():
    print_header()
    filename = get_data_file()
    print(filename)
    data = load_file(filename)
    query_data(data)
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
        purchases = []
        for row in reader:
            # print(row)
            # print('Bed count: {}'.format(row['beds']))
            p = Purchases.create_from_dict(row)
            purchases.append(p)

        return purchases

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

"""HUOMAA: lambda-metodilla voidaan korvata aiemmin määritetty get_price(p)-funktio
jolla tuotettiin hintatieto järjestelyä ja halvimman ja kalleimman 
poimimista varten:"""

#def get_price(p):
#    return p.price


def query_data(data): #: list[Purchases]):

    # if data was sorted by price:
    data.sort(key=lambda p: p.price) # lambda p. p on ikään kuin funktioon sijoitettu argumentti
    # Huomaa myös että p.price on sama kuin korvatun funktion palautusarvo!
    # most expensive house?
    high_purchase = data[-1]
    print('The most expensive house is ${:,} with {} beds and with {} baths.'.format(high_purchase.price, high_purchase.beds, high_purchase.baths))
    # least expensive house?
    low_purchase = data[0]
    print('The least expensive house is ${:,} with {} beds and with {} baths.'.format(low_purchase.price, low_purchase.beds, low_purchase.baths))

    # average price house? statistics-modulin mean-metodista:

    #prices = []
    # for pr in data:
    #   prices.append(pur.price)
    # Ylläolevaan looppikoodin voi korvata list comprehensionilla:

    prices = [
        p.price # projection or items tuplena
        for p in data # the set to process
    ]


    ave_price = statistics.mean(prices)
    print("The average home price is ${:,}.".format(int(ave_price)))
    # average price of 2 bedroom houses?
    #prices = []
    # baths = []
    #for pur in data:
    #    if pur.beds == 2:
    #        prices.append(pur.price)
    #        baths.append(pur.baths)

    two_bed_homes = [
        p  # projection or items tuplena
        for p in data  # the set to process
        if p.beds == 2 # test/condition
    ]

# List comprehensives:
    ave_price = statistics.mean(p.price for p in two_bed_homes)
    ave_baths = statistics.mean(p.baths for p in two_bed_homes)
    ave_sqft = statistics.mean(p.sq__ft for p in two_bed_homes)

    print("The average price of a 2-bedroom home is ${:,}, baths={}, sq ft={}.".format(int(ave_price), round(ave_baths, 1), round(ave_sqft, 1)))


if __name__ == '__main__':
    main()
