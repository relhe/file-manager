import os
import src.filemanager as fm

if __name__ == "__main__":
    print("This program allows you to manage files in a directory.")
    print("Please Give the path to the directory you want to manage ending with /.")
    print("The path must exist and be a directory other wise the current directory will be used.")

    while True:
        path = input("Enter path: ")
        if path == "":
            path = "./"
        f = fm.FileManager(path)
        if os.path.exists(path) and os.path.isdir(path):
            break

    print("")
    print("choose an option (Enter option number):")
    option1to3 = " 0. See option list\n 1. List all files\n 2. Sort file\n 3. back-sort file\n"
    option4to6 = " 4. List first 10 files\n 5. List last 10 files\n 6. Create new directory\n"
    option7to9 = " 7. Create nested directory\n 8. Create new file\n 9. Remove file from folder\n"
    option10to11 = " 10. remove an empty directory\n 11. remove non-empty directory from folder\n"
    option12to13 = " 12. move file to another directory\n 13. move file from location to another\n"
    option14to15 = " 14. copy file to another directory\n 15. rename file in folder\n"
    option16to17 = " 16. modify file name with pattern in folder\n q. exit\n"
    options = option1to3 + option4to6 + option7to9 + option10to11 + option12to13 + option14to15 + option16to17
    print(options)

    command = dict()
    command["0"] = lambda : print(options)
    command["1"] = f.list_all_files
    command["2"] = f.sort_all_files
    command["3"] = f.reverse_sort_all_files
    command["4"] = f.list_first_ten_files
    command["5"] = f.list_last_ten_files
    command["6"] = lambda : f.create_new_file(input("Enter new directory name: "))
    command["7"] = lambda : f.create_leaf_directory(input("Enter directories separated by /: "))
    command["8"] = lambda : f.create_new_file(input("Enter new filename: "))
    command["9"] = lambda : f.remove_file_from_folder(input("Enter existing filename: "))
    command["10"] = lambda : f.remove_empty_directory(input("Enter empty directory name: "))
    command["11"] = lambda : f.remove_directory(input("Enter directory name: "))
    command["12"] = lambda : f.move_to_another_directory(input("Enter filename: "), input("Enter new path ending with /: "))
    command["13"] = lambda : f.move_file_from_folder_to_another(input("Enter old pathname: "), input("Enter new pathname: "))
    command["14"] = lambda : f.copy_file_to_another_directory(input("Enter the filename: "), input("Enter new path: "))
    command["15"] = lambda : f.rename_file_in_folder(input("Enter filename: "), input("Enter new filename: "))
    command["16"] = lambda : f.modify_file_name_with_pattern(input("Enter seeking pattern: "), input("Enter new replacement pattern: "))
    command["q"] = lambda : exit()

    while True:
        print("")
        i = input("Enter an option number: ")
        try:
            command[i]()
        except KeyError:
            print("Invalid option number.")
