import os
import shutil

class FileManager:
    def __init__(self, path = "./"):
        self.path = path
        try:
            self.files = os.listdir(self.path)
        except FileNotFoundError:
            print("The path does not exist.")
            self.path = "./"

    def get_files(self):
        self.files = os.listdir(self.path)
        return self.files

    def list_all_files(self):
        self.files = os.listdir(self.path)
        for filename in self.files:
            print(" " + filename)

    def sort_all_files(self):
        self.files = os.listdir(self.path)
        self.files.sort()
        for filename in self.files:
            print(filename)

    def reverse_sort_all_files(self):
        self.files = os.listdir(self.path)
        self.files.sort()
        self.files.reverse()
        for filename in self.files:
            print(filename)

    def list_first_ten_files(self):
        self.files = os.listdir(self.path)
        if len(self.files) > 10:
            files = self.files[0:10]
            for filename in files:
                print(filename)
        else:
            for filename in self.files:
                print(filename)

    def list_last_ten_files(self):
        self.files = os.listdir(self.path)
        if len(self.files) > 10:
            files = self.files[-10:]
            for filename in files:
                print(filename)
        else:
            for filename in self.files:
                print(filename)

    def create_new_directory(self, dirname):
        try:
            os.mkdir(self.path + dirname)
        except OSError:
            print(f"The {dirname} directory already exists.")

    def create_leaf_directory(self, dirname):
        try:
            os.makedirs(self.path + dirname)
        except OSError:
            print(f"The {dirname} directory already exists.")

    def create_new_file(self, filename):
        try:
            open(self.path + filename, "w")
        except OSError:
            print("The file already exists.")

    def remove_file_from_folder(self, filename):
        try:
            os.remove(self.path + filename)
        except FileNotFoundError:
            print(f"The {filename} file does not exist.")
        except OSError:
            print("The file is a directory.")

    def remove_empty_directory(self, dirname):
        try:
            os.rmdir(self.path + dirname)
        except FileNotFoundError:
            print(f"The {dirname} directory does not exist.")
        except OSError:
            print("The directory is not empty.")

    def remove_directory(self, dirname):
        try:
            shutil.rmtree(self.path + dirname)
        except FileNotFoundError:
            print(f"The {dirname} directory does not exist.")
        except NotADirectoryError:
            print(f"The file is not a directory.")

    def move_to_another_directory(self, filename, new_path):
        # verify if the new_path exists if not it creates it + the file to be moved
        if(not os.path.exists(new_path)):
            os.makedirs(new_path)
        try:
            shutil.move(self.path + filename, new_path)
        except FileNotFoundError:
            print(f"The {filename} file does not exist.")
        except OSError:
            print("The file already exists.")

    def move_file_from_folder_to_another(self, original_path, new_path):
        try:
            if(not os.path.exists(original_path)):
                raise FileNotFoundError
            if(not os.path.exists(new_path)):
                os.makedirs(new_path)
            shutil.move(original_path, new_path)
        except FileNotFoundError:
            print("The file does not exist in this pathname")
        except FileExistsError:
            print("The file already exists in the new path last directory.")

    def rename_file_in_folder(self, original_name, new_name):
        try:
            os.rename(self.path + original_name, self.path + new_name)
        except FileNotFoundError:
            print(f"The file {original_name} does not exist.")
        except FileExistsError:
            print(f"The file {new_name} already exists.")
        except IsADirectoryError:
            print(f"The file is a directory.")
        except NotADirectoryError:
            print(f"The file is not a directory.")
        except OSError:
            print(f"There already is a not empty {new_name} folder.")

    def modify_file_name_with_pattern(self, pattern, new_pattern = ""):
        self.files = os.listdir(self.path)
        for filename in self.files:
            if pattern in filename and os.path.isfile(self.path + filename):
                new_name = filename.replace(pattern, new_pattern)
                self.rename_file_in_folder(filename, new_name)

    def copy_file_to_another_directory(self, filename, new_path):
        try:
            shutil.copy(self.path + filename, new_path)
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")
        except FileExistsError:
            print(f"The file {filename} already exists.")
        except IsADirectoryError:
            print(f"The file is a directory.")
        except NotADirectoryError:
            print(f"The file is not a directory.")
        except OSError:
            print(f"There already is a not empty {filename} folder.")