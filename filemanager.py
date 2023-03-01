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
        return self.files

    def list_all_files(self):
        for filename in self.files:
            print(filename)

    def sort_all_files(self):
        self.files.sort()
        for filename in self.files:
            print(filename)

    def reverse_sort_all_files(self):
        self.files.sort()
        self.files.reverse()
        for filename in self.files:
            print(filename)

    def list_first_ten_files(self):
        if len(self.files) > 10:
            files = self.files[0:10]
            for filename in files:
                print(filename)
        else:
            for filename in self.files:
                print(filename)

    def list_last_ten_files(self):
        if len(self.files) > 10:
            files = self.files[-10:]
            for filename in files:
                print(filename)
        else:
            for filename in self.files:
                print(filename)

    def create_new_directory(self, dirname):
        try:
            os.mkdir(self.path + "/" + dirname)
        except OSError:
            print(f"The {dirname} directory already exists.")

    def create_leaf_directory(self, dirname):
        try:
            os.makedirs(self.path + "/" + dirname)
        except OSError:
            print(f"The {dirname} directory already exists.")

    def create_new_file(self, filename):
        try:
            open(self.path + "/" + filename, "w")
        except OSError:
            print("The file already exists.")