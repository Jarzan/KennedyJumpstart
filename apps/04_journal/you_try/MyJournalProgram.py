import MyJournal


# from journal import load, save
# from journal import *

# Tämä on pääohjelma joka hoitaa kaikki hommat:
def main():
    """Aluksi listaamme tähän pääfunktiooon ohjeman toiminnat suorittavat alifunktiot.
    Tämä high-level-funktio siirretään jatkossa aina ensimmäiseksi ja
    alifunktiot määritetään sen alle"""
    print_header()
    run_event_loop()


def print_header():
    """Tulostaa ohjelman esittelyotsakkeen."""
    print('-----------------------------')
    print('         JOURNAL APP')
    print('-----------------------------')


def run_event_loop():
    """Tässä kysytään käyttäjältä minkä toiminnan hän haluaa ajaa."""
    print('Mitä haluat tehdä päiväkirjallasi?')  # Appi aloitetaan kysymällä käyttäjältä jotain.
    cmd = 'TYHJÄ'
    journal_name = 'default'
    journal_data = MyJournal.load(journal_name)  # [] # voi toteuttaa myös list()-metodilla

    while cmd != 'x' and cmd:  # Pythonissa toteutuu vain jos ehto on tosi jos cmd=tyhjä, niin False, Siksi pelkkä cmd.

        cmd = input('[L]istaa syötteet, [A]dd syöte, E[x]it poistu: ')  # Tämä ottaa vastaan käyttäjän komennon.
        cmd = cmd.lower().strip()

        if cmd == 'l':  # Huomaa että ehdon ajot on ohjattu funktioon! Cool!
            list_entries(journal_data)  # Huomaa että tyhjä lista on parametrina! Cool!

        elif cmd == 'a':
            add_entry(journal_data)

        elif cmd != 'x' and cmd:  # Tämä siksi jos käyttäjä syöttää puutaheinää.LISÄKSI tyhjä=False.Siksi pelkkä cmd.
            print("Sori, en ymmärtänyt pyyntöäsi '{}'...".format(cmd))

    print('Kiitos ja näkemiin!')
    MyJournal.save(journal_name, journal_data)


def list_entries(data):
    print('Sinun tekstisi: ')
    entries = reversed(data)  # Tämä toiminto kääntää syötteen tulostusjärjstyksen.
    for idx, entry in enumerate(entries):  # Tämä enumerate()-toiminto lisää indeksinron joka syötteelle.
        print('* [{}] {}'.format(idx + 1, entry))  # Tämä lisää * alkuu ja idx-muuttujan []:iin.


def add_entry(data):
    text = input('Kirjoita syötteesi, <enter> poistu: ')
    MyJournal.add_entry(text, data)
    # data.append(text) # Syöte mene data-muuttujaan.

print("__file__" + __file__) # Tämä moduli edustaa "full path to programmia"
print("__name__" + __name__) # Tämä moduli edustaa koko ohjelmaa!!!

if __name__ == '__main__':
    main()
