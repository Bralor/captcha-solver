import pytest

from captcha_solver.generator_honza import CaptchaContentGenerator

class TestCaptchaContentGenerator:

    def setup(self):
        """Create testing instance of generator."""
        numbers = True
        lowercase = True
        uppercase = True
        self.test = CaptchaContentGenerator(numbers, lowercase, uppercase)

    def test_correct_parameter_numbers(self):
        assert self.test.numbers

    def test_incorrect_parameter_numbers(self):
        assert self.test.numbers is not False

    def test_correct_parameter_lowercase(self):
        assert self.test.lowercase

    def test_incorrect_parameter_lowercase(self):
        assert self.test.lowercase is not False

    def test_collecting_of_correct_numbers(self):
        assert self.test.collect_numbers() == "0123456789"

    def test_collecting_of_incorrect_numbers(self):
        assert self.test.collect_numbers() != "012346789"

    def test_collecting_of_correct_lowercase_letters(self):
        assert self.test.collect_lowercase() == 'abcdefghijklmnopqrstuvwxyz'

    def test_collecting_of_incorrect_lowercase_letters(self):
        assert self.test.collect_lowercase() != 'abcdfghijklmnopqrstuvwxyz'

    def test_collecting_of_correct_uppercase_letters(self):
        assert self.test.collect_uppercase() == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def test_collecting_of_incorrect_uppercase_letters(self):
        assert self.test.collect_uppercase() != 'ABCDEFGHIJKLMOPQRSTUVWXYZ'

    def test_creating_correct_data_type_of_captcha(self):
        assert isinstance(self.test.create_content(), str)

    def test_creating_captchas_content_of_correct_length(self):
        assert len(self.test.create_content()) == 5
