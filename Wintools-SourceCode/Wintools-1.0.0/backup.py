from shutil import copy
from os.path import exists

def offline_backup(src_folder_path: str, no_of_copies_to_backup: int, Paths: list):
    """
    The src_folder_path should be given the source 
    folder containing the files to backup.

    The no_of_copies_to_backup shoul contain the number
    of copies to backup.

    The Paths input should be given an list of paths.
    The no_of_copies_to_backup should be equal as
    no of paths in the list as a copy is stored in every
    directory given ih the Paths list input
    """
    run = True
    if no_of_copies_to_backup == len(Paths):
        for i in Paths:
            if not exists(str(i)):
                run = False
        while run == True:
            if exists(src_folder_path):
                for i in Paths:
                    copy(src_folder_path, str(i))