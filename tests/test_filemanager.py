import unittest
from unittest import mock
from src.filemanager import FileManager
from constants import constants as ct

LISTING_METHOD = ct.LISTING_METHOD
FILE_LIST = ct.FILE_LIST
SORTED_LIST = ct.SORTED_LIST
REVERSE_SORTED = ct.REVERSE_SORTED

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.fm = FileManager(path='./test_dir/')
        self.files = FILE_LIST
        self.sorted = SORTED_LIST
        self.reversed_sorted = REVERSE_SORTED

    def tearDown(self):
        self.fm.remove_directory('test_dir')

    def test_init_with_existing_directory(self):
        with mock.patch(LISTING_METHOD, return_value=self.files):
            fm = FileManager(path='./test_dir/')
            self.assertEqual(fm.files, self.files)

    def test_init_with_non_existing_directory(self):
        with mock.patch(LISTING_METHOD, side_effect=FileNotFoundError):
            fm = FileManager(path='./non_existing_dir/')
            self.assertEqual(fm.path, './')

    def test_get_files(self):
        with mock.patch(LISTING_METHOD, return_value=self.files):
            files = self.fm.get_files()
            self.assertEqual(files, self.files)

    def test_list_all_files(self):
        with mock.patch(LISTING_METHOD, return_value=self.files):
            files = self.fm.list_all_files()
            self.assertEqual(files, self.files)

    def test_sort_all_files(self):
        with mock.patch(LISTING_METHOD, return_value=self.files):
            self.fm.sort_all_files()
            self.assertEqual(self.files, self.sorted)

    def test_reverse_sort_all_files(self):
        with mock.patch(LISTING_METHOD, return_value=self.files):
            self.fm.reverse_sort_all_files()
            self.assertEqual(self.files, self.reversed_sorted)

    def test_list_first_ten_files_with_more_than_ten_files(self):
        with mock.patch(LISTING_METHOD, return_value=self.files[:10]):
            files = self.fm.list_first_ten_files()
            self.assertEqual(files, self.files[:10])

    def test_list_first_ten_files_with_less_than_ten_files(self):
        with mock.patch(LISTING_METHOD, return_value=['file10.txt', 'file20.txt', 'file30.txt']):
            files = self.fm.list_first_ten_files()
            self.assertEqual(files, ['file10.txt', 'file20.txt', 'file30.txt'])

    def test_list_first_ten_files_with_more_than_ten_files(self):
        with mock.patch(LISTING_METHOD, return_value=self.files[-10:]):
            files = self.fm.list_last_ten_files()
            self.assertEqual(files, self.files[-10:])

    def test_list_last_ten_files_with_less_than_ten_files(self):
        with mock.patch(LISTING_METHOD, return_value=['file1.txt', 'file2.txt', 'file3.txt']):
            files = self.fm.list_last_ten_files()
            self.assertEqual(files, ['file1.txt', 'file2.txt', 'file3.txt'])

    def test_create_new_directory(self):
        with mock.patch('os.mkdir', return_value=None, side_effect=OSError) as mock_mkdir:
            self.fm.create_new_directory('test')
            mock_mkdir.assert_called_once_with(self.fm.path + 'test')

    def test_create_leaf_directory(self):
        with mock.patch('os.makedirs', return_value=None, side_effect=OSError) as mock_makedirs:
            self.fm.create_leaf_directory('test')
            mock_makedirs.assert_called_once_with(self.fm.path + 'test')

    def  test_remove_file_from_folder(self):
        with mock.patch('os.remove', return_value=None, side_effect=FileNotFoundError) as mock_remove:
            self.fm.remove_file_from_folder('test')
            mock_remove.assert_called_once_with(self.fm.path + 'test')

    def test_remove_empty_directory(self):
        with mock.patch('os.rmdir', return_value=None, side_effect=OSError)as mock_rmdir:
            self.fm.remove_empty_directory('test')
            mock_rmdir.assert_called_once_with(self.fm.path + 'test')

    def test_remove_directory(self):
        with mock.patch('shutil.rmtree', return_value=None, side_effect=FileNotFoundError) as mock_rmtree:
            self.fm.remove_directory('test')
            mock_rmtree.assert_called_once_with(self.fm.path + 'test')
