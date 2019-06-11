import os
import subprocess

import My_cat_service

def main():
    #  print the header:
    print_header()
    #  get or create output folder
    folder = get_or_create_output_folder()
    #  download cats
    download_cats(folder)
    #  display cats
    display_cats(folder)


def print_header():
    print('---------------------------')
    print('       Cat Factory App')
    print('---------------------------')


def get_or_create_output_folder():
    base_folder = os.path.abspath(os.path.dirname(__file__))
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)
    # at this point print the full path to see it:
    #  print(full_path)

    #  This if-statement creates the folder if not found:
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)  # Tämä luo hakemiston
    #  You need to reurt full_path whether or you created it:
    return full_path


def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        My_cat_service.get_cat(folder, name)

    print('Done.')


def display_cats(folder):
    #  open folder:
    print('Displaying cats in OS window')
    subprocess.call(['open', folder])


if __name__ == '__main__':
    main()
