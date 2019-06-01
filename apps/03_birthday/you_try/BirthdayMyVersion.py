import datetime


def print_header():
    print('--------------------------------------')
    print('            BIRTHDAY APP')
    print('--------------------------------------')
    print()


def get_birthday_from_user():
    print("Koska olet syntynyt? ")
    year = int(input("Vuosi [VVVV]: "))
    month = int(input("kuukausi [KK]: "))
    day = int(input("Päivä [PP]: "))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print("Syntymäpäiväsi oli {} päivää sitten tänä vuonna.". format(-days))
    elif days > 0:
        print("Syntymäpäiväsi on {} päivän päästä tänä vuonna.".format(days))
    else:
        print("Hyvää Syntymäpäivää!!!")


def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print(number_of_days)
    print_birthday_information(number_of_days)

main()
