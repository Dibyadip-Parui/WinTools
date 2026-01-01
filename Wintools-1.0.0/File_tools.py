import os
import shutil

chunk = 1024*1024

class Rename():
    def rename_1234(folder_path):
        if os.path.exists(folder_path):
            os.chdir(folder_path)
            os.mkdir("Renamed_files")
            File_list = os.listdir()
            i=(-1)
            for o in File_list:
                i=i+1
                extention = File_list[i].split('.')
                with open(File_list[i], "rb") as file_in, open(os.path.join("Renamed_files", str(i)+"."+str(extention[1])), "wb") as file_out:
                    while True:
                        data = file_in.read(chunk)
                        file_out.write(data)
                        if not data:
                            break
                    file_in.close()
                    file_out.close()
    def rename_name(name, folder_path):
        if os.path.exists(folder_path):
            os.chdir(folder_path)
            os.mkdir("Renamed_files")
            File_list = os.listdir()
            i=(-1)
            for o in File_list:
                _i=_i+1
                i = str(name)+str(_i)
                extention = File_list[i].split('.')
                with open(File_list[i], "rb") as file_in, open(os.path.join(str(i)+"."+str(extention[1])), "wb") as file_out:
                    while True:
                        data = file_in.read(chunk)
                        file_out.write(data)
                        if not data:
                            break
                    file_in.close()
                    file_out.close()
        del i, _i
        del File_list
        del folder_path
        del data
class sort():
    def sort_size(folder_path):
        try:
            if os.path.exists(folder_path):
                os.chdir(folder_path)
                files = []
                count = -1
                for i in os.listdir():
                    count = count+1
                    try:
                        temp = i.split('.')[1]
                        files.insert(count, i)
                    except IndexError:
                        _ = _+1
                try:
                    os.mkdir("Big")
                    os.mkdir("Medium")
                    os.mkdir("Small")
                    os.mkdir("Tiny")
                except FileExistsError or FileNotFoundError:
                    print("File exists or flder path is invalid.")
                
                for file in files:
                    file_size = os.path.getsize(file)
                    if file_size < 16*1024:
                        shutil.copy(file, os.path.join("Tiny", file))
                    if file_size <= 10*1024*1024 and file_size > 16*1024:
                        shutil.copy(file, os.path.join("Small", file))
                    if file_size <= 1024*1024*1024 and file_size >10*1024*1024:
                        shutil.copy(file, os.path.join("Medium", file))
                    if file_size > 100*1024*1024*1024:
                        shutil.copy(file, os.path.join("Big", file))
                del file_size, file, files

            else:
                print("Path not found!")
        except os.error as e:
            print("An error occured:", e) 
    def sort_extention(folder_path):
        try:
            if os.path.exists(folder_path):
                os.chdir(folder_path)
                files = []
                count = -1
                for i in os.listdir():
                    count = count+1
                    try:
                        temp = i.split('.')[1]
                        files.insert(count, i)
                    except IndexError:
                        _=_+1
                for file in files: 
                    i = file.split('.')[1]
                    if not os.path.exists(i):
                        os.mkdir(i)
                    if not os.path.exists(os.path.join(i, file)):
                        shutil.copy(file, os.path.join(i, file))
                    else:
                            print(os.path.join(i, file), "Exists!")
            else:
                print("Path not found!")
        except os.error as e:
            print("An error occured:", e) 