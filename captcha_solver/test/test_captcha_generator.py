import pytest

from captcha_solver.generator_honza import DatasetGenerator


class TestDatasetGenerator:

    def setup(self):
        """Create a testing instance of creating new dataset."""
        x: int = 180
        y: int = 50
        self.test = DatasetGenerator(x, y)

    def test_the_correct_parameter_of_first_dimension(self):
        """Check if the given parameter is correct instance attr."""
        assert self.test.size_x == 180

