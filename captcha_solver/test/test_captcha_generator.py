import pytest

from captcha_solver.generator_honza import CaptchaContentGenerator

class TestCaptchaContentGenerator:

    def setup(self):
        """Create testing instance of generator."""
        numbers = True
        lowercase = True
        uppercase = True
        self.test = CaptchaContentGenerator(numbers, lowercase, uppercase)

    def test_generator_with_correct_parameter_numbers(self):
        assert self.test.numbers

    def test_generator_with_incorrect_parameter_numbers(self):
        assert self.test.numbers is not False

    def test_generator_with_correct_parameter_lowercase(self):
        assert self.test.lowercase

    def test_generator_with_incorrect_parameter_lowercase(self):
        assert self.test.lowercase is not False

    def test_generator_that_collects_correct_numbers(self):
        assert self.test.collect_numbers() == "0123456789"

    def test_generator_that_collects_incorrect_numbers(self):
        assert self.test.collect_numbers() != "012346789"
