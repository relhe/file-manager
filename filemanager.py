import os

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
