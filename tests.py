# tests.py

import unittest
from functions.files import write_file, run_python_file


class TestFunctions(unittest.TestCase):

    # def test_lorem_ipsum(self):
    #     response = get_file_content("calculator", "lorem.txt")
    #     print(response)
    #     self.assertTrue("truncated at 10000 characters" in response)

    def test_write_file(self):
        response = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(response)
        self.assertTrue("Successfully wrote" in response)

    def test_write_more_lorem(self):
        response = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(response)
        self.assertTrue("Successfully wrote" in response)
    
    def test_write_file_outside_directory(self):
        response = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(response)
        self.assertTrue("Error: Cannot write to" in response)

    # Running python files

    def test_run_python_file(self):
        response = run_python_file("calculator", "main.py")
        print(response)
        self.assertTrue("STDOUT" in response or "Error" in response)

    def test_run_python_file_two(self):
        response = run_python_file("calculator", "tests.py")
        print(response)
        self.assertTrue("STDERR" in response or "Error" in response)

    def test_run_python_file_three(self):
        response = run_python_file("calculator", "../main.py")
        print(response)
        self.assertTrue("STDOUT" in response or "Error" in response)

    def test_run_python_file_four(self):
        response = run_python_file("calculator", "nonexistent.py")
        print(response)
        self.assertTrue("STDOUT" in response or "Error" in response)

if __name__ == "__main__":
    unittest.main()