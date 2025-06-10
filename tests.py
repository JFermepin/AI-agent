# tests.py

import unittest
from functions.get_files_info import get_files_info


class TestFunctions(unittest.TestCase):

    def test_full_directory(self):
        response = get_files_info("calculator", ".")
        print(response)
        self.assertTrue(response.startswith("- pkg: file_size="))

    def test_subdirectory(self):
        response = get_files_info("calculator", "pkg")
        print(response)
        self.assertTrue(response.startswith("- calculator.py: file_size="))
    
    def test_directory_not_in_range(self):
        response = get_files_info("calculator", "/bin")
        self.assertEqual(
            response,
            'Error: Cannot list "/bin" as it is outside the permitted working directory'
        )

    def test_directory_not_in_range_two(self):
        response = get_files_info("calculator", "../")
        print(response)
        self.assertEqual(
            response,
            'Error: Cannot list "../" as it is outside the permitted working directory'
        )

if __name__ == "__main__":
    unittest.main()