import os
import pytest

from captcha_solver.generator_honza import DatasetGenerator


class TestDatasetGenerator:

    def setup(self):
        """Create a testing instance of creating new dataset."""
        x: int = 180
        y: int = 50
        folder: str = "foo"
        choices: int = 10
        self.content: str = "a1bc2"
        self.test = DatasetGenerator(x, y, folder, choices, self.content)

    def test_the_correct_parameter_of_first_dimension(self):
        assert self.test.size_x == 180

    def test_the_incorrect_parameter_of_first_dimension(self):
        assert self.test.size_x != 280

    def test_the_correct_value_of_the_second_dimension(self):
        assert self.test.size_y == 50

    def test_the_incorrect_value_of_the_second_dimension(self):
        assert self.test.size_y != 55

    def test_if_the_given_correct_default_parameter_path(self):
        assert self.test.folder == "foo"

    def test_if_the_given_incorrect_default_parameter_path(self):
        assert self.test.folder != "bar"

    def test_correct_value_of_parameter_choices(self):
        assert self.test.choices == 10

    def test_generating_new_dataset_of_captcha_pictures(self):
        assert self.test.generate_dataset("captcha_solver") \
            == "captcha_solver/foo/a1bc2.png"

    def test_method_for_creating_a_new_empty_folder_if_it_does_not_exist(self):
        assert self.test.create_empty_dir("captcha_solver/") \
            != "INFO: created directory foo at captcha_solver/"

    def test_method_for_already_existing_folder_foo(self):
        assert self.test.create_empty_dir("captcha_solver/") \
            == "WARNING: Folder foo already exists"

    def test_method_for_creating_testing_image(self):
        self.test.create_image("captcha_solver", self.content)

        assert "a1bc2.png" in os.listdir("captcha_solver/foo")

    def test_method_if_there_is_no_incorrect_image(self):
        assert os.listdir("captcha_solver/foo") == ["a1bc2.png"]


    def test_cleaning_the_created_captcha_image_from_the_foo_folder(self):
        try:
            os.remove("captcha_solver/foo/a1bc2.png")

        except FileNotFoundError:
            print("There is no such file.")

    def test_cleaning_the_created_testing_folder(self):
        try:
            os.rmdir("captcha_solver/foo")

        except FileNotFoundError:
            print("There is no such folder")

