import os


def main():
    #  print the header:
    print_header()
    #  get or create output folder
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    #  download cats
    #  display cats


def print_header():
    print('---------------------------')
    print('       Cat Factory App')
    print('---------------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.abspath(os.path.join(base_folder, folder))
    # at this point print the full path to see it:
    #  print(full_path)

    #  This if-statement creates the folder if not found:
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path) # Tämä luo hakemiston

    return full_path

if __name__ == '__main__':
    main()