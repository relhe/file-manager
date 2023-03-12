import unittest
from unittest import mock
from src.filemanager import FileManager

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.fm = FileManager(path='./test_dir/')
        self.files = [
            'file1.txt', 'file3.txt', 'file2.txt', 'file1.py', 'file4.txt',
            'file2.py', 'file3.py', 'dir0', 'dir1', 'dir2', 'dir3',]
        self.sorted = [
            'dir0', 'dir1', 'dir2', 'dir3','file1.py','file1.txt', 'file2.py',
            'file2.txt', 'file3.py', 'file3.txt', 'file4.txt'
        ]
        self.reversed_sorted = [
            'file4.txt','file3.txt','file3.py','file2.txt', 'file2.py',
            'file1.txt', 'file1.py', 'dir3', 'dir2', 'dir1', 'dir0'
        ]

    def tearDown(self):
        self.fm.remove_directory('test_dir')

    def test_init_with_existing_directory(self):
        with mock.patch('os.listdir', return_value=self.files):
            fm = FileManager(path='./test_dir/')
            self.assertEqual(fm.files, self.files)

    def test_init_with_non_existing_directory(self):
        with mock.patch('os.listdir', side_effect=FileNotFoundError):
            fm = FileManager(path='./non_existing_dir/')
            self.assertEqual(fm.path, './')

    def test_get_files(self):
        with mock.patch('os.listdir', return_value=self.files):
            files = self.fm.get_files()
            self.assertEqual(files, self.files)

    def test_list_all_files(self):
        with mock.patch('os.listdir', return_value=self.files):
            files = self.fm.list_all_files()
            self.assertEqual(files, self.files)

    def test_sort_all_files(self):
        with mock.patch('os.listdir', return_value=self.files):
            self.fm.sort_all_files()
            self.assertEqual(self.files, self.sorted)

    def test_reverse_sort_all_files(self):
        with mock.patch('os.listdir', return_value=self.files):
            self.fm.reverse_sort_all_files()
            self.assertEqual(self.files, self.reversed_sorted)

    def test_list_first_ten_files_with_more_than_ten_files(self):
        with mock.patch('os.listdir', return_value=self.files[:10]):
            files = self.fm.list_first_ten_files()
            self.assertEqual(files, self.files[:10])

    def test_list_first_ten_files_with_less_than_ten_files(self):
        with mock.patch('os.listdir', return_value=['file1.txt', 'file2.txt', 'file3.txt']):
            files = self.fm.list_first_ten_files()
            self.assertEqual(files, ['file1.txt', 'file2.txt', 'file3.txt'])

    def test_list_first_ten_files_with_more_than_ten_files(self):
        with mock.patch('os.listdir', return_value=self.files[-10:]):
            files = self.fm.list_last_ten_files()
            self.assertEqual(files, self.files[-10:])

    def test_list_last_ten_files_with_less_than_ten_files(self):
        with mock.patch('os.listdir', return_value=['file1.txt', 'file2.txt', 'file3.txt']):
            files = self.fm.list_last_ten_files()
            self.assertEqual(files, ['file1.txt', 'file2.txt', 'file3.txt'])

