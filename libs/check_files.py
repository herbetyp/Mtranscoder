import os


def files_exists(name_file: str, path: str, output_midia_format: str) -> bool:
    if not os.path.exists(path):
        return True
    else:
        while True:
            option = input(f'\nINFO: [The file "{name_file}_{output_midia_format}.{output_midia_format}"'
                           f' already exists.]\n\nDo you want to overwrite[y/n]: ')
            if option.strip().lower() == 'y':
                return True
            elif option.strip().lower() == 'n':
                return False
            else:
                print('\nINCORRECT OPTION!')
                continue
