import os
import uuid
import json
import string
import random
import shutil
import itertools

from src.generator_honza import MyImageCaptcha


class DatasetGenerator:
    """Create a set of files"""

    def __init__(self, x: int, y: int, folder: str, choices: int, content: str):
        self.size_x = x
        self.size_y = y
        self.folder = folder
        self.choices = choices
        self.content = content

    def create_empty_dir(self, root_dir: str) -> str:
        """
        Create an empty directory if it does not already exist.

        :return: the string with the resulted status
        :rtype: str

        :Example:
        >>> dataset_1 = DatasetGenerator(
        ...     size_x=180, size_y=50, choices=5, 
        ...     folder="images", content="a1bc2"
        ... )
        >>> dataset_1.create_empty_dir("captcha_solver/")
        INFO: created directory images at captcha_solver/
        """
        try:
            os.mkdir(os.path.join(root_dir, self.folder))

        except FileExistsError:
            message: str = f"WARNING: Folder {self.folder} already exists"
        else:
            message: str = f"INFO: created directory {self.folder} at {root_dir}"
        finally:
            return message


    def generate_dataset(self, root_dir: str):
        """
        Create a dataset of captcha images.

        :Example:
        >>> dataset_1 = DatasetGenerator(
        ...     size_x=180, size_y=50, choices=5, content="a1bc2"
        ... )
        >>> dataset_1.generate_dataset()
        INFO: created directory /captcha_solver/images/ ..
        INFO: generated dataset of 5 images in /captcha_solver/images/*.
        """
        status: str = self.create_empty_dir(root_dir)

        if status.startswith("INFO:") or status.startswith("WARNING:"):
            return self.create_image(root_dir, self.content)


    def create_image(self, root_dir: str, png_name: str) -> str:
        """
        Create image object and save it to the disc.

        :return: the string with the name of .png file
        :rtype: str
        """
        image = MyImageCaptcha(self.size_x, self.size_y)
        png_name = os.path.join(root_dir, self.folder, f"{self.content}.png")
        image.write(self.content, png_name)

        return png_name


class CaptchaContentGenerator:
    """
    Generate captcha characters from the number, lowercase and uppercase
    letters.
    """

    def __init__(
            self,
            length: int,
            numbers: bool,
            lowercase: bool,
            uppercase: bool
    ):
        self.length = length
        self.numbers = numbers
        self.lowercase = lowercase
        self.uppercase = uppercase

    def collect_numbers(self) -> str:
        """
        Return a string of all numbers.

        :return: the string of numbers.
        :rtype: str

        :Example:
        >>> numbers = CaptchaContentGenerator.collect_numbers()
        >>> numbers
        '0123456789'
        """
        return string.digits if self.numbers else ""

    def collect_lowercase(self) -> str:
        """
        Return a string of all lowercase letters.

        :return: the string of lowercase letters.
        :rtype: str

        :Example:
        >>> lowercases = CaptchaContentGenerator.collect_lowercase()
        >>> lowercases
        'abcdefghijklmnopqrstuvwxyz'
        """
        return string.ascii_lowercase if self.lowercase else ""

    def collect_uppercase(self) -> str:
        """
        Return a string of all uppercase letters.

        :return: the string of uppercase letters.
        :rtype: str

        :Example:
        >>> uppercases = CaptchaContentGenerator.collect_uppercase()
        >>> uppercases
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        """
        return string.ascii_uppercase if self.uppercase else ""

    def create_content(self):
        """
        Return a string of 5 characters from the given numbers, lowercase
        and uppercase letters.

        :return: the string of 5 characters
        :rtype: str

        :Example:
        >>> content = CaptchaContentGenerator.create_content()
        >>> content
        '1a3Bp'
        """
        chars_collection: str = "".join(
            (
                self.collect_numbers(),
                self.collect_lowercase(),
                self.collect_uppercase()
            )
        )

        return "".join(random.choices(chars_collection, k=self.length))

    def create_batch(self, count: int) -> tuple:
        """
        Return a tuple of N samples with captcha content.

        :return: the tuple of N values
        :rtype: tuple

        :Example:
        >>> batch = CaptchaContentGenerator.create_batch(5)
        >>> batch
        ('a34vB', 'mn547', 's2398', 'd12gn', 'po09d')
        """
        return tuple([self.create_content() for _ in range(count)])
