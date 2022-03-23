import string
import random


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

