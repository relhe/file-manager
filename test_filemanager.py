import unittest
from filemanager import FileManager
import os

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.f = FileManager()
        self.f.create_new_directory('test')

    def test_get_files(self):
        self.assertEqual(self.f.get_files(), [])

    def test_list_all_files(self):
        self.assertEqual(self.f.list_all_files(), [])

    def test_sort_all_files(self):
        self.assertEqual(self.f.sort_all_files(), [])

    def test_reverse_sort_all_files(self):
        self.assertEqual(self.f.reverse_sort_all_files(), [])

    def test_list_first_ten_files(self):
        self.assertEqual(self.f.list_first_ten_files(), [])

    def test_list_last_ten_files(self):
        self.assertEqual(self.f.list_last_ten_files(), [])

    def test_create_new_directory(self):
        self.assertEqual(os.path.isdir('test'), True)

    def test_create_leaf_directory(self):
        self.f.create_leaf_directory('test/t/e/s/t')
        self.assertEqual(os.path.isdir('test/t'), True)
        self.assertEqual(os.path.isdir('test/t/e'), True)
        self.assertEqual(os.path.isdir('test/t/e/t'), True)

    def test_create_new_file(self):
        self.f.create_new_file('tutor.txt')
        self.assertEqual(os.path.isfile('test/tutor.txt'), True)

    def test_remove_file_from_folder(self):
        self.f.remove_file_from_folder('test')
        self.assertEqual(os.path.isdir('test'), False)

    def test_remove_empty_directory(self):
        self.f.remove_empty_directory('test')
        self.assertEqual(os.path.isdir('test'), False)

    def test_remove_directory(self):
        self.f.create_leaf_directory('test/t/e/s/t/o')
        self.f.remove_directory('test/t/e/s/t')
        self.assertEqual(os.path.isdir('test/t'), False)
        self.assertEqual(os.path.isdir('test/t/e'), False)
        self.assertEqual(os.path.isdir('test/t/e/t'), False)
        self.assertEqual(os.path.isdir('test/t/e/t/0'), False)
