import os


def files_exists(name_file: str, path: str, output_midia_format: str) -> bool:
    if not os.path.exists(path):
        return True
    else:
        print(
            f'\nThe file {name_file}_{output_midia_format}.{output_midia_format} already exists.')
        option = input('\nDo you want to overwrite[y/n]: ')
        if option.strip().lower() == 'y':
            return True
        elif option.strip().lower() == 'n':
            return False
        else:
            print('\nIncorrect option!')
